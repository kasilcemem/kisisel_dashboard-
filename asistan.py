import os
import shutil

# Neyi nereye taşıyacağız?
HEDEFLER = {
    "sinema": [".mp4", ".mkv", ".url", ".txt"],
    "mimari": [".pdf", ".dwg"],
    "bonsai": [".jpg", ".jpeg", ".png"]
}

def sistemi_guncelle():
    # 1. Dosyaları klasörlerine taşı
    for dosya in os.listdir("."):
        if os.path.isfile(dosya) and dosya not in ["asistan.py", "index.html"]:
            uzanti = os.path.splitext(dosya)[1].lower()
            for klasor, uzantilar in HEDEFLER.items():
                if uzanti in uzantilar:
                    yol = f"veriler/{klasor}"
                    os.makedirs(yol, exist_ok=True)
                    shutil.move(dosya, f"{yol}/{dosya}")

    # 2. HTML'i güncelle
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            icerik = f.read()

        for klasor in HEDEFLER.keys():
            isaret = f"<!-- {klasor.upper()}_LISTESI -->"
            yol = f"veriler/{klasor}"
            linkler = ""
            if os.path.exists(yol):
                for d in os.listdir(yol):
                    linkler += f'<a href="{yol}/{d}" target="_blank">📄 {d}</a>\n'
            
            if isaret in icerik:
                parcalar = icerik.split(isaret)
                # Sadece linkleri tazele, diğer her şeyi koru
                icerik = parcalar[0] + linkler + isaret + parcalar[-1].split("</a>")[-1]

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(icerik)

if __name__ == "__main__":
    sistemi_guncelle()
