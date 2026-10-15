import unittest
import subprocess
from scripts.proje_denetimi import ROOT, scene_count, stale_arc, julian_weekday


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
        path = 'karakter/sehzade-berkay-ahval-defteri.md'
        original = subprocess.check_output(['git', 'show', '43f6a20:' + path], cwd=ROOT)
        self.assertEqual((ROOT / path).read_bytes(), original)

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
