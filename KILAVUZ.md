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
- **Depo lisansı:** © 2026 rumora19-cloud — tüm hakları saklıdır (`LICENSE`). Kısa, kaynak gösterilerek yapılan akademik alıntı (iktibas) serbesttir; kurgu metinlerinin kopyalanması, çevrilmesi ve uyarlanması yazılı izne bağlıdır.
- Vikipedi (CC BY-SA): kullanılırsa belirtilir; tek başına kaynak sayılmaz, mutlaka DİA/akademik kaynakla çapraz kontrol edilir.

## 6. Hikâye kancaları

Kaynak dosyalarında, tarihî bir ayrıntının kurgu için kullanılabileceği yerler **🎭** işaretiyle gösterilir. Bunlar öneri niteliğindedir; `hikaye/` klasörüne taşınıp işlenmedikçe bağlayıcı değildir.

## 7. Kurgu / tarih ayrımı

- `kaynaklar/` altında **asla** kurgusal karakter yer almaz (Berkay dahil).
- `karakter/` ve `hikaye/` altındaki dosyalar tarihî kişileri kullanabilir; fakat tarihî kişiye atfedilen **kurgusal** söz ve eylemler, gerçek kayıtlarla açıkça çelişiyorsa dosya içinde `⚠ kronoloji notu` ile açıklanır (bilinçli sapma mı, hata mı?).

## 8. Dil ve üslup (hikâye metni için ön ilkeler)

- Anlatı dili çağdaş Türkçe; diyaloglarda dönem rengi **hitap ve unvanlarla** verilir (*Sultanım, devletlü, Çelebi, Paşa hazretleri, lala, ağa, kadı efendi, bey*), uydurma "eski Türkçe" taklidi yapılmaz.
- Şehzadeler 15. yüzyılın ilk yarısında **"Çelebi"** (Mehmed Çelebi, Alâeddin Ali Çelebi); Fâtih'ten itibaren **"Sultan"** (Sultan Cem, Sultan Korkud, Sultan Bayezid) olarak anılır. **Berkay için istisna (yazar kararı, 15 Ekim 2026; lâkap düzeltmesi aynı gün): "Çelebi" ve "Bahadır" hiç kullanılmaz.** 1444–1451 "Şehzade Berkay"; tek lâkabı **"Şâh-küş Şehzâde"** (uzun biçimi resmî yazıda: *"Yek tîr ile taht-ı Engürüs'ü bî-şâh koyan Şehzâde-i Şâh-küş Berkay bin Murad Han — tâle bekāhu"*); **"kral vuran!"** yalnız Varna nârası ve Koca Hızır'ın ağzında, küçük harfle kalır. 1451 sonrası "Sultan Berkay", 1453 sonrası "Fâtih Sultan Berkay Han" / "Ebü'l-Feth". (Defterde ve bölüm metinlerinde "Şehzâde" imlâsı.) (Bk. `kaynaklar/05-kurumlar/sehzadelik-sistemi.md`.)
- Yer adları dönem biçimiyle: Kostantiniyye/İstanbul (1453 sonrası ikisi de), Edirne, Burusa/Bursa, Mağnisa/Manisa, Amasya, Selânik, Üsküb, Semendire, Belgrad, Eğriboz, İnebahtı, Mora, Eflak, Boğdan, Erdel, Engürüs (Macaristan), Frengistan.

## 9. Kişi kuralı — kurgu kişi / tarihî kişi (yazar kararı, 15 Ekim 2026)

- **Kurgusal kişi yalnız şunlardır:** Berkay, **Meryem Hatun**, **Meryem'in ailesi** (Yörgüç Paşa ve konağı), **Orhan**, **Alâeddin Ali**. Bunların dışında **hiçbir uydurma ad kullanılmaz**: her kişi ya **gerçek tarihî bir kişi**dir, ya da **adsızdır** ("sancağın kadısı", "Erdelli bir akıncı").
- **Berkay'ın câriyesi yoktur; eşi yalnız Meryem Hatun'dur.** İki oğlu (Orhan, Alâeddin Ali) da Meryem'dendir. **Berkay'ın kız çocuğu yazılmaz;** 1474 Akkoyunlu düğünü gerçek tarihteki gibidir: **Mehmed'in kızı Gevherhan** Uğurlu Mehmed Mirza'ya verilir. Orhan'ın tek oğlu Selim'dir (annesi Dulkadırlı Ayşe).
- Gerçek kişilerin hikâyedeki **kurgusal** eylem ve sözleri dosya içinde **⚙** ile, gerçek tarihten alınanlar `[K]`/`[M]`/`[T]`/`[R]` ile işaretlenir; ayrıca ilgili yıl dosyasının "⚑ Çatal ve kâtip notları" tablosunda gösterilir.
- **Kurgusal adların gerçek karşılıkları** (eski adlar bütün dosyalardan silinmiştir):

| Eski (kurgu) | Yeni (gerçek) | Rol |
|---|---|---|
| Kâtip Sinan bin Abdullah | **Tursun Bey** (Tûr-ı Sînâ; Bursalı; Cebe Ali Bey'in yeğeni; d. ~1426) | 1444'te Saruhan kâtibi (18 yaşında); nüshayı 1459'da Göynük'te temize çeker; rüyayı 1459'da öğrenir; *Târîh-i Ebü'l-Feth*'i yazar; sonra defterdar |
| Silâhdar Yunus Ağa | **Has Yunus Bey** | Silâhdar; 1456 kapudan (Enez–Limni); ⚙ 17 Haz 1462 gecesi Lala'yla düşer |
| Hazinedar Hamza Ağa | **Hamza Bey** | Hazinedar (1444); Berkay'ın Amasya lalası (1446–51 ⚙); 20 Nis 1453 Baltaoğlu yerine kapudan; Niğbolu; Şub 1462'de Vlad kazığa vurur |
| Şövalye Pedri | **Vlad Țepeş (Kazıklı Voyvoda)** | Lala'yı 17 Haz 1462'de o öldürür; ⚙ 31 Ara 1476 Salı (14 Ramazan 881) Bükreş yakınında akıncılar önüne sürer, Berkay kendi eliyle öldürür |
| Hüma Sultan (Berkay'ın kızı) | **Gevherhan** (Mehmed'in gerçek kızı) | 1474 Uğurlu Mehmed Mirza düğünü gerçek tarihin kendisidir |

- **Epigraf (ebced):** *"Bir ok u bir kral"* — **بر اوق و بر قرال** = **848**. Kâtip Tursun'un defterinin başına ve yıl dosyalarının açılışına bu ebced yazılır. (Hesap: 2+200+1+6+100+6+2+200+100+200+1+30 = 848.)

## 10. El yazması düzeni ve üç kalıp

- El yazması sırası `hikaye/03-el-yazmasi-sirasi.md`'de tutulur: **epigraf (848) → 1444 → "Kâtip Tursun'un Defteri" → 1445…1520 → hâtime (30 Eylül 1520, Alâeddin Ali'nin defteri) → ekler.**
- **Üç kalıp:** *tam bölüm* · *kısa bölüm* · *defter yaprağı* (400–900 kelime). Defter yaprağı yılları: 1447, 1454–55, 1457–58, 1460, 1465–67, 1469, 1471–72, 1477, 1483, 1486, 1488, 1490–91, 1493, 1496–98, 1501–02, 1504–08. Kalıp, `hikaye/02-bolum-plani.md` tablosunun son sütununda yazılıdır.
