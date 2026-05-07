import os
import shutil

AYARLAR = {
    "sinema": [".mp4", ".mkv", ".url", ".txt"],
    "bonsai": [".jpg", ".jpeg", ".png"],
    "mimari": [".pdf", ".dwg", ".dxf", ".url"],
    "frekans": [".mp3", ".wav"]
}

def sistem_calistir():
    # 1. Dosyaları Klasörlere Taşı
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
            html_icerik = f.read()

        for klasor in AYARLAR.keys():
            isaretci = f"<!-- {klasor.upper()}_LISTESI -->"
            yol = f"veriler/{klasor}"
            yeni_linkler = ""
            
            if os.path.exists(yol):
                dosyalar = os.listdir(yol)
                for d in dosyalar:
                    yeni_linkler += f'<a href="{yol}/{d}" target="_blank">🔗 {d}</a>\n'
            
            if isaretci in html_icerik:
                # Mevcut listeyi temizleyip yeniden ekleyen mantık
                temiz_html = html_icerik.split(isaretci)
                if len(temiz_html) > 1:
                    # Sadece en son yüklenenleri değil, klasördeki her şeyi listeler
                    html_icerik = temiz_html[0] + yeni_linkler + isaretci + temiz_html[-1].split("</a>")[-1]

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html_icerik)

if __name__ == "__main__":
    sistem_calistir()
