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


class ExpandedAuditTests(unittest.TestCase):
    def test_references_outside_year_headers_are_checked(self):
        from scripts.proje_denetimi import reference_findings
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'hikaye/notlar').mkdir(parents=True)
            (root / 'README.md').write_text('Bir başka satırda `kayip.md` ve [not](yanlis.md).')
            (root / 'hikaye/notlar/not.md').write_text('Gövde atfı: `olmayan.md`.')
            findings = reference_findings(root)
            self.assertEqual(sum(f[0] == 'ENGEL' for f in findings), 3)
            self.assertTrue(any(f[1].startswith('hikaye/notlar/not.md:') for f in findings))

    def test_templates_and_fences_are_not_fake_broken_links(self):
        from scripts.proje_denetimi import reference_findings
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'README.md').write_text('`yillar/YYYY-baslik.md`\n```\n`ornek.md`\n```\n')
            self.assertEqual(reference_findings(root), [])

    def test_ambiguous_short_reference_is_not_guessed(self):
        from scripts.proje_denetimi import reference_findings
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for folder in ('karakter', 'hikaye'):
                (root / folder).mkdir()
                (root / folder / 'ayni.md').write_text('# Aynı')
            (root / 'README.md').write_text('`ayni.md`')
            self.assertTrue(any('birden fazla' in f[2] for f in reference_findings(root)))

    def test_archived_text_cannot_be_a_year_source(self):
        from scripts.proje_denetimi import reference_findings
        with TemporaryDirectory() as directory:
            root = Path(directory)
            archive = root / 'hikaye/notlar/kaynaktan-ayrilan/eski.md'
            archive.parent.mkdir(parents=True)
            archive.write_text('Eski iç atıf `kayip.md` salt kayıt içinde kalır.')
            path = root / 'hikaye/yillar/1448-test.md'
            path.parent.mkdir()
            path.write_text('Gövde: `../notlar/kaynaktan-ayrilan/eski.md`')
            findings = reference_findings(root)
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0][0], 'ENGEL')
            self.assertIn('Salt kayıt', findings[0][2])

    def test_repository_has_no_broken_active_file_references(self):
        from scripts.proje_denetimi import reference_findings
        self.assertEqual(reference_findings(ROOT), [])

    def test_source_metadata_is_complete_but_not_certification(self):
        from scripts.proje_denetimi import source_metadata_missing
        self.assertEqual(source_metadata_missing('# Başlık\n'),
                         ['Kapsam', 'Güvenilirlik', 'Son güncelleme'])
        for p in (ROOT / 'kaynaklar').rglob('*.md'):
            with self.subTest(path=p):
                self.assertEqual(source_metadata_missing(p.read_text()), [])

    def test_variation_of_stale_appointment_is_detected(self):
        self.assertTrue(stale_arc('Kurtçu Doğan, akıncıların kumandanı oldu.'))
        self.assertTrue(stale_arc('Kurtçu, bir süre sonra akıncı beyi olarak tayin edildi.'))
        self.assertFalse(stale_arc('Kurtçu Doğan akıncı beyi olarak tayin edilemez; bu yanlıştır.'))

    def test_julian_weekday_explicit_format_and_invalid_date(self):
        from scripts.proje_denetimi import weekday_findings
        self.assertEqual(weekday_findings('test.md', '7 Mart 1451 (4 Safer 855) Pazar'), [])
        self.assertTrue(weekday_findings('test.md', '7 Mart 1451 Pazartesi'))
        self.assertEqual(weekday_findings('test.md', '31 Nisan 1451 Pazar')[0][0], 'ENGEL')
        # Jülyende 1500 artık yıldır; Gregoryen kuralı uygulanmaz.
        self.assertNotEqual(weekday_findings('test.md', '29 Şubat 1500 Pazar'),
                            [('ENGEL', 'test.md:1', 'Geçersiz Jülyen tarih: 29 Şubat 1500 Pazar')])

    def test_age_is_completed_age_not_year_subtraction(self):
        from scripts.proje_denetimi import completed_age
        self.assertEqual(completed_age((1432, 3, 30), (1451, 3, 7)), 18)
        self.assertEqual(completed_age((1470, 10, 10), (1520, 9, 22)), 49)
        with self.assertRaises(ValueError):
            completed_age((1452, 1, 1), (1451, 1, 1))

    def test_77_templates_selected_without_41_author_approvals(self):
        from scripts.proje_denetimi import project_metrics, plan_templates, LIMITS
        metrics = project_metrics(ROOT)
        self.assertEqual(metrics['planned_years'], 77)
        self.assertEqual(metrics['written_years'], 8)
        self.assertEqual(metrics['missing_templates'], [])
        self.assertEqual(len(metrics['provisional_templates']), 41)
        plan = plan_templates((ROOT / 'hikaye/02-bolum-plani.md').read_text())
        self.assertEqual(set(plan), set(range(1444, 1521)))
        self.assertTrue(all(template in LIMITS for template in plan.values()))
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'hikaye/yillar').mkdir(parents=True)
            (root / 'hikaye/02-bolum-plani.md').write_text('| **1448** | — | kısa bölüm |')
            (root / 'hikaye/yillar/1448-test.md').write_text('# Eksik sahne sınırları')
            bad = project_metrics(root)
            self.assertEqual(bad['written_years'], 1)
            self.assertTrue(bad['scene_errors'])  # özet, bozuk sahneyi gizlemez veya çökmez

    def test_meryem_relationship_regression_in_real_manuscript_draft(self):
        text = (ROOT / 'hikaye/yillar/1449-anne.md').read_text()
        self.assertNotIn('Kızı on dört yaşında kaldı', text)
        self.assertIn('Torunu daha çocuktu', text)
        self.assertIn("Meryem'in babasıyla konuştu", text)
        self.assertIn('1442', text)

    def test_close_viewpoint_and_unverified_mehir_are_not_hidden(self):
        text = (ROOT / 'hikaye/yillar/1448-sofyadan-kosovaya.md').read_text()
        self.assertNotIn('On dört yıl sonra', text)
        self.assertNotIn("bu ordu Kosova'ya gidiyordu", text)
        wedding = (ROOT / 'hikaye/yillar/1450-dugun.md').read_text()
        self.assertIn('| ⚙ `[?]` |', wedding)
        self.assertIn('Mehmed’in katılımı'.replace('’', "'"), wedding)
        self.assertIn('https://islamansiklopedisi.org.tr/mehmed-ii', wedding)

    def test_draft_scene_style_uses_plain_emphasis_and_one_apostrophe(self):
        from scripts.proje_denetimi import scene_text
        for path in (ROOT / 'hikaye/yillar').glob('*.md'):
            if 1447 <= int(path.name[:4]) <= 1451:
                with self.subTest(path=path):
                    self.assertNotIn('**', scene_text(path.read_text()))
                    self.assertNotRegex(path.read_text(), '[‘’]')


if __name__ == '__main__':
    unittest.main()
