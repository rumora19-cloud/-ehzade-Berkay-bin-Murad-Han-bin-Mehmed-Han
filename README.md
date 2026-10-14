# Şehzâde Berkay bin Murad Han bin Mehmed Han

**Tarihî kurgu projesi.** II. Murad'ın oğlu, Fâtih Sultan Mehmed'in kardeşi olarak tasarlanmış kurgusal bir Osmanlı şehzadesinin —Şehzâde Berkay Çelebi— hikâyesi ve bu hikâyenin dayandığı tarihî kaynak arşivi.

Kapsanan dönem: **11 Kasım 1444** (Varna Zaferi'nin ertesi günü) — **1520** (Yavuz Sultan Selim'in ölümü, Kanunî'nin cülûsu).

## Repo nasıl çalışır?

```
.
├── README.md                  ← bu dosya
├── KILAVUZ.md                 ← yazım, tarih, atıf ve dosya kuralları
├── karakter/                  ← Berkay'ın "Ahvâl Defteri" ve soy ağacı
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
| Fâtih dönemi 1451–1481 (ayrıntılı) | ⏳ sırada |
| II. Bayezid dönemi 1481–1512 (ayrıntılı) | ⏳ |
| Yavuz dönemi 1512–1520 (ayrıntılı) | ⏳ |
| Şehzadelik sistemi | ✅ ilk sürüm |
| Hanedan (II. Murad ailesi) | ✅ ilk sürüm (doğrulanacak maddeler işaretli) |
| Saray, ordu, günlük hayat, yerler | ⏳ |
| Karakter dosyası (Ahvâl Defteri) | ⏳ PDF bekleniyor |

> Not: Bu repo bir **kurgu** projesidir. `kaynaklar/` altındaki her şey tarihî kayıtlara dayanır ve atıflıdır; `karakter/` ve `hikaye/` altındakiler kurgudur. İkisi hiçbir zaman karıştırılmaz.
