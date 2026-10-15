# Kaynak–kurgu ayrımı: ikinci grup ve birleşik teslim

**Tarih:** 15 Ekim 2026 · **Kapsam:** Kullanıcının onayladığı beş kronoloji ve iki hanedan dosyası; ilk dört dosyayla aynı PR #13 altında teslim. Bu rapor bütün projenin bittiği veya tarihî incelemelerin kapandığı anlamına gelmez.

## 1. İşlenen yedi dosya

| Kaynak | Ayrılan içerik |
|---|---|
| `kaynaklar/01-kronoloji/00-genel-zaman-cizelgesi-1444-1520.md` | Son yaş/olay tablosu, kurgu hayat tarihleri ve üç eski çalışma notu |
| `kaynaklar/01-kronoloji/01-ii-murad-ikinci-saltanat-1444-1451.md` | Kancalar, Buçuktepe için hikâyede kullanılan özel gün aralığı |
| `kaynaklar/01-kronoloji/02-fatih-donemi-1451-1481.md` | Alternatif hükümdar/ölüm/görev uygulamaları; satır içi notlar ve §13 |
| `kaynaklar/01-kronoloji/03-ii-bayezid-donemi-1481-1512.md` | Alternatif veraset ve İtalya seyri; kancalar ve §10 |
| `kaynaklar/01-kronoloji/04-yavuz-selim-donemi-1512-1520.md` | Alternatif soy ve kapanış; kancalar ve §12 |
| `kaynaklar/03-kisiler/hanedan-ii-murad-ailesi.md` | Eklenen oğul ve kurgu akrabalık/mezarlık bağlantıları |
| `kaynaklar/03-kisiler/hanedan-1451-1520.md` | Kurgu bağlantıları ve §4'teki karışık kuşak/yaş tablosu |

Tarihî olaylar, gerçek aile tabloları, vezîriâzam listeleri ve açık sorular kaynaklarda kaldı. Genel çizelgenin Ahmed kaydındaki Ali Bey = Evrenosoğlu kesinliği de `[?]` yapıldı; bu özdeşlik doğrulanmadı. Yaş tabloları yeniden hesaplanmadı; yeni yazar kararı üretilmedi.

## 2. Kayıpsızlık ve erişim

- Yedi dosyanın **22c2ef0** commit'indeki tam eski baytları `hikaye/notlar/kaynaktan-ayrilan/` altında korunuyor. Tam commit, kaynak yolu ve SHA-256 değerleri `kaynak-ayirma-kaydi.json` içinde. Manifest artık **11 kayıt** içeriyor.
- İlk dört kaydın başlangıç commit'i, özetleri ve arşivleri değiştirilmedi. İlk grup raporu `2026-10-15-kaynak-ayirma-1.md` tarihî teslim olarak korunur.
- Değişen her dolu satır ayrıca özgün satır aralığıyla alıntılandı. Okuma haritası: `../hikaye/notlar/kronoloji-hanedan-uygulamalari/README.md`. Bu döküm ve tam arşiv, güncel kurgu anayasası değildir; eskimiş cümlelerin taşınması onay sayılmaz.
- Eski numaralı ayrılmış bölümlerde yer tutucu/yönlendirme bırakıldı; sonraki tarihî bölümler yeniden numaralanmadı. README ve INDEX'teki eski §13/yaş tablosu tanımları güncellendi. Yıl dosyalarının tarihî bölüm atıfları korunuyor.

## 3. Özellikle korunan bağlam

- 1457 sünnet satırındaki kurgu açıklamasından **sonra** gelen Papalık donanması ve Albulena kayıtları kesilmedi.
- 1456 Belgrad sonrası tayinler, 1492 diplomatik/göç kayıtları, 1517 İskenderiye/Haremeyn ve 1520 ölüm haberi–cenaze devamları korundu.
- Bellini'nin **Meryem resmi**, kurgu Meryem Hatun değildir. Tarihî dinî tasvir ifadesi yerinde kaldı. Denetleyici yalnız açık “Papa'nın mektubu, Bellini'nin Meryem resmi” bağlamını istisna tutar; diğer Meryem kullanımları ve kurgu işaretleri hâlâ yakalanır.
- Eski “gerçek: Ali Bey...” gibi ifadeler yeni bir doğrulama değildir. Eski 1481 linç/yer cümlesi ve eşleme öncesi “kâtip Sinan” kaydı çalışma notlarının uyarılarında ayrıca sınırlandı.

## 4. Kontroller

- `python3 -m unittest discover -s tests -v`: **17 test başarılı**. On bir nüshanın SHA-256 kontrolü; Git nesnesi varsa bayt karşılaştırması; ilk dört özetin sabitliği; değişen satırların köken dökümü; tarihî bölüm/satır devamlarının korunması; Meryem bağlamı ve eksik not dosyasının engellenmesi sınanıyor.
- `git diff --check`: temiz.
- Yazar defteri koruma özeti değişmedi. `karakter/sehzade-berkay-ahval-defteri.md`, Zeyl/§XX ve sekiz mevcut yıl dosyası bu grupta değiştirilmedi.
- Genel denetim: **3 açık kalıp engeli + 24 elle inceleme kaydı**. Önceki 30 aday dosyanın yedisi ayrıldı. Ortak taramaya 🎭 işareti de eklendiği için katalog dosyası bir ek inceleme adayı oldu: **30 − 7 + 1 = 24**. Bu sayılar doğrulanmış tarihî hata sayısı değildir.
- `--strict`: **exit 1 beklenir**. 1448 (448/900 alt sınır), 1449 (424/900), 1450 (628/2000) uzunluk açıkları sürüyor. Eşik düşürülmedi, sahne veya yeni olay eklenmedi. Bu engeller kaynak ayırma kaybı değildir; birleşme onları kapatmaz.

## 5. Açık kalan işler

1. `uc-kisi-kaynak-incelemesi.md` içindeki Evrenosoğlu Ali Bey, Hamza Bey ve Has Yunus Bey iddialarının doğrudan dış kaynak/neşir karşılaştırması. Bu grupta dış araştırma yapılmadı.
2. Arşivin kalan yer, kurum, günlük hayat ve birincil kaynak dosyalarının ayrılması; D21 arşiv geneli için açık.
3. Tarihî derlemeler arasındaki tarih/yaş uyumsuzluklarının atıfla çözülmesi. Örneğin genel çizelge–dönem dosyalarındaki Bayezid'in 1512 ölüm günü farkı ve Selim'in ölümünde 50 / tamamlanmış 49 yaş ayrımı burada doğrulanmış veya kapanmış sayılmaz.
4. 1444'ten itibaren olay günü yaşı, yol süresi, bilginin kaynağı ve anlatıcı bakışı incelemesi; ardından yazarla sırayla mevcut yılların gözden geçirilmesi. 1447–1451 taslakları onaylı yıl sayılmaz.

**Birleştirme sınırı:** Kullanıcı iki ayırma grubunun birleştirilmesine izin verdi. PR #13'ün birleşmesi bu dosya düzenini teslim eder; tarihî belirsizlikleri, kâtip önerilerini veya onaysız yıl metinlerini onaylamaz.
