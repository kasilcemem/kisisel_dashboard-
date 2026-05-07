import os
import shutil

AYARLAR = {
    "sinema": [".mp4", ".mkv", ".url", ".txt", ".pdf"],
    "bonsai": [".jpg", ".jpeg", ".png"],
    "mimari": [".pdf", ".dwg", ".dxf"],
    "frekans": [".mp3", ".wav"]
}

def sistem_calistir():
    # 1. Dosyaları Taşı
    for dosya in os.listdir("."):
        if os.path.isfile(dosya) and dosya not in ["asistan.py", "index.html"]:
            _, uzanti = os.path.splitext(dosya)
            for klasor, uzantilar in AYARLAR.items():
                if uzanti.lower() in uzantilar:
                    yol = f"veriler/{klasor}"
                    if not os.path.exists(yol): os.makedirs(yol)
                    shutil.move(dosya, f"{yol}/{dosya}")

    # 2. HTML'i Güncelle
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            html = f.read()

        for klasor in AYARLAR.keys():
            isaretci = f"<!-- {klasor.upper()}_LISTESI -->"
            yol = f"veriler/{klasor}"
            linkler = ""
            if os.path.exists(yol):
                for d in os.listdir(yol):
                    linkler += f'<a href="{yol}/{d}" target="_blank">🔗 {d}</a>\n'
            
            # Eski listeyi temizle ve yenisini ekle
            if isaretci in html:
                # Bu mantık listenin birikmesini önler, her seferinde güncel klasörü yazar
                html = html.replace(isaretci, linkler + isaretci) if linkler else html

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)

if __name__ == "__main__":
    sistem_calistir()
