# Çalışma Kılavuzu

Bu dosya, repodaki bütün metinlerin uyması gereken kuralları toplar. Kısa tutulmuştur; şüphede kalınan her durumda buraya eklenir.

## 1. Dosya ve klasör adları

- Dosya adları **ASCII** (Türkçe karakter yok), küçük harf, tire ile: `01-ii-murad-ikinci-saltanat-1444-1451.md`.
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

**🎭 kancaları yalnız `hikaye/` veya `karakter/` altında tutulur.** `kaynaklar/` tarihî olgu, kaynak künyesi ve belirsizlik etiketlerini barındırır; kurgu kişi, alternatif olay/soy/görev ve sahne önerisi burada tutulmaz. Eski kaynak dosyalarındaki 🎭/⚙ notları izinli yeni kayıt değil, kayıpsız ayrılacak eski çalışma borcudur. Salt bir işaret taraması tarihî hata kanıtı değildir. Ayırma bağlantıları ve dizinlerdeki açıklayıcı yönlendirmeler kurgu biyografisi sayılmaz. Kancanın taşınması yazar onayı anlamına gelmez; §7 ve §12 birlikte uygulanır.

## 7. Kurgu / tarih ayrımı

- `kaynaklar/` altında **asla** kurgusal karakter yer almaz (Berkay dahil).
- `karakter/` ve `hikaye/` altındaki dosyalar tarihî kişileri kullanabilir; fakat tarihî kişiye atfedilen **kurgusal** söz ve eylemler, gerçek kayıtlarla açıkça çelişiyorsa dosya içinde `⚠ kronoloji notu` ile açıklanır (bilinçli sapma mı, hata mı?).

## 8. Dil ve üslup (hikâye metni için ön ilkeler)

- Anlatı dili çağdaş Türkçe; diyaloglarda dönem rengi **hitap ve unvanlarla** verilir (*Sultanım, devletlü, Çelebi, Paşa hazretleri, lala, ağa, kadı efendi, bey*), uydurma "eski Türkçe" taklidi yapılmaz.
- Şehzadeler 15. yüzyılın ilk yarısında **"Çelebi"** (Mehmed Çelebi, Alâeddin Ali Çelebi); Fâtih'ten itibaren **"Sultan"** (Sultan Cem, Sultan Korkud, Sultan Bayezid) olarak anılır. **Berkay için istisna (yazar kararı, 15 Ekim 2026; lâkap düzeltmesi aynı gün): "Çelebi" ve "Bahadır" hiç kullanılmaz.** 1444–1451 "Şehzade Berkay"; tek lâkabı **"Şâh-küş Şehzâde"** (uzun biçimi resmî yazıda: *"Yek tîr ile taht-ı Engürüs'ü bî-şâh koyan Şehzâde-i Şâh-küş Berkay bin Murad Han — tâle bekāhu"*); **"kral vuran!"** yalnız Varna nârası ve Koca Hızır'ın ağzında, küçük harfle kalır. 1451 sonrası "Sultan Berkay", 1453 sonrası "Fâtih Sultan Berkay Han" / "Ebü'l-Feth". (Defterde ve bölüm metinlerinde "Şehzâde" imlâsı.) (Bk. `kaynaklar/05-kurumlar/sehzadelik-sistemi.md`.)
- Yer adları dönem biçimiyle: Kostantiniyye/İstanbul (1453 sonrası ikisi de), Edirne, Burusa/Bursa, Mağnisa/Manisa, Amasya, Selânik, Üsküb, Semendire, Belgrad, Eğriboz, İnebahtı, Mora, Eflak, Boğdan, Erdel, Engürüs (Macaristan), Frengistan.

## 9. Kişi kuralı — kurgu kişi / tarihî kişi (yazar kararı, 15 Ekim 2026)

- **Kurgusal kişi yalnız şunlardır:** Berkay, **Meryem Hatun**, **Meryem'in ailesi** (Yörgüç Paşa tarihî kişidir; Meryem'in ona bağlanan aile ilişkisi kurgudur), **Orhan**, **Alâeddin Ali**. Bunların dışında **hiçbir uydurma ad kullanılmaz**: her kişi ya **gerçek tarihî bir kişi**dir, ya da **adsızdır** ("sancağın kadısı", "Erdelli bir akıncı").
- **Berkay'ın câriyesi yoktur; eşi yalnız Meryem Hatun'dur.** İki oğlu (Orhan, Alâeddin Ali) da Meryem'dendir. **Berkay'ın kız çocuğu yazılmaz;** 1474 Akkoyunlu düğünü gerçek tarihteki gibidir: **Mehmed'in kızı Gevherhan** Uğurlu Mehmed Mirza'ya verilir. Orhan'ın tek oğlu Selim'dir (annesi Dulkadırlı Ayşe).
- Gerçek kişilerin hikâyedeki **kurgusal** eylem ve sözleri dosya içinde **⚙** ile, gerçek tarihten alınanlar `[K]`/`[M]`/`[T]`/`[R]` ile işaretlenir; ayrıca ilgili yıl dosyasının "⚑ Çatal ve kâtip notları" tablosunda gösterilir.
- **Kişi eşlemeleri** (hikâye tercihleri ile tarihî özdeşlik ayrı tutulur; eski adların arşiv genelinde bütünüyle silindiği ileri sürülmez). Tarihî dayanaklar: `denetim/2026-10-15-dogrudan-kaynak-kontrolu.md`; doğrulama fişi: `denetim/uc-kisi-kaynak-incelemesi.md`.

| Eski (kurgu) | Yeni (gerçek) | Rol |
|---|---|---|
| Kâtip Sinan bin Abdullah | **Tursun Bey** (Tûr-ı Sînâ; Bursalı; Cebe Ali Bey'in yeğeni; d. ~1426) | 1444'te Saruhan kâtibi (18 yaşında); nüshayı 1459'da Göynük'te temize çeker; rüyayı 1459'da öğrenir; *Târîh-i Ebü'l-Feth*'i yazar; sonra defterdar |
| Silâhdar Yunus Ağa | **Has Yunus Bey** | ⚙ Silâhdar ve hikâyede 1456 kapudan; tarihî göreve geliş DİA’da 1455 yazı. ⚙ 17 Haz 1462 ölümü alternatif kaderdir; tarihî idamı DİA’da 1456 kışı sonrası ihtimalli verilir |
| Hazinedar Hamza Ağa | **Hamza Bey** | ⚙ Hazinedar (1444) ve Amasya lalası (1446–51). Hikâyenin 20 Nis 1453 kapudanlık / Şub 1462 ölüm tercihleri korunur; tarihî tayin günü, ay ve Biçeroğlu ile özdeşlik `[?]`. DİA’da 1462 elçi ölümü için doğrudan dayanak bulundu; bütün roller aynı kişiye mal edilmez |
| Şövalye Pedri | **Vlad Țepeş (Kazıklı Voyvoda)** | Lala'yı 17 Haz 1462'de o öldürür; ⚙ 31 Ara 1476 Salı (14 Ramazan 881) Bükreş yakınında akıncılar önüne sürer, Berkay kendi eliyle öldürür |
| Hüma Sultan (Berkay'ın kızı) | **Gevherhan** (Mehmed'in gerçek kızı) | Evlilik modern kaynaklarda destekleniyor; 1474 yılı Parlaz’ın makalesinde açıkça geçiyor `[M]`. Bu, çoklu çağdaş kaynak denetimi tamamlandı demek değildir |

- **Epigraf (ebced):** *"Bir ok u bir kral"* — **بر اوق و بر قرال** = **848**. Kâtip Tursun'un defterinin başına ve yıl dosyalarının açılışına bu ebced yazılır. (Hesap: 2+200+1+6+100+6+2+200+100+200+1+30 = 848.)

## 10. El yazması düzeni ve üç kalıp

- El yazması sırası `hikaye/03-el-yazmasi-sirasi.md`'de tutulur: **epigraf (848) → 1444 → "Kâtip Tursun'un Defteri" → 1445…1520 → hâtime (30 Eylül 1520, Alâeddin Ali'nin defteri) → ekler.**
- **Üç kalıp:** *tam bölüm* · *kısa bölüm* · *defter yaprağı* (400–900 kelime). Defter yaprağı yılları: 1447, 1454–55, 1457–58, 1460, 1465–67, 1469, 1471–72, 1477, 1483, 1486, 1488, 1490–91, 1493, 1496–98, 1501–02, 1504–08. Kalıp, `hikaye/02-bolum-plani.md` tablosunun son sütununda yazılıdır.

## 11. Denetim kapısı — yazar düzeltmesinden sonra

- **Kurtçu Doğan'ın bağlayıcı seyri:** ağalıktan alınma → düşkünlük → Akşemseddin'e sığınma ve günahlarını anlama → daha sonra Fâtih Sultan Berkay Han'ın affı → Berkay'ın adamı olma. **Devşirme Kurtçu Doğan akıncı veya akıncı beyi yapılmaz; Evrenosoğlu Ali Bey'in ucuna tayin edilmez.** Affın tarihi ve sonraki resmî görevi belirlenmedi; kâtip bunları kendiliğinden doldurmaz. Bu, yazarın proje kararıdır; kaynaklarda belgeli bir biyografi gibi sunulmaz.
- **Görev denetimi:** kişinin kökeni, kapıkulu/ocak/serhat mensubiyeti, görev sırası ve bağlı olduğu makam kontrol edilmeden yeni tayin yazılmaz. İki askerî görevin ikisi de atlı diye birbirinin yerine geçirilemez. Doğrulanmayan kurum tarihi `[?]` olarak araştırmaya ayrılır.
- **Karar yetkisi:** ✔ yalnız açık yazar kararıdır; kâtip önerileri ⚙ olarak kalır. Teknik işleri yürütme izni, ölüm yılı veya yeni kurgu kaderi için verilmiş özel onay diye kaydedilemez. 1527, Alâeddin Ali için kabul edilmiş ölüm yılı değildir.
- **Yıl sırası:** önceki yılın yazar onayı alınmadan sonraki yıl yazılmaz. 1448–1451 dosyalarının bulunması onları onaylı yapmaz; önceki kâtip ilerleyişi onay zincirini atlamıştır. Yeni yıl üretimi denetim boyunca durdurulur.
- **Tarih ve kurgu:** `[K]`, `[M]`, `[T]`, `[R]`, `[?]` tarihî iddianın kanıt durumudur. Uydurulmuş bir konuşma, hava, özel buluşma veya sahne eylemi `[T]` değil **⚙** olur. ✔ yazar kararı da gerçek tarih kanıtı değildir.
- **Tamamlanma ölçütü:** kelime sayısında yalnız sahne metni sayılır; künye, kaynakça ve ⚑ tablosu sayılmaz. Sayısal sınırı geçmek tarihî doğruluk veya yazar onayı yerine geçmez.
- **Teslim öncesi:** kararın kaynağı → ilgili bütün kayıtlar → yaş/menzil/takvim → kurum ve görev → anlatıcı bilgisi → kaynak/kurgu ayrımı → kalıp denetimi. Açık bulgular raporlanmadan “tamamlandı/temiz” denmez. Betik tarih uzmanının ve yazarın yerini tutmaz.

## 12. Kaynak ayırma kayıtları

- Temizlenen kaynak metninin önceki karışık nüshası `hikaye/notlar/kaynaktan-ayrilan/` altında köken yolu, başlangıç commit’i ve SHA-256 ile saklanır. Aktarım listesi `denetim/kaynak-ayirma-kaydi.json` içindedir.
- Bu salt kayıt nüshaları güncel karar veya tarihî kaynak değildir. İçlerindeki eski adlar ve hatalar yalnız aktarımın izini korur; yeni sahneye dayanak yapılmaz, toplu ad değiştirmeyle düzeltilmez. Güncel kararlar ana hat/kişi dosyalarında tutulur.
- Kaynak ayırmak ile tarihî iddiayı doğrulamak ayrı işlerdir. Bir kurgu sütununun taşınması kalan `[K]` etiketlerini kendiliğinden doğrulamaz. Görülmeyen kaynağa sayfa/alıntı/erişim tarihi eklenmez.

## 13. Otomatik denetimin sınırları ve kayıt nüshaları

- Denetleyici metin/atıf/künye/kalıp kontrolleri yapar; testlerin geçmesi tarihî doğruluk, gözlemsel hilal veya yazar onayı değildir. Tanıdığı açık tarih biçimlerinde Jülyen hafta gününü hesaplayabilir; örtük/rivayet tarihlerini ve bütün yaş ifadelerini kendiliğinden çözmez.
- Kayıpsız arşiv ve aktarılan alıntı dökümleri etkin kaynak listesinden ayrıdır. Yeni yıl dosyasında bunlara dayanak atfı verilmez; eski hatalı adlar denetimden “silmek” için nüshalar değiştirilmez.
- Kelime kalıbı yalnız sahne dosyalarına uygulanır; araştırma notuna roman kalıbı dayatılmaz. 77 yıllık plandaki boş/uyumsuz kalıplar ayrıca raporlanır. Kalıbı seçmek yılı onaylamak değildir.
