# Çalışma Kılavuzu

Bu dosya, repodaki bütün metinlerin uyması gereken kuralları toplar. Kısa tutulmuştur; şüphede kalınan her durumda buraya eklenir.

## 1. Dosya ve klasör adları

- Dosya adları **ASCII** (Türkçe karakter yok), küçük harf, tire ile: `ii-murad-ikinci-saltanat-1444-1451.md`.
- Başlıklar ve metin **Türkçe**, Türkçe karakterli.
- Her kaynak dosyasının başında kısa bir **künye bloğu** bulunur:

```
> **Kapsam:** 1444–1451 · **Güvenilirlik:** yüksek · **Son güncelleme:** 2026-10-14
> **Ana kaynaklar:** İnalcık, "Murad II" (DİA); Gazavât-ı Sultan Murad; Âşıkpaşazâde
```

## 2. Tarihler

- Önce **milâdî**, parantez içinde **hicrî**: `10 Kasım 1444 (28 Receb 848)`.
- Hicrî tarih bilinmiyorsa sadece milâdî yazılır; tahminî ise `~1447` veya `1447/48`.
- Çağdaş kaynaklar arasında fark varsa ikisi de verilir: `3 Şubat 1451 (İnalcık) / 5 Şubat (Babinger)`.
- Julyen–Gregoryen farkı: Dönem tarihleri **Julyen** takvimiyledir (Avrupa kaynaklarında da öyledir); dönüştürülmez.

## 3. Güvenilirlik etiketleri

Her olay/iddia satırının başına gerekirse etiket konur:

| Etiket | Anlamı |
|---|---|
| `[K]` | Kesin: birden çok çağdaş kaynak + modern araştırma uyumlu |
| `[M]` | Muhtemel: tek güvenilir kaynak veya küçük tarih farkları |
| `[T]` | Tartışmalı: kaynaklar çelişiyor; modern tarihçiler bölünmüş |
| `[R]` | Rivayet/menkıbe: edebî-geleneksel anlatı, tarihî doğruluğu belirsiz ama **hikâye için kullanışlı** |
| `[?]` | Doğrulanacak: henüz kaynağına inilmedi |

## 4. Atıf biçimi

- DİA (TDV İslâm Ansiklopedisi): `İnalcık, "Murad II", DİA, https://islamansiklopedisi.org.tr/murad-ii`
- Kronik: `Âşıkpaşazâde, Tevârîh-i Âl-i Osmân (nşr. Giese), s. 112` — neşir adı mutlaka yazılır, çünkü sayfa numaraları neşirden neşire değişir.
- Modern eser: `İnalcık, Fatih Devri Üzerinde Tetkikler ve Vesikalar I (TTK 1954), s. 70-104`.
- Web: tam URL + erişim tarihi.

## 5. Telif ve metin alıntısı

- **Özgün Osmanlı kronik metinleri** (Âşıkpaşazâde, Neşrî, Oruç Bey, Tursun Bey, anonimler…) telif dışıdır; ancak modern **neşir, transkripsiyon ve çeviriler** telifli olabilir. Kısa alıntı (birkaç cümle) + atıf serbest; uzun blok kopyalama yapılmaz.
- DİA maddeleri telifli: **özetlenir**, kısa alıntı + bağlantı verilir.
- Vikipedi (CC BY-SA): kullanılırsa belirtilir; tek başına kaynak sayılmaz, mutlaka DİA/akademik kaynakla çapraz kontrol edilir.

## 6. Hikâye kancaları

Kaynak dosyalarında, tarihî bir ayrıntının kurgu için kullanılabileceği yerler **🎭** işaretiyle gösterilir. Bunlar öneri niteliğindedir; `hikaye/` klasörüne taşınıp işlenmedikçe bağlayıcı değildir.

## 7. Kurgu / tarih ayrımı

- `kaynaklar/` altında **asla** kurgusal karakter yer almaz (Berkay dahil).
- `karakter/` ve `hikaye/` altındaki dosyalar tarihî kişileri kullanabilir; fakat tarihî kişiye atfedilen **kurgusal** söz ve eylemler, gerçek kayıtlarla açıkça çelişiyorsa dosya içinde `⚠ kronoloji notu` ile açıklanır (bilinçli sapma mı, hata mı?).

## 8. Dil ve üslup (hikâye metni için ön ilkeler)

- Anlatı dili çağdaş Türkçe; diyaloglarda dönem rengi **hitap ve unvanlarla** verilir (*Sultanım, devletlü, Çelebi, Paşa hazretleri, lala, ağa, kadı efendi, bey*), uydurma "eski Türkçe" taklidi yapılmaz.
- Şehzadeler 15. yüzyılın ilk yarısında **"Çelebi"** (Mehmed Çelebi, Alâeddin Ali Çelebi); Fâtih'ten itibaren **"Sultan"** (Sultan Cem, Sultan Korkud, Sultan Bayezid) olarak anılır. Berkay için 1444–1451'de "Berkay Çelebi", sonrası için "Sultan Berkay" uygundur. (Bk. `kaynaklar/05-kurumlar/sehzadelik-sistemi.md`.)
- Yer adları dönem biçimiyle: Kostantiniyye/İstanbul (1453 sonrası ikisi de), Edirne, Burusa/Bursa, Mağnisa/Manisa, Amasya, Selânik, Üsküb, Semendire, Belgrad, Eğriboz, İnebahtı, Mora, Eflak, Boğdan, Erdel, Engürüs (Macaristan), Frengistan.
