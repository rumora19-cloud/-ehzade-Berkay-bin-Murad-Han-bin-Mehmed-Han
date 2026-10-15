#!/usr/bin/env python3
"""Metin içi tutarlılık taraması. Tarihî doğrulama/yazar onayı yerine geçmez.

python3 scripts/proje_denetimi.py           # bulguları gösterir
python3 scripts/proje_denetimi.py --strict  # açık engel varsa başarısız olur
python3 -m unittest discover -s tests -v    # denetleyicinin kendi testleri
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIMITS = {'tam bölüm': (2000, 5000), 'kısa bölüm': (900, 2000),
          'defter yaprağı': (400, 900)}
# Yalnız eski, olumlu tayin ifadeleri. Yeni düzeltmenin olumsuz cümleleri yasak değildir.
STALE = ("Lala'nın ucuna akıncı beyi", "Lala'nın yanına Rumeli ucuna akıncı beyi",
         "Rumeli ucuna akıncı beyi olarak gönderilir", "Kurtçu Doğan uca;",
         "Kurtçu Doğan'ın akıncıları", "Kurtçu Doğan ağalıktan uca.",
         "Kurtçu Doğan Ağa Lala'nın ucuna gider", "Kurtçu Doğan sürülmez, uca gider")


def julian_weekday(year: int, month: int, day: int) -> int:
    """Jülyen tarihin hafta günü: Pazartesi=0, Pazar=6; hicrî dönüşüm değildir."""
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    jdn = day + (153 * m + 2) // 5 + 365 * y + y // 4 - 32083
    return jdn % 7


def scene_text(text: str) -> str:
    """Künye ve son kâtip tablosunu saymadan sahneleri çıkarır."""
    start = re.search(r'^#{2,3} I\s*$', text, re.M)
    end = re.search(r'^#{2,3} ⚑', text, re.M)
    if not start or not end or end.start() <= start.end():
        raise ValueError('Sahne başlangıcı veya ⚑ tablosu eksik')
    body = text[start.end():end.start()]
    body = re.sub(r'^#{2,3} [IVXLCDM]+\s*$', '', body, flags=re.M)
    return body.strip()


def scene_count(text: str) -> int:
    # Basit ve yeniden üretilebilir ölçü: boşlukla ayrılmış birimler.
    return len(scene_text(text).split())


def stale_arc(text: str) -> list[str]:
    return [phrase for phrase in STALE if phrase in text]


def audit(root: Path = ROOT) -> list[tuple[str, str, str]]:
    findings: list[tuple[str, str, str]] = []
    plan = (root / 'hikaye/02-bolum-plani.md').read_text(encoding='utf-8')
    for path in sorted((root / 'hikaye/yillar').glob('*.md')):
        relative = path.relative_to(root).as_posix()
        text = path.read_text(encoding='utf-8')
        year = path.name[:4]
        row = next((line for line in plan.splitlines()
                    if line.startswith(f'| **{year}**')), '')
        template = row.split('|')[-2].strip() if row else ''
        try:
            n = scene_count(text)
        except ValueError as exc:
            findings.append(('ENGEL', relative, str(exc)))
            continue
        if template in LIMITS:
            low, high = LIMITS[template]
            if not low <= n <= high:
                findings.append(('ENGEL', relative,
                                 f'{template}: {n} sahne kelimesi; gerekli {low}–{high}.'))
        else:
            findings.append(('İNCELE', relative, 'Kalıp seçilmemiş veya tanınmıyor.'))
        # Tam yol verilen atıflar kontrol edilir; kısaltılmış adlar ayrıca elle incelenir.
        for line in text.splitlines():
            if not line.startswith('> **Kaynak:**'):
                continue
            for m in re.finditer(r'`([^`]+\.md)`(?:\s*§(\d+))?', line):
                name, section = m.groups()
                if '/' not in name or '…' in name:
                    continue
                candidates = [root / name, path.parent / name]
                target = next((q for q in candidates if q.is_file()), None)
                if target is None:
                    findings.append(('ENGEL', relative, f'Atıf dosyası yok: {name}'))
                elif section and not re.search(
                        rf'^#{{2,3}} {section}\.\s',
                        target.read_text(encoding='utf-8'), re.M):
                    findings.append(('İNCELE', relative,
                                     f'Bölüm atfı bulunamadı: {name} §{section}'))
    for folder in ('hikaye', 'karakter', 'kaynaklar'):
        for path in sorted((root / folder).rglob('*.md')):
            text = path.read_text(encoding='utf-8')
            for phrase in stale_arc(text):
                findings.append(('ENGEL', path.relative_to(root).as_posix(),
                                 f'Eski Kurtçu Doğan seyri: {phrase}'))
    # Bir kanıt değil, aday tespitidir: aktarılacak kurgu parçalarını insan inceleyecek.
    for path in sorted((root / 'kaynaklar').rglob('*.md')):
        text = path.read_text(encoding='utf-8')
        matches = [(i, line) for i, line in enumerate(text.splitlines(), 1)
                   if re.search(r'Berkay|Meryem|⚙', line)]
        if matches:
            findings.append(('İNCELE', path.relative_to(root).as_posix(),
                             f'Kaynak/kurgu ayrımı adayı: {len(matches)} satır; '
                             'eşleşme tek başına tarihî hata kanıtı değildir.'))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--strict', action='store_true')
    args = parser.parse_args()
    findings = audit()
    for level, path, message in findings:
        print(f'[{level}] {path}: {message}')
    blockers = sum(level == 'ENGEL' for level, _, _ in findings)
    review = len(findings) - blockers
    print(f'\n{blockers} açık engel; {review} elle inceleme kaydı. '
          'Bu tarama tarihî doğrulama veya yazar onayı değildir.')
    return 1 if args.strict and blockers else 0


if __name__ == '__main__':
    raise SystemExit(main())
