# Eşleştirme dizini

Bu dosya `araclar/eslestirme_uret.py` ile kartlardan üretilir; elle düzenleme.

## Etiket sözlüğü

Derdi en çok anlatan etiket birincildir; en çok iki ikincil eklenir. İfadeler örnektir: kullanıcı başka sözlerle de aynı şeyi anlatabilir. Kriz sinyali içeren ifadeler bu sözlükte yer almaz; onlar için önce `references/guvenlik.md` uygulanır.

| Etiket | Ne demek | Kullanıcı şöyle diyebilir |
|---|---|---|
| `anlam-amac` | Yaptıklarının ya da hayatın anlamını sorgulama, yön kaybı, içi boş bir düzen. | "Ne için uğraşıyorum ki?" · "Her şey yolunda ama içim boş" · "Hayatımın bir yönü yok" |
| `kaygi-belirsizlik` | Gelecek ya da bilinmeyen bir şey hakkında süren endişe, kafada dönen olasılıklar. | "İçim rahat değil" · "Ya olmazsa?" · "Hep en kötüsünü düşünüyorum" |
| `kayip-yas` | Birinin ölümü ya da hayatındaki önemli bir şeyin kaybından sonra yaşanan acı ve yas. | "Babamı kaybettim" · "Onsuz nasıl devam edeceğim bilmiyorum" · "Hâlâ yasını tutuyorum" |
| `ask-iliski` | Romantik ilişki, aşk, ayrılık, bağlanma ve partnerle yaşanan sorunlar. | "Ayrıldık, aklımdan çıkmıyor" · "Sevgilimle hep aynı yerde tıkanıyoruz" · "Karşılıksız seviyorum" |
| `aile` | Anne, baba, kardeş ve akrabalarla bağlar; aile beklentileri, görevler ve kırgınlıklar. | "Annemlerin beklentileri beni boğuyor" · "Babamla konuşamıyoruz" · "Evde hep fedakârlığı ben yapıyorum" |
| `yalnizlik` | Yalnız hissetme, bağ kuramama, anlaşılmama ya da bir yere ait olamama. | "Kimse beni anlamıyor" · "Kalabalıkta bile yalnızım" · "Konuşacak kimsem yok" |
| `kariyer-is` | Mevcut iş, meslek ve iş yeri: memnuniyetsizlik, takdir görmeme, meslek yönü. | "İşimden nefret ediyorum" · "Galiba yanlış meslekteyim" · "Terfi alamadım" |
| `yaraticilik-tikanma` | Yazı, müzik, resim, kod gibi yaratıcı bir işte üretememe, ilham kaybı. | "Hiçbir şey yazamıyorum" · "İlhamım kurudu" · "Ne yapsam kötü geliyor" |
| `erteleme-disiplin` | Erteleme, odaklanamama, alışkanlık kuramama; yapmak istediğine başlayamama. | "Hep son güne bırakıyorum" · "Bir türlü başlayamıyorum" · "Hiç zamanım yetmiyor" |
| `ozguven-kimlik` | Kendine güvenmeme, değersizlik hissi, kim olduğu sorusu, başkalarının tanımına göre yaşama. | "Kendime güvenmiyorum" · "Yeterince iyi değilim" · "Ben aslında kimim?" |
| `ofke-catisma` | Öfke, kavga, kin ve kırgınlık; biriyle süren çatışma. | "Çok sinirliyim" · "Ev arkadaşım beni deli ediyor" · "Kendimi tutamayıp bağırdım" |
| `adaletsizlik-ayrimcilik` | Haksızlığa uğrama; cinsiyet, köken, kimlik ya da konum yüzünden ayrımcılık ve eşitsizlik. | "Haksızlığa uğradım" · "Kadın olduğum için ciddiye alınmıyorum" · "Kimliğim yüzünden dışlanıyorum" |
| `ozgurluk-baski` | Baskı altında hissetme, sınırlanma, kendi hayatını yaşayamama; özgürlüğün sınırları. | "Kendi hayatımı yaşayamıyorum" · "Herkes bana ne yapacağımı söylüyor" · "Kafeste gibiyim" |
| `karar-ikilem` | Seçenekler ortadayken seçememe, iki yol arasında kalma, yanlış seçim korkusu. | "İki arada kaldım" · "Kalsam mı gitsem mi?" · "Hangisini seçeceğimi bilemiyorum" |
| `basarisizlik-red` | Başarısız olma, kaybetme, reddedilme ve bunun açtığı yara. | "Yine olmadı" · "Sınavı kazanamadım" · "Başvurum reddedildi" |
| `olum-sonluluk` | Kriz dışında ölümlülük, yaşlanma ve zamanın geçişi üzerine düşünme. | "Ölüm sık sık aklıma takılıyor" · "Zaman çok hızlı geçiyor" · "Otuzuma geldim, hiçbir şey yapmadım" |
| `kiskanclik-karsilastirma` | Başkasının başarısını ya da hayatını kıskanma, sürekli kıyaslama, geride kalma hissi. | "Herkes benden ileride" · "Arkadaşımın başarısını kıskanıyorum" · "Instagram'a bakınca kendimi kötü hissediyorum" |
| `tukenmislik` | Uzun süren bitkinlik, hiçbir şeye hevesin kalmaması, yükün altında ezilme. | "Tükendim" · "Hiçbir şeye hâlim yok" · "Sabah kalkacak gücüm yok" |
| `ahlak-vicdan` | Doğru mu yanlış mı sorusu, vicdan azabı, ilkeyle çıkar ya da kural arasında sıkışma. | "Bunu yapmak doğru mu?" · "Vicdanım rahat değil" · "Arkadaşımı ele versem mi?" |
| `girisim-risk` | Kendi işini kurma, güvenceyi bırakıp bir şeye atılma, risk alma korkusu. | "Kendi işimi kurmak istiyorum ama korkuyorum" · "Bir fikrim var, denesem mi?" · "Maaşlı işi bırakmak riskli geliyor" |
| `beden-imaj` | Görünüş, kilo, beden algısı; hastalık, yaşlanma ya da değişen bedenle ilişki. | "Aynaya bakmak istemiyorum" · "Kilom yüzünden kendimden utanıyorum" · "Bedenimi sevemiyorum" |

### Sık karışan etiketler

- `kayip-yas` mı `olum-sonluluk` mu: Somut bir kayıp ve yas varsa `kayip-yas` birincildir. Ölümlülük, yaşlanma ya da zamanın geçişi üzerine genel bir düşünceyse `olum-sonluluk`.
- `kaygi-belirsizlik` mi `karar-ikilem` mi: Seçenekler belli ve kişi seçemiyorsa `karar-ikilem`. Ne olacağının bilinmemesi kemiriyorsa `kaygi-belirsizlik`.
- `kariyer-is` mi `girisim-risk` mi: Mevcut iş ve meslek sorunu `kariyer-is`. Kendi işini kurmak, güvenceyi bırakıp bir şeye atılmak `girisim-risk`.
- `erteleme-disiplin`, `tukenmislik`, `yaraticilik-tikanma`: Gücü var ama başlayamıyorsa erteleme. Gücü kalmamışsa tükenmişlik. Sorun yaratıcı bir işte üretememekse yaratıcılık.
- `ozguven-kimlik` mi `beden-imaj` mı: Görünüş ya da beden merkezdeyse `beden-imaj` birincil, `ozguven-kimlik` ikincildir.
- `kiskanclik-karsilastirma` mı `ask-iliski` mi: Partnerle ilgili kıskançlıkta `ask-iliski` birincildir. Başkasının başarısı ya da hayatıyla kıyas `kiskanclik-karsilastirma`.
- `basarisizlik-red` ve `ask-iliski`: Romantik bir reddedilmede `ask-iliski` birincil, `basarisizlik-red` ikincildir.
- `ofke-catisma` mı `adaletsizlik-ayrimcilik` mı: Öfkenin kaynağı bir haksızlık ya da ayrımcılıksa `adaletsizlik-ayrimcilik` birincildir.
- `ozgurluk-baski` ve `aile`: Baskı aileden geliyorsa `aile` birincil, `ozgurluk-baski` ikincildir.
- `tukenmislik` haftalardır süren bir bitkinlikse öneriyle birlikte kısa bir profesyonel destek notu düş.

## Etiket → kişiler

**Doğrudan:** kişi bu konuyu bizzat ele almış. **Dolaylı:** kaynaklı fikirleri bu derde uygulanıyor. Önce doğrudan listeden seç; çeşitlilik için gerekirse dolaylıdan tamamla.

| Etiket | Doğrudan | Dolaylı |
|---|---|---|
| `anlam-amac` | aristoteles, beauvoir, camus, epiktetos, epikuros, gandhi, kafka, kant, kanye-west, kierkegaard, konfucyus, marcus-aurelius, martin-luther-king, marx, mill, nietzsche, paul-graham, platon, rilke, sara-blakely, seneca, sokrates, spinoza, steve-jobs, tolstoy, wollstonecraft, woolf, zhuangzi | arendt, baldwin, du-bois, frida-kahlo, hume, laozi, maya-angelou |
| `kaygi-belirsizlik` | aristoteles, baldwin, beauvoir, epiktetos, epikuros, frida-kahlo, hume, kafka, kierkegaard, marcus-aurelius, martin-luther-king, rilke, sara-blakely, seneca, spinoza, steve-jobs, tolstoy, woolf | arendt, camus, du-bois, gandhi, kant, konfucyus, laozi, marx, maya-angelou, mill, nietzsche, paul-graham, platon, sokrates, wollstonecraft, zhuangzi |
| `kayip-yas` | baldwin, beauvoir, du-bois, epiktetos, frida-kahlo, kanye-west, kierkegaard, konfucyus, maya-angelou, platon, rilke, seneca, steve-jobs, tolstoy, wollstonecraft, woolf, zhuangzi | arendt, aristoteles, camus, epikuros, hume, kafka, laozi, marcus-aurelius, nietzsche, sokrates, spinoza |
| `ask-iliski` | arendt, aristoteles, baldwin, beauvoir, du-bois, epiktetos, epikuros, frida-kahlo, gandhi, hume, kafka, kant, kanye-west, kierkegaard, marcus-aurelius, maya-angelou, mill, platon, rilke, sokrates, spinoza, steve-jobs, tolstoy, wollstonecraft, woolf | camus, konfucyus, laozi, martin-luther-king, marx, nietzsche, seneca, zhuangzi |
| `aile` | aristoteles, baldwin, beauvoir, camus, du-bois, epiktetos, epikuros, frida-kahlo, gandhi, kafka, kant, kanye-west, kierkegaard, konfucyus, marcus-aurelius, marx, maya-angelou, mill, platon, rilke, sara-blakely, seneca, steve-jobs, tolstoy, wollstonecraft, woolf | — |
| `yalnizlik` | arendt, aristoteles, baldwin, beauvoir, camus, epikuros, frida-kahlo, kafka, kant, konfucyus, maya-angelou, nietzsche, rilke, seneca, sokrates, tolstoy, wollstonecraft, woolf | du-bois, epiktetos, hume, kierkegaard, marcus-aurelius, martin-luther-king, marx, paul-graham, platon, spinoza |
| `kariyer-is` | arendt, baldwin, beauvoir, camus, du-bois, epiktetos, frida-kahlo, gandhi, hume, kafka, kanye-west, kierkegaard, konfucyus, laozi, marcus-aurelius, martin-luther-king, marx, maya-angelou, mill, paul-graham, rilke, sara-blakely, seneca, spinoza, steve-jobs, tolstoy, wollstonecraft, woolf, zhuangzi | aristoteles, epikuros, kant, nietzsche, platon, sokrates |
| `yaraticilik-tikanma` | baldwin, beauvoir, camus, du-bois, kafka, kanye-west, marx, maya-angelou, nietzsche, paul-graham, rilke, sara-blakely, woolf | arendt, aristoteles, epiktetos, frida-kahlo, gandhi, hume, kant, kierkegaard, konfucyus, laozi, marcus-aurelius, martin-luther-king, mill, platon, seneca, spinoza, steve-jobs, tolstoy, wollstonecraft, zhuangzi |
| `erteleme-disiplin` | aristoteles, camus, epiktetos, epikuros, gandhi, kafka, kanye-west, kierkegaard, konfucyus, laozi, marcus-aurelius, martin-luther-king, maya-angelou, nietzsche, paul-graham, rilke, seneca, sokrates, tolstoy, wollstonecraft | arendt, beauvoir, du-bois, frida-kahlo, hume, kant, marx, mill, platon, sara-blakely, steve-jobs, woolf |
| `ozguven-kimlik` | arendt, aristoteles, baldwin, beauvoir, du-bois, epiktetos, frida-kahlo, gandhi, hume, kafka, kanye-west, kierkegaard, konfucyus, laozi, martin-luther-king, maya-angelou, mill, nietzsche, sara-blakely, steve-jobs, wollstonecraft, woolf, zhuangzi | camus, epikuros, kant, marcus-aurelius, marx, paul-graham, platon, rilke, seneca, sokrates, spinoza, tolstoy |
| `ofke-catisma` | arendt, aristoteles, baldwin, camus, du-bois, epiktetos, frida-kahlo, gandhi, hume, kafka, kanye-west, konfucyus, laozi, marcus-aurelius, martin-luther-king, marx, mill, nietzsche, platon, seneca, sokrates, spinoza, tolstoy, wollstonecraft, zhuangzi | beauvoir, epikuros, kant, kierkegaard, maya-angelou, paul-graham, rilke, steve-jobs, woolf |
| `adaletsizlik-ayrimcilik` | arendt, aristoteles, baldwin, beauvoir, camus, du-bois, epiktetos, epikuros, frida-kahlo, gandhi, hume, kafka, kant, kanye-west, kierkegaard, konfucyus, laozi, marcus-aurelius, martin-luther-king, marx, maya-angelou, mill, nietzsche, paul-graham, platon, rilke, sara-blakely, seneca, sokrates, spinoza, tolstoy, wollstonecraft, woolf, zhuangzi | — |
| `ozgurluk-baski` | arendt, aristoteles, baldwin, beauvoir, camus, du-bois, epiktetos, frida-kahlo, gandhi, hume, kafka, kant, kanye-west, kierkegaard, konfucyus, laozi, marcus-aurelius, martin-luther-king, marx, maya-angelou, mill, nietzsche, paul-graham, platon, rilke, seneca, sokrates, spinoza, steve-jobs, tolstoy, wollstonecraft, woolf, zhuangzi | epikuros, sara-blakely |
| `karar-ikilem` | arendt, aristoteles, baldwin, beauvoir, camus, epiktetos, epikuros, gandhi, hume, kafka, kant, kierkegaard, konfucyus, marcus-aurelius, martin-luther-king, maya-angelou, mill, paul-graham, platon, rilke, seneca, sokrates, spinoza, steve-jobs, tolstoy, zhuangzi | du-bois, frida-kahlo, laozi, marx, nietzsche, sara-blakely, wollstonecraft, woolf |
| `basarisizlik-red` | beauvoir, gandhi, hume, kafka, kanye-west, konfucyus, marcus-aurelius, martin-luther-king, marx, maya-angelou, paul-graham, rilke, sara-blakely, steve-jobs, wollstonecraft | arendt, aristoteles, camus, du-bois, epiktetos, kant, kierkegaard, laozi, nietzsche, platon, seneca, sokrates, tolstoy, woolf, zhuangzi |
| `olum-sonluluk` | baldwin, beauvoir, camus, du-bois, epiktetos, epikuros, frida-kahlo, hume, kafka, kant, kierkegaard, konfucyus, laozi, marcus-aurelius, martin-luther-king, platon, rilke, seneca, sokrates, spinoza, steve-jobs, tolstoy, wollstonecraft, woolf, zhuangzi | nietzsche |
| `kiskanclik-karsilastirma` | beauvoir, frida-kahlo, gandhi, kierkegaard, laozi, nietzsche, spinoza, tolstoy, wollstonecraft, zhuangzi | arendt, du-bois, epiktetos, epikuros, hume, kant, konfucyus, marcus-aurelius, marx, maya-angelou, mill, paul-graham, platon, rilke, seneca, sokrates, woolf |
| `tukenmislik` | hume, kafka, kanye-west, marx, mill, paul-graham, seneca | arendt, aristoteles, beauvoir, camus, du-bois, epiktetos, epikuros, frida-kahlo, gandhi, kant, kierkegaard, konfucyus, laozi, marcus-aurelius, martin-luther-king, nietzsche, platon, rilke, sokrates, spinoza, steve-jobs, tolstoy, wollstonecraft, woolf, zhuangzi |
| `ahlak-vicdan` | arendt, aristoteles, baldwin, beauvoir, camus, du-bois, epiktetos, epikuros, frida-kahlo, gandhi, hume, kafka, kant, kanye-west, kierkegaard, konfucyus, laozi, marcus-aurelius, martin-luther-king, marx, maya-angelou, mill, nietzsche, paul-graham, platon, rilke, seneca, sokrates, spinoza, steve-jobs, tolstoy, wollstonecraft, woolf, zhuangzi | sara-blakely |
| `girisim-risk` | du-bois, kanye-west, martin-luther-king, paul-graham, sara-blakely, steve-jobs, tolstoy | arendt, aristoteles, baldwin, beauvoir, epiktetos, epikuros, gandhi, hume, kafka, kierkegaard, konfucyus, laozi, marcus-aurelius, marx, mill, nietzsche, platon, rilke, seneca, sokrates, spinoza, wollstonecraft, woolf, zhuangzi |
| `beden-imaj` | beauvoir, epiktetos, frida-kahlo, gandhi, kafka, maya-angelou, platon, sara-blakely, sokrates, wollstonecraft, woolf, zhuangzi | baldwin, kierkegaard, laozi, marcus-aurelius, mill, rilke, seneca, spinoza |
