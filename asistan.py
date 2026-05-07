import os
import shutil

AYARLAR = {
    "sinema": [".mp4", ".mkv", ".url", ".txt", ".pdf"],
    "bonsai": [".jpg", ".jpeg", ".png"],
    "mimari": [".pdf", ".dwg", ".dxf", ".url"]
}

def baslat():
    # 1. Dosya Düzenleme
    for dosya in os.listdir("."):
        if os.path.isfile(dosya) and dosya not in ["asistan.py", "index.html"]:
            _, uzanti = os.path.splitext(dosya)
            for klasor, uzantilar in AYARLAR.items():
                if uzanti.lower() in uzantilar:
                    yol = f"veriler/{klasor}"
                    if not os.path.exists(yol): os.makedirs(yol)
                    shutil.move(dosya, f"{yol}/{dosya}")

    # 2. Ekrana Yazma
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            html = f.read()

        for klasor in AYARLAR.keys():
            marker = f"<!-- {klasor.upper()}_LISTESI -->"
            yol = f"veriler/{klasor}"
            liste = ""
            if os.path.exists(yol):
                for d in os.listdir(yol):
                    liste += f'<a href="{yol}/{d}" target="_blank">▶️ {d}</a>\n'
            
            if marker in html:
                parts = html.split(marker)
                html = parts[0] + liste + marker + parts[-1].split("</a>")[-1]

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)

if __name__ == "__main__":
    baslat()
