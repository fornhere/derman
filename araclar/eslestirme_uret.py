"""Kişi kartlarının kimlik.md ön bilgisinden references/eslestirme.md dizinini üretir.

Kullanım: python3 araclar/eslestirme_uret.py            # yeniden üret
         python3 araclar/eslestirme_uret.py --kontrol  # güncel değilse 1 ile çıkar
Sözlük bölümü araclar/etiket-sozlugu.md dosyasından alınır; dizin kartlardan üretilir.
"""
import re
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parents[1]
P = KOK / "derman/references/personalar"
SIRA = ("anlam-amac kaygi-belirsizlik kayip-yas ask-iliski aile yalnizlik kariyer-is "
        "yaraticilik-tikanma erteleme-disiplin ozguven-kimlik ofke-catisma adaletsizlik-ayrimcilik "
        "ozgurluk-baski karar-ikilem basarisizlik-red olum-sonluluk kiskanclik-karsilastirma "
        "tukenmislik ahlak-vicdan girisim-risk beden-imaj").split()


def liste(metin, alan):
    m = re.search(rf"^{alan}:\s*\[(.*?)\]", metin, re.M)
    return [e.strip() for e in m.group(1).split(",") if e.strip()] if m else []


def main():
    dogrudan = {e: [] for e in SIRA}
    dolayli = {e: [] for e in SIRA}
    for d in sorted(x for x in P.iterdir() if x.is_dir()):
        kim = (d / "kimlik.md").read_text()
        dg = set(liste(kim, "dogrudan"))
        for e in liste(kim, "etiketler"):
            (dogrudan if e in dg else dolayli)[e].append(d.name)
    satirlar = [
        "# Eşleştirme dizini",
        "",
        "Bu dosya `araclar/eslestirme_uret.py` ile kartlardan üretilir; elle düzenleme.",
        "",
        (KOK / "araclar/etiket-sozlugu.md").read_text().strip(),
        "",
        "## Etiket → kişiler",
        "",
        "**Doğrudan:** kişi bu konuyu bizzat ele almış. **Dolaylı:** kaynaklı fikirleri bu derde uygulanıyor. "
        "Önce doğrudan listeden seç; çeşitlilik için gerekirse dolaylıdan tamamla.",
        "",
        "| Etiket | Doğrudan | Dolaylı |",
        "|---|---|---|",
    ]
    for e in SIRA:
        satirlar.append(f"| `{e}` | {', '.join(dogrudan[e]) or '—'} | {', '.join(dolayli[e]) or '—'} |")
    yeni = "\n".join(satirlar) + "\n"
    hedef = KOK / "derman/references/eslestirme.md"
    if "--kontrol" in sys.argv:
        if hedef.read_text() != yeni:
            sys.exit("eslestirme.md kartlarla uyuşmuyor; python3 araclar/eslestirme_uret.py ile yeniden üret")
        print("eslestirme.md güncel")
        return
    hedef.write_text(yeni)


if __name__ == "__main__":
    main()
