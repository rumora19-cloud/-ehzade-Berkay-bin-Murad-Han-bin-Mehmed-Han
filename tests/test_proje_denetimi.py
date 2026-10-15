import unittest
import subprocess
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from scripts.proje_denetimi import ROOT, scene_count, stale_arc, julian_weekday, migration_payload, migration_findings


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
        self.assertEqual(len(rows), 4)
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
