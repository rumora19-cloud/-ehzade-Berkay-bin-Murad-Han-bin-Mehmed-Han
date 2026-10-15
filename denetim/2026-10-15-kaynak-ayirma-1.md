# Kaynak–kurgu ayrımı — ilk çalışma grubu

> **Tarih:** 15 Ekim 2026 · **Durum:** dört dosyada ayırma tamamlandı; tarihî doğrulama ve arşivin geri kalanı açık.
> **Sınır:** Yeni yıl, sahne, karakter kaderi veya 1600 sonrası sınır kararı yazılmadı. Bu çalışma yazarın asıl defterine müdahale etmez.

## 1. Ne değişti?

| Kaynak dosyası | Ayrılan içerik | Kaynakta kalan |
|---|---|---|
| `kaynaklar/03-kisiler/kisiler-1451-1520.md` | Tablolardaki kurgu temas sütunu; Vlad'ın alternatif ölüm günü ve tarihî biyografiye sızan kurgu ölümleri | Tarihî biyografi derlemesi; belgesiz kimlik/tarih iddiaları için açık inceleme notları |
| `kaynaklar/03-kisiler/devlet-adamlari-1444-1451.md` | §E temas önerileri, gömülü hikâye kancaları ve kurgu çocukluk bağlantıları | Devlet adamları derlemesi; Ali Bey ve Hamza Bey için kesinlik yerine inceleme kaydı |
| `kaynaklar/04-yerler/italya.md` | Coğrafya/siyaset/kişi tablolarındaki hikâye sütunları, alternatif sefer/ölüm/idarî görev haritası | Coğrafya, Otranto 1480–81 ve gerçek İtalya siyaseti derlemesi; bütün tarihî ayrıntılar bu işlemle doğrulanmış sayılmaz |
| `kaynaklar/06-gunluk-hayat/takvim-ve-zaman.md` | Kişiye bağlı yaş sütunu, doğum günü bağlantısı, kurgu olay/yaş örnekleri | 80 satırlık genel tarih tablosu, aylar ve zaman algısı; tarihler yeniden hesaplanmadı |

Kişi ve görev bilgilerini kaynaklardan ayırırken boşluğu yeni bir ad, tarih veya makamla doldurmadım. Kaynak dosyasında `[?]` bırakılan bir iddia otomatik olarak yanlış ilan edilmedi; doğrudan dayanağı henüz gösterilmediği açıklandı.

## 2. Bilgi kaybını nasıl önledim?

Dört dosyanın işlem öncesi metni, **tam bayt içeriğiyle**, `hikaye/notlar/kaynaktan-ayrilan/` altında saklandı. Bunlar yeni kaynak veya geçerli kurgu kararı değil, eski karışık çalışma nüshalarıdır. İçlerindeki eski yanlışlar ve adlar tarihî kayıt diye yeniden kullanılmamalı.

- Her nüshada özgün dosya yolu, başlangıç commit'i `312d904e36ee6c982248ae3aa6d691a602bd7151` ve SHA-256 var.
- Makine okunur aktarım kaydı: `denetim/kaynak-ayirma-kaydi.json`.
- Testler, saklanan metinlerin özetini denetliyor; Git nesnesi mevcutsa özgün commit içeriğiyle de karşılaştırıyor.
- Takvim testinde, kaldırılan yaş sütunu dışındaki **80 satırın hücrelerinin aynı kaldığı** ayrıca kontrol ediliyor.

Kullanılacak kurgu çalışma kayıtları:

- `hikaye/notlar/italya-uygulamasi.md`: önceki İtalya §6 seyrinin aktarımı; yeni karar değildir.
- `hikaye/notlar/yas-ve-takvim-uygulamasi.md`: önceki yaş hesabı ve örnekler; sayısal/kavramsal sorunlar çözülmüş sayılmaz. Ölümden sonraki satırlardaki yaşlar kişinin yaşadığı anlamına gelmez.

Planın ilgili İtalya ve yaş atıfları bu notlara yönlendirildi. Kaynak §6 gibi eski bölüm numaraları sessizce başka konuya verilmedi; ayırmayı açıklayan yönlendirmeler bırakıldı. INDEX ve ilgili README açıklamaları güncellendi.

## 3. Üç kişi incelemesi nerede?

Ayrıntılı fiş: `denetim/uc-kisi-kaynak-incelemesi.md`.

- **Evrenosoğlu Ali Bey:** Dukas'a atfedilen Küçük Ahmed anlatısındaki Ali Bey ile özdeşlik, idam kaydı ve 1462 faaliyeti arasında çözülmemiş bir kimlik sorunu var. Önceki metin bu sorunu hem kabul edip hem kesin özdeşlik kuruyordu. İlgili özetlere `[?]` notu eklendi; kurgu Lala kararı korunuyor.
- **Hamza Bey:** beylerbeyilik, kapudanlık, elçilik ve belirli ölüm ayının tek biyografide birleştirilmesi doğrudan dayanak bekliyor. Hikâyenin 20 Nisan 1453 / Şubat 1462 tercihleri değiştirilmedi; tarihî doğrulama ile kurgu tercihi ayrı tutuldu.
- **Has Yunus Bey:** 1456 kapudanlık/Enez–Limni kaydına doğrudan atıf henüz gösterilmedi. Silâhdarlığı ve 1462'deki ölümü kurgu uygulaması olarak kalıyor.

**Bu turda dış kaynaklar okunmuş gibi davranılmadı.** Yeni sayfa numarası, alıntı veya erişim tarihi üretilmedi. İnceleme fişi hangi metinlerin hangi sorular için karşılaştırılacağını gösterir; tarihî kişilerin doğrulamasının tamamlandığını iddia etmez.

## 4. Kontroller

```bash
python3 -m unittest discover -s tests -v
python3 scripts/proje_denetimi.py
python3 scripts/proje_denetimi.py --strict
```

- **11 test geçiyor.** Önceki 8 kontrole kayıpsız nüsha, bozuk aktarımın yakalanması ve takvim hücrelerinin korunması eklendi.
- İlk dört ayrılmış dosyaya kurgu adı/işareti geri girerse veya arşiv özeti bozulursa denetleyici engel veriyor. Bu sözcük taraması tarih uzmanı yerine geçmez.
- Yazarın defterinin `43f6a20d3d5fbe508cf5f0d014642e7d900fcb2b` commit'indeki metinle bayt düzeyinde aynı olduğu tekrar karşılaştırıldı. Özet `denetim/yazar-metni-korumasi.json` içinde sabitlendi; kontrol artık eski Git nesnesinin sığ klonda bulunmasına bağımlı değil. Yeni yazar onayı olmadan bu kayıt değiştirilmez.
- Genel tarama: **3 kalıp engeli + 30 kaynak/kurgu inceleme kaydı.** Önceki sayı 35'ti; dört kaynak dosyası ve yaş açıklaması temizlenen günlük hayat README'si artık eşleşmiyor. Sayının azalması bütün tarihî iddiaların doğrulandığı anlamına gelmez.
- `--strict` üç eksik bölüm nedeniyle hâlâ başarısız olmalıdır. Eşikler düşürülmedi; sahne eklenmedi.

## 5. Sıradaki iş

1. Kalan kaynak dosyalarının ayırmasını aynı köken/kayıpsızlık yöntemiyle sürdürmek; öncelik dönem kronolojileri ve hanedan tabloları.
2. Üç kişi için ilgili neşir/biyografi kayıtlarını doğrudan karşılaştırıp inceleme fişindeki her satırı atıfla sonuçlandırmak.
3. Kaynak ayrımı ve kimlik incelemesi bitmeden mevcut yıl taslaklarına yeni olay eklememek. Yazarın yıl onayı sırası hâlâ geçerlidir.

Bu rapor yalnız ilk grubun teslimidir; önceki denetimdeki D21 arşiv geneli için açık kalır.
