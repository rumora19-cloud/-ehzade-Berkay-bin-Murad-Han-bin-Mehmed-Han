import unittest
import subprocess
import hashlib
import json
import re
from pathlib import Path
from tempfile import TemporaryDirectory
from scripts.proje_denetimi import ROOT, scene_count, stale_arc, julian_weekday, migration_payload, migration_findings, source_fiction_marker


class AuditTests(unittest.TestCase):
    def test_only_scene_counted(self):
        text = '# Başlık\n> Künye yüz kelime de olabilir\n\n## I\nBir iki üç.\n## II\nDört beş.\n## ⚑ Notlar\nKaynaklar sayılmaz.'
        self.assertEqual(scene_count(text), 5)

    def test_legacy_three_hash_headings(self):
        text = '# Yıl\n### I\nBir iki.\n### II\nÜç.\n### ⚑ Notlar\nSayılmaz.'
        self.assertEqual(scene_count(text), 3)

    def test_julian_anchor_dates(self):
        for date, weekday in [((1451, 3, 7), 6), ((1453, 4, 6), 4),
                              ((1453, 5, 1), 1), ((1476, 12, 31), 1),
                              ((1481, 6, 20), 2)]:
            with self.subTest(date=date):
                self.assertEqual(julian_weekday(*date), weekday)

    def test_author_manuscript_unchanged_since_audit_start(self):
        record = json.loads((ROOT / 'denetim/yazar-metni-korumasi.json').read_text())
        actual = (ROOT / record['path']).read_bytes()
        self.assertEqual(hashlib.sha256(actual).hexdigest(), record['sha256'])

    def test_migration_snapshots_match_recorded_hashes(self):
        rows = json.loads((ROOT / 'denetim/kaynak-ayirma-kaydi.json').read_text())
        self.assertEqual(len(rows), 11)
        self.assertEqual(len({r["source"] for r in rows}), 11)
        self.assertEqual(len({r["archive"] for r in rows}), 11)
        for row in rows:
            with self.subTest(source=row['source']):
                archived = migration_payload((ROOT / row['archive']).read_text())
                self.assertEqual(hashlib.sha256(archived).hexdigest(), row['sha256'])
                # Git nesnesi varsa ek karşılaştırma; kayıpsızlık hash testi sığ klonda da zorunlu.
                result = subprocess.run(
                    ['git', 'show', row['source_commit'] + ':' + row['source']],
                    cwd=ROOT, capture_output=True)
                if result.returncode == 0:
                    self.assertEqual(archived, result.stdout)
        self.assertEqual(migration_findings(ROOT), [])

    def test_corrupted_archive_is_blocker(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'denetim').mkdir()
            (root / 'archive.md').write_text('Kayıp nüsha')
            (root / 'source.md').write_text('Genel coğrafya')
            row = {'source': 'source.md', 'archive': 'archive.md', 'sha256': 'bad'}
            (root / 'denetim/kaynak-ayirma-kaydi.json').write_text(json.dumps([row]))
            self.assertTrue(any(f[0] == 'ENGEL' for f in migration_findings(root)))

    def test_calendar_dates_unchanged_when_age_column_removed(self):
        rows = json.loads((ROOT / 'denetim/kaynak-ayirma-kaydi.json').read_text())
        row = next(x for x in rows if x['source'].endswith('/takvim-ve-zaman.md'))
        old = migration_payload((ROOT / row['archive']).read_text()).decode()
        new = (ROOT / row['source']).read_text()
        import re
        def data(text):
            return [line.split('|')[1:-1] for line in text.splitlines()
                    if re.match(r'^\| \d{3} \|', line)]
        old_rows, new_rows = data(old), data(new)
        self.assertEqual(len(old_rows), 80)
        self.assertEqual(len(new_rows), 80)
        for before, after in zip(old_rows, new_rows):
            self.assertEqual(before[:6] + before[7:], after)

    def test_historical_mary_is_not_fictional_meryem(self):
        self.assertFalse(source_fiction_marker("(Papa'nın mektubu, Bellini'nin Meryem resmi) `[T]`"))
        for text in ("Meryem Hatun", "Meryem'in ailesi", "Berkay", "⚙", "🎭",
                     "Bellini'nin Meryem resmi",  # bağlamsız kullanım istisna değildir
                     "(Papa'nın mektubu, Bellini'nin Meryem resmi); Meryem Hatun"):
            with self.subTest(text=text):
                self.assertTrue(source_fiction_marker(text))

    def test_first_batch_pins_not_replaced(self):
        expected = {
            'kisiler-1451-1520.md': '66538aa0b381f78fde7dee3f6efbfa20d0008d1fd71c710fe333c5fcaebb93ed',
            'devlet-adamlari-1444-1451.md': 'ab6b5374da4ffe3e40d56fcffc2164d6afb8fe86384fda9132b2fcc5a118d8da',
            'italya.md': '11088a9c8fdc81f6eac919e862f71c97d20a7020df5ba93a694d7aefef21f579',
            'takvim-ve-zaman.md': '5c2d1769ed98a6b7fb6a3cf3f5e056bc1b9ba7ea464d233f107d4fecd9a25e5f',
        }
        rows = json.loads((ROOT / 'denetim/kaynak-ayirma-kaydi.json').read_text())
        self.assertEqual({Path(r['source']).name: r['sha256'] for r in rows[:4]}, expected)
        self.assertTrue(all(r['source_commit'] == '312d904e36ee6c982248ae3aa6d691a602bd7151'
                            for r in rows[:4]))

    def test_second_batch_all_changed_lines_have_provenance(self):
        rows = json.loads((ROOT / 'denetim/kaynak-ayirma-kaydi.json').read_text())
        group = [r for r in rows if r.get('batch') == 2]
        self.assertEqual(len(group), 7)
        for row in group:
            with self.subTest(source=row['source']):
                old = migration_payload((ROOT / row['archive']).read_text()).decode()
                current = (ROOT / row['source']).read_text()
                notes = (ROOT / row['application_notes']).read_text()
                self.assertIn(row['source_commit'], notes)
                self.assertIn('../../' + row['application_notes'], current)
                self.assertIn('../../' + row['archive'], current)
                # Tam nüshaya ek olarak, değişen her dolu satırın okunabilir dökümü.
                for number, line in enumerate(old.splitlines(), 1):
                    if line.strip() and line not in current.splitlines():
                        ranges = re.findall(r'^## Kaynak satırları (\d+)–(\d+)$', notes, re.M)
                        self.assertTrue(any(int(a) <= number <= int(b) for a, b in ranges))
                        self.assertIn('> ' + line, notes)

    def test_historical_suffixes_and_religious_image_survive(self):
        rows = json.loads((ROOT / 'denetim/kaynak-ayirma-kaydi.json').read_text())
        for row in rows:
            if row.get('batch') != 2:
                continue
            with self.subTest(source=row['source']):
                old = migration_payload((ROOT / row['archive']).read_text()).decode()
                current = (ROOT / row['source']).read_text()
                for line in old.splitlines():
                    # Karışık satırın kanca öncesindeki tarihî bölümü korunmalı.
                    if line.startswith(('- ', '| ')) and '🎭' in line:
                        if line.startswith('- **Tarih:** 1446'):
                            continue  # özel gün aralığı da kurgu; başka teste tâbi
                        self.assertIn(line.split('🎭', 1)[0].rstrip(), current)
                if Path(row['source']).name.startswith('02-fatih'):
                    wedding = next(l for l in old.splitlines() if l.startswith('- **1457:**'))
                    self.assertIn(wedding[wedding.index('Papalık donanması'):], current)
                    self.assertIn("Bellini'nin Meryem resmi", current)
                    self.assertIn("Belgrad'dan sonra", current)
                if Path(row['source']).name.startswith('04-yavuz'):
                    self.assertIn("Ölüm gizlenir; **Süleyman Manisa'dan 30 Eylül İstanbul'a**", current)
                    self.assertIn('**28 Mayıs İskenderiye**', current)

    def test_unmarked_historical_sections_remain_in_place(self):
        rows = json.loads((ROOT / 'denetim/kaynak-ayirma-kaydi.json').read_text())
        blocks = {
            '00-genel-zaman-cizelgesi-1444-1520.md': ('## Dönüm noktaları', None),
            '02-fatih-donemi-1451-1481.md': ('## 13.', '## 14.'),
            '03-ii-bayezid-donemi-1481-1512.md': ('## 10.', '## 11.'),
            '04-yavuz-selim-donemi-1512-1520.md': ('## 12.', '## 13.'),
            'hanedan-1451-1520.md': ('## 4.', '## 5.'),
        }
        for row in rows:
            if row.get('batch') != 2:
                continue
            old = migration_payload((ROOT / row['archive']).read_text()).decode()
            current = (ROOT / row['source']).read_text().splitlines()
            start, end = blocks.get(Path(row['source']).name, (None, None))
            inside = False
            for line in old.splitlines():
                if start and line.startswith(start):
                    inside = True
                if inside and end and line.startswith(end):
                    inside = False
                if inside or not line.strip() or source_fiction_marker(line):
                    continue
                if 'Evrenosoğlu Ali Bey eliyle; Dukas' in line:
                    # Bir kimlik kesinliği kaldırıldı; yeni tarihî doğrulama iddiası yok.
                    self.assertTrue(any('özdeşliği `[?]`' in l for l in current))
                    continue
                with self.subTest(source=row['source'], line=line[:90]):
                    self.assertIn(line, current)

    def test_missing_application_notes_is_blocker(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'denetim').mkdir()
            payload = b'Tarih\n'
            (root / 'archive.md').write_bytes(b'````markdown\n' + payload + b'````\n')
            (root / 'source.md').write_bytes(payload)
            row = {'source': 'source.md', 'archive': 'archive.md',
                   'sha256': hashlib.sha256(payload).hexdigest(), 'application_notes': 'missing.md'}
            (root / 'denetim/kaynak-ayirma-kaydi.json').write_text(json.dumps([row]))
            self.assertTrue(any(f[0] == 'ENGEL' and f[1] == 'missing.md'
                                for f in migration_findings(root)))

    def test_missing_scene_rejected(self):
        with self.assertRaises(ValueError):
            scene_count('# Başlık\n## ⚑ Notlar')

    def test_old_appointment_detected(self):
        self.assertTrue(stale_arc("Lala'nın ucuna akıncı beyi gider"))

    def test_disguised_command_detected(self):
        self.assertTrue(stale_arc("Kurtçu Doğan'ın akıncıları Vlad'ı getirir"))

    def test_author_correction_not_flagged(self):
        self.assertFalse(stale_arc('Kurtçu Doğan akıncı beyi yapılmaz. Akşemseddin’e sığınır.'))


if __name__ == '__main__':
    unittest.main()
