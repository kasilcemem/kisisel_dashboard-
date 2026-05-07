import os
import shutil

HEDEFLER = {
    "sinema": [".mp4", ".mkv", ".url", ".txt"],
    "mimari": [".pdf", ".dwg"],
    "bonsai": [".jpg", ".jpeg", ".png"]
}

def baslat():
    # 1. Dosyaları Taşı
    for dosya in os.listdir("."):
        if os.path.isfile(dosya) and dosya not in ["asistan.py", "index.html"]:
            uzanti = os.path.splitext(dosya)[1].lower()
            for klasor, uzantilar in HEDEFLER.items():
                if uzanti in uzantilar:
                    yol = f"veriler/{klasor}"
                    os.makedirs(yol, exist_ok=True)
                    shutil.move(dosya, f"{yol}/{dosya}")

    # 2. HTML'i Noktasal Güncelle
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            html = f.read()

        for klasor in HEDEFLER.keys():
            basla_isareti = f"<!-- {klasor.upper()}_LISTESI_BASLA -->"
            bitis_isareti = f"<!-- {klasor.upper()}_LISTESI_BITIS -->"
            
            yol = f"veriler/{klasor}"
            yeni_linkler = ""
            if os.path.exists(yol):
                for d in os.listdir(yol):
                    yeni_linkler += f'<a href="{yol}/{d}" target="_blank">📄 {d}</a>\n'
            
            if basla_isareti in html and bitis_isareti in html:
                basi = html.split(basla_isareti)[0]
                sonu = html.split(bitis_isareti)[1]
                html = basi + basla_isareti + "\n" + yeni_linkler + bitis_isareti + sonu

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)

if __name__ == "__main__":
    baslat()
