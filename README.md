# Şehzâde Berkay bin Murad Han bin Mehmed Han

> **Kaynak ayrımı — iki grup / 11 dosya:** İlk dört derlemeye beş kronoloji ve iki hanedan tablosu eklendi. Kayıpsız aktarım ve açık işler: `denetim/2026-10-15-kaynak-ayirma-2.md` (ilk grup: `denetim/2026-10-15-kaynak-ayirma-1.md`). Yazar defteri ve yıl sahneleri değişmedi; arşivin tamamı henüz ayrılmış veya tarihî olarak doğrulanmış değildir.

> **Denetim durumu:** Yeni yıl yazımı durduruldu. 1447–1451 dosyaları kâtip taslağıdır; dosyanın bulunması yazar onayı veya tamamlanma anlamına gelmez. Kurtçu Doğan'ın yanlış akıncı beyliği kaldırıldı. Açık sorunlar ve kontrol sonuçları: `denetim/2026-10-15-proje-denetimi.md`.

**Tarihî kurgu projesi.** II. Murad'ın oğlu, Fâtih Sultan Mehmed'in kardeşi olarak tasarlanmış kurgusal bir Osmanlı şehzadesinin —Şehzâde Berkay— hikâyesi ve bu hikâyenin dayandığı tarihî kaynak arşivi.

Kapsanan dönem: **11 Kasım 1444** (Varna Zaferi'nin ertesi günü) — **1520** (Yavuz Sultan Selim'in ölümü, Kanunî'nin cülûsu).

> **© 2026 rumora19-cloud — Tüm hakları saklıdır.** Buradaki kurgu metinlerinin ve derlemelerin hiçbir parçası yazılı izin olmadan kullanılamaz; ayrıntı ve istisnalar: [`LICENSE`](LICENSE).

## Repo nasıl çalışır?

```
.
├── README.md                  ← bu dosya
├── LICENSE                    ← telif (tüm hakları saklıdır)
├── KILAVUZ.md                 ← yazım, tarih, atıf ve dosya kuralları
├── karakter/                  ← Berkay'ın "Ahvâl Defteri" (yazarın metni) + tashih notları
├── hikaye/                    ← bölümler, plan, sahne notları
├── denetim/                   ← açık bulgular, kaynak fişleri, koruma özetleri
├── scripts/                   ← salt okunur proje denetleyicisi
├── tests/                     ← teknik ve metin regresyon testleri
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

### Durum — 15 Ekim 2026 kritik denetimi

**Dosyanın varlığı tamamlanma veya yazar onayı değildir.** Ayrıntı: `denetim/2026-10-15-kritik-denetim-yaniti.md`.

| Alan | Mevcut durum / açık iş |
|---|---|
| Yıl planı | 77 satır; önceden boş 41 kalıp ⚙ kâtip önerisi olarak seçildi. Öneri dosyası: `hikaye/notlar/kalip-secimi-1444-1520.md`. Yazar onayı değildir. |
| Sahne metinleri | 1444–1451: 8 yıl, 12.323 sahne kelimesi. 1447–1451 onaysız taslak; 69 yılın sahnesi yok. Yeni yıl yazımı duruyor. |
| Kalıp açıkları | 1448 kısa: 430/900; 1449 kısa: 411/900; 1450 tam: 616/2000. Alt sınırlar sağlanmadı; kalıp düşürülmedi, dolgu olay eklenmedi. |
| Kaynak arşivi | 39 Markdown dosyası; tamamında Kapsam/Güvenilirlik/Son güncelleme anahtarları var. Künye, iddiaların doğrulandığı anlamına gelmez. Kalan kurgu karışımları için ayırma işi açık. |
| Kayıpsız ayırma | 11 eski nüsha, commit ve SHA-256 ile korunur. Eski nüshalar ve alıntı dökümleri güncel sahne kaynağı değildir. |
| Kimlik ve tarih denetimi | Yörgüç, Hamza, Has Yunus, Ali ve Gevherhan için doğrudan modern dayanaklar kaydedildi; bütün görev/kimlik zincirleri doğrulanmış değil. `denetim/2026-10-15-dogrudan-kaynak-kontrolu.md`. |
| Yazar defteri | SHA-256 koruması eşleşiyor; Zeyl/§XX dahil değiştirilmedi. Koruma kaydı, bütün tarihî iddiaların doğruluğunun belgesi değildir. |
| Ana hat / çatal / kişi dosyaları | Mevcut çalışma derlemeleri; ✔ yalnız açık yazar kararı, ⚙ yalnız kâtip önerisi/kurgu. Tarihî biyografiyle eşitlenmez. |
| Teknik denetim | Etkin dosya atıfları, künye, 77 kalıp, kayıt nüshasına yanlış sahne atfı, sınırlı hafta günü ve eski görev ifadeleri taranır. Test başarısı tarihî doğruluk onayı değildir. |
| Telif | `LICENSE`: © 2026 rumora19-cloud — tüm hakları saklıdır. |

> **Açık çalışma sırası:** Önce 1447–1451 taslaklarının yazarla yıl sırasına göre ele alınması, 1448–1450'nin dayanaklı redaksiyonu ve kalan kaynak/kimlik incelemeleri. Hiçbir yıl sırf sayıyı doldurmak için genişletilmez; önceki yıl onaylanmadan yenisine geçilmez.
