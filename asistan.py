import os
import shutil

# Düzenleme kuralları
AYARLAR = {
    "sinema": [".mp4", ".mkv", ".url", ".txt"],
    "mimari": [".pdf", ".dwg", ".url"],
    "bonsai": [".jpg", ".png", ".jpeg"]
}

def arsivi_bagla():
    # 1. Klasörleme
    for dosya in os.listdir("."):
        if os.path.isfile(dosya) and dosya not in ["asistan.py", "index.html"]:
            _, uzanti = os.path.splitext(dosya)
            for klasor, uzantilar in AYARLAR.items():
                if uzanti.lower() in uzantilar:
                    hedef = f"veriler/{klasor}"
                    if not os.path.exists(hedef): os.makedirs(hedef)
                    shutil.move(dosya, f"{hedef}/{dosya}")

    # 2. HTML Paneline Entegrasyon
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            html = f.read()

        for klasor in AYARLAR.keys():
            marker = f"<!-- {klasor.upper()}_LISTESI -->"
            yol = f"veriler/{klasor}"
            link_grubu = f'<div style="color:#58a6ff; font-size:0.7em; margin-top:10px;">{klasor.upper()}</div>'
            
            if os.path.exists(yol):
                for d in os.listdir(yol):
                    link_grubu += f'<a href="{yol}/{d}" target="_blank">📄 {d}</a>\n'
            
            if marker in html:
                parcalar = html.split(marker)
                html = parcalar[0] + link_grubu + marker + parcalar[-1].split("</a>")[-1]

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)

if __name__ == "__main__":
    arsivi_bagla()
