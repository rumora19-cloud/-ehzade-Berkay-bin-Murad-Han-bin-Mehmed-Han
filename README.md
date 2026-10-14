# Şehzâde Berkay bin Murad Han bin Mehmed Han

**Tarihî kurgu projesi.** II. Murad'ın oğlu, Fâtih Sultan Mehmed'in kardeşi olarak tasarlanmış kurgusal bir Osmanlı şehzadesinin —Şehzâde Berkay— hikâyesi ve bu hikâyenin dayandığı tarihî kaynak arşivi.

Kapsanan dönem: **11 Kasım 1444** (Varna Zaferi'nin ertesi günü) — **1520** (Yavuz Sultan Selim'in ölümü, Kanunî'nin cülûsu).

## Repo nasıl çalışır?

```
.
├── README.md                  ← bu dosya
├── KILAVUZ.md                 ← yazım, tarih, atıf ve dosya kuralları
├── karakter/                  ← Berkay'ın "Ahvâl Defteri" (yazarın metni) + tashih notları
├── hikaye/                    ← bölümler, plan, sahne notları
└── kaynaklar/                 ← TARİHÎ KAYNAK ARŞİVİ (hikâyenin omurgası)
    ├── 00-INDEX.md            ← kaynak haritası: hangi soru için hangi dosya
    ├── 01-kronoloji/          ← 1444–1520 yıl yıl, dönem dönem olaylar
    ├── 02-birincil-kaynaklar/ ← Osmanlı kronikleri, Bizans & Batı kaynakları kataloğu
    ├── 03-kisiler/            ← hanedan, devlet adamları, yabancı hükümdarlar
    ├── 04-yerler/             ← Edirne, Manisa, Amasya, Bursa, İstanbul, Konya, Trabzon...
    ├── 05-kurumlar/           ← şehzadelik, saray, ordu, divan, hukuk
    ├── 06-gunluk-hayat/       ← dil, hitap, kıyafet, yemek, takvim, para
    ├── 07-sozluk/             ← dönem terimleri sözlüğü
    └── 08-ikincil-kaynaklar/  ← modern araştırmalar (İnalcık, Babinger, Emecen...)
```

### İş akışı

1. **Hikâye yazarken:** Sahnenin geçtiği yıla `kaynaklar/01-kronoloji/` içinden bakılır; geçen kişiler `03-kisiler/`, mekân `04-yerler/`, protokol/kurum `05-kurumlar/`, dil ve eşya `06-gunluk-hayat/` dosyalarından doğrulanır. Her bölümün sonuna **"Dayandığı kaynaklar"** listesi eklenir.
2. **Karakter dosyasını güncellerken:** Berkay'ın hayatındaki her kurgusal olay, aynı tarihteki gerçek olaylarla (`00-genel-zaman-cizelgesi`) çakıştırılır; çelişki varsa `karakter/` içindeki dosyaya "⚠ kronoloji notu" düşülür.
3. **Yeni kaynak eklerken:** `KILAVUZ.md`'deki atıf biçimi kullanılır; telifli metinler özetlenir, telifsiz/erişilebilir metinlere bağlantı verilir.

### Durum

| Alan | Durum |
|---|---|
| Kaynak kataloğu (birincil) | ✅ ilk sürüm |
| Genel zaman çizelgesi 1444–1520 | ✅ ilk sürüm |
| II. Murad ikinci saltanatı 1444–1451 (ayrıntılı) | ✅ ilk sürüm |
| Fâtih dönemi 1451–1481 (ayrıntılı) | ✅ ilk sürüm (yıl yıl; §13 hikâye düğümleri) |
| II. Bayezid dönemi 1481–1512 (ayrıntılı) | ✅ ilk sürüm |
| Yavuz dönemi 1512–1520 (ayrıntılı) | ✅ ilk sürüm |
| Şehzadelik sistemi | ✅ ilk sürüm |
| Hanedan (II. Murad ailesi) | ✅ ilk sürüm (doğrulanacak maddeler işaretli) |
| Yerler (Edirne, Bursa, Manisa, Amasya, İstanbul, sancaklar, savaş alanları, yol süreleri; **Varna**; **İtalya 1480–1520**) | ✅ ilk sürüm (`varna.md`, `italya.md` 2026-10-15) |
| Kurumlar (ordu; saray–divan–devlet; hitap kılavuzu; **hukuk: kanunnâme–kadı–kazasker–müftü–ceza**) | ✅ ilk sürüm (`hukuk-kanun-ve-kadi-1444-1520.md` 2026-10-15) |
| Günlük hayat (takvim tablosu 1444–1521, para, tıp, kıyafet–yemek–meclis, dil–inanç) | ✅ ilk sürüm |
| Hanedan ve kişiler 1451–1520; kaynak × dönem matrisi | ✅ ilk sürüm |
| Karakter dosyası (Ahvâl Defteri) | ✅ işlendi; tashih C1, C3–C6, C9–C12 yazar onayıyla uygulandı (`karakter/sehzade-berkay-ahval-defteri.md`, döküm `tashih-notlari.md` §H) |
| Hikâye ana hattı (üç padişahlık kavis) | ✅ derlendi (`hikaye/00-ana-hat.md`) — ✔ yazar kararları / ⚙ kâtip kararları işaretli |
| Yıl yıl plan (1444–1520, 77 yıl; kitap bölümlemesi kaldırıldı) | ✅ yazar kararı 15 Ekim 2026 (`hikaye/02-bolum-plani.md`) |
| Yıl metinleri | ✎ 1444 ve 1445 yazıldı (`hikaye/yillar/1444-saf-beni-gecti.md`, `1445-golge.md`); sırada 1446 |
| Kaynak dosyalarındaki 🎭 hikâye notları | ✅ nihai kurguya göre güncellendi (2026-10-15): Berkay 1451–81, II. Orhan 1481–1512, Selim 1512–20 |
| Çatal noktaları (gerçek tarih → kurgu, yıl yıl) | ✅ ilk sürüm (`hikaye/01-catal-noktalari.md`) |
| Kurgusal hanedan ve çevre dosyaları (Berkay soyu, Mehmed soyu, çevre kişiler) | ✅ derlendi (`karakter/`) |
| Karakter dosyasının tarihî tashihi | ✅ ilk sürüm (`karakter/tashih-notlari.md`) — yazar onayı bekleniyor |

> Not: Bu repo bir **kurgu** projesidir. `kaynaklar/` altındaki her şey tarihî kayıtlara dayanır ve atıflıdır; `karakter/` ve `hikaye/` altındakiler kurgudur. İkisi hiçbir zaman karıştırılmaz.
