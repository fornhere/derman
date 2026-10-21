<div align="center">

# Derman

**Derdini anlat, ona iyi gelecek düşünürle konuş.**

Seneca'dan Kafka'ya, Laozi'den Maya Angelou'ya 35 düşünür ve fikir önderiyle Türkçe sohbet eden bir Claude skill'i.

[![Lisans: MIT](https://img.shields.io/badge/lisans-MIT-blue.svg)](LICENSE)
![Dil: Türkçe](https://img.shields.io/badge/dil-T%C3%BCrk%C3%A7e-red.svg)
![Persona: 35](https://img.shields.io/badge/persona-35-8a2be2.svg)
![Claude Skill](https://img.shields.io/badge/Claude-Skill-d97757.svg)

</div>

---

## Nasıl çalışır

1. **Derdini yaz.** İşte tükenmişlik, bir ayrılık, karar verememe, üretememe, yalnızlık... Ne varsa.
2. **Üç öneri al.** Derman derdini temalara ayırır ve sana farklı dönemlerden, derde farklı kapılardan giren üç kişi önerir.
3. **Birini seç, konuş.** Seçtiğin kişi, kaynaklı fikirleri ve tanınabilir üslubuyla seninle derdin üzerine konuşur; her yanıt bir soru ya da bugün atılabilecek küçük bir adımla biter.

### Kısa bir örnek

> **Sen:** Birkaç aydır sabahları kalkarken midem düğümleniyor. Hep "şu lansman bitsin, sonra nefes alırım" diyorum ama biri bitmeden öbürü başlıyor. Galiba tükendim.
>
> **Derman:** Bu konuda konuşabileceğin üç kişi:
> 1. **Karl Marx**: yabancılaşma fikriyle, yorgunluğunu yalnızca kendi dayanıksızlığın gibi görmeni engeller.
> 2. **Franz Kafka**: üzerindeki beklentileri tek tek görünür kılar.
> 3. **Seneca**: hep sonraya ertelediğin hayatının hesabını seninle birlikte tutar.
>
> **Sen:** 3, Seneca.
>
> **Seneca (canlandırma):** Dostum, satırlarını bir hasta yatağının başında oturur gibi okudum. Yalnız baştan söyleyeyim: sana yukarıdan reçete yazan bir hekim değilim; aynı hastalıktan hâlâ iyileşmeye çalışan bir hastayım. Önce teşhisi koyalım: hastalığın adı yalnızca yorgunluk değil, ödünç verilmiş bir hayat...

Konuşmaların tamamı: [`derman/ornekler/`](derman/ornekler/) (tükenmişlik, kriz anında personadan çıkış, yaşayan bir kişiyle konuşma).

## Kimlerle konuşabilirsin

| Dönem | Kişiler | Özellikle iyi geldiği dertler |
|---|---|---|
| **Antik Yunan ve Roma** | Sokrates, Platon, Aristoteles, Epikuros, Epiktetos, Seneca, Marcus Aurelius | karar, kaygı, öfke, tükenmişlik, ölüm ve sonluluk, disiplin |
| **Antik Çin** | Konfüçyüs, Laozi, Zhuangzi | aile, kıyaslama, kayıp, zorlamayı bırakmak |
| **Aydınlanma ve modern felsefe** | Spinoza, Hume, Kant, Kierkegaard, Nietzsche, Beauvoir, Camus | ahlak ve vicdan, ikilem, anlam arayışı, özgürlük, kimlik |
| **Siyaset ve toplum** | Wollstonecraft, Mill, Marx, Arendt, Du Bois, Gandhi, Martin Luther King Jr. | haksızlık, ayrımcılık, baskı, iş ve yabancılaşma |
| **Edebiyat, şiir ve sanat** | Tolstoy, Rilke, Kafka, Woolf, Baldwin, Maya Angelou, Frida Kahlo | yaratıcı tıkanma, yalnızlık, aile, beden ve kimlik |
| **Çağdaş** | Steve Jobs, Paul Graham\*, Sara Blakely\*, Kanye West\* | kariyer, girişim ve risk, erteleme, başarısızlık |

\* Yaşayan kişi. Bu personalar her konuşmaya kısa bir çerçeve notuyla başlar (aşağıya bak).

Listede olmayan birini istersen Derman bunu açıkça söyler ve en yakın üç kişiyi önerir; kartı olmayan kimseyi canlandırmaz.

## Kurulum

### Claude.ai ve Claude masaüstü

1. [Releases](../../releases/latest) sayfasından `derman.zip` dosyasını indir.
2. Claude'da **Settings → Capabilities** altından *Code execution and file creation* özelliğinin açık olduğundan emin ol.
3. **Customize → Skills → Upload skill** ile ZIP'i yükle.
4. Yeni bir sohbette derdini yazman yeter; örneğin *"Bir karar veremiyorum, bir düşünürle konuşmak istiyorum."*

### Claude Code

```bash
git clone https://github.com/fornhere/derman.git
```

```bash
cp -r derman/derman ~/.claude/skills/derman
```

## Önemli notlar

> [!IMPORTANT]
> **Derman terapi değildir.** Bir ruh sağlığı uzmanının, hekimin, avukatın ya da finans danışmanının yerini tutmaz. Tıbbi, hukuki ve mali konularda yalnızca genel bir düşünme ortaklığı yapar ve seni bir uzmana yönlendirir.

> [!WARNING]
> **Kriz anında:** Kendine ya da başkasına zarar verme düşüncesi, şiddet ya da tıbbi acil durum fark edildiğinde persona hemen bırakılır ve normal bir destek yanıtına geçilir. Türkiye'deysen **112**'yi ara; başka bir ülkedeysen oradaki acil numarayı ara ya da güvendiğin biriyle konuş.

- **Bunlar canlandırmadır.** Konuştuğun kişi, kamuya açık eser ve fikirlerden yola çıkan bir yapay zekâ canlandırmasıdır; kişinin kendisi değildir, onu temsil etmez ve onun onayını taşımaz. Sorduğunda bunu açıkça söyler.
- **Alıntı yoktur.** Personalar birebir söz aktarmaz, kendi cümleleriyle parafraz yapar. "Bunu gerçekten söyledi mi?" diye sorarsan dürüst cevap alırsın ve kaynağa yönlendirilirsin.
- **Yaşayan kişiler** her konuşmaya bir çerçeve notuyla başlar. Bu personalar kişi adına yeni görüş, güncel olay yorumu ya da ürün veya kişi onayı üretmez; özel hayatları hakkında tahmin yürütmez.
- Kişilerin bugün ayrımcı sayılan tarihsel görüşleri öğüt olarak tekrar edilmez.
- **18 yaş ve üstü** kullanıcılar için tasarlanmıştır.
- Derman hiçbir kişi, kurum ya da mirasla bağlantılı değildir ve onlar tarafından onaylanmamıştır. Adı geçen markalar ve isimler sahiplerine aittir.
- Derman bağımsız bir topluluk projesidir; Anthropic ile bağlantılı ya da resmî değildir. Claude, Anthropic'in markasıdır.
- Kartı bulunan bir kişi ya da temsilcisiysen ve kartın değiştirilmesini veya kaldırılmasını istiyorsan bir issue aç; kart incelenip düzeltilir ya da kaldırılır.

## Nasıl yapıldı

Her persona bir **kart** dosyasıdır: kim olduğu, ana fikirleri ve kaynakları, konuşma üslubu, onu tanınır kılan ayırt edici işaretler, hangi dertlere iyi geldiği, kaçınılacaklar ve kaynakça. Fikirler Stanford Encyclopedia of Philosophy gibi kaynaklara dayanır; üslup tarifleri bir tasarım yorumudur, tarihsel bir konuşma kaydı değildir.

Geliştirme sırasında kartlar ad gizlenerek bir kör tanıma denemesinden geçirildi ve personalar üsluplarından ayırt edilebildi. Bu bir iç deneme; depoda yeniden üretilebilir bir test olarak yer almıyor.

```
derman/
├── SKILL.md                     # akış, güvenlik ve sohbet kuralları
├── references/
│   ├── guvenlik.md              # kriz protokolü ve sınırlar
│   ├── eslestirme.md            # 21 dert etiketi → kişi eşleşmeleri
│   └── personalar/*.md          # 35 kişi kartı
└── ornekler/                    # örnek konuşmalar
```

## Katkı

Yeni bir kişi eklemek ya da bir kartı düzeltmek istersen:

1. Mevcut bir kartı (ör. [`seneca.md`](derman/references/personalar/seneca.md)) şablon olarak kopyala; bütün bölümleri doldur ve her ana fikre güvenilir bir kaynak bağla.
2. Kişiyi [`eslestirme.md`](derman/references/eslestirme.md) içindeki uygun etiketlere ve [`SKILL.md`](derman/SKILL.md) içindeki kişi listesine ekle.
3. Yaşayan bir kişiyse karta çerçeve notunu ekle.
4. Pull request aç.

Bir kişi hakkında yanlış bilgi ya da kırılmış bir kaynak bağlantısı görürsen bir issue açman yeterli.

## Lisans

Kod ve kart metinleri [MIT](LICENSE) lisanslıdır. Lisans; kişi adlarını, markaları ve bağlantı verilen dış kaynakları kapsamaz.

---

<details>
<summary><b>English summary</b></summary>

**Derman** ("remedy" in Turkish) is a Claude skill that listens to what's troubling you, suggests three fitting thinkers out of 35 (Seneca, Kafka, Laozi, Arendt, Maya Angelou, Steve Jobs and more), and then role-plays the one you choose, drawing on their sourced ideas and recognisable voice, in Turkish.

It is **not therapy**. On any crisis signal it drops the persona immediately and points to emergency help. All personas are AI portrayals inspired by public works, not the people themselves, and are not affiliated with or endorsed by them or their estates. For adults (18+). Not affiliated with Anthropic. Living people are portrayed with an explicit framing note and no new opinions or endorsements are generated in their name. No verbatim quotes are used.

Install: download `derman.zip` from Releases and upload it via **Customize → Skills** in Claude, or copy the `derman/` folder into `~/.claude/skills/` for Claude Code. MIT licensed.

</details>
