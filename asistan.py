import os
import shutil

# 1. KATEGORİ VE DOSYA YAPILANDIRMASI
AYARLAR = {
    "sinema": [".mp4", ".mkv", ".url", ".txt"],
    "bonsai": [".jpg", ".jpeg", ".png"],
    "mimari": [".pdf", ".dwg", ".dxf"],
    "frekans": [".mp3", ".wav"]
}

def dosyalari_duzenle():
    """Ana dizindeki dosyaları ilgili klasörlere taşır."""
    for dosya in os.listdir("."):
        if os.path.isfile(dosya) and dosya not in ["asistan.py", "index.html"]:
            _, uzanti = os.path.splitext(dosya)
            for klasor, uzantilar in AYARLAR.items():
                if uzanti.lower() in uzantilar:
                    hedef_yol = f"veriler/{klasor}"
                    if not os.path.exists(hedef_yol):
                        os.makedirs(hedef_yol)
                    shutil.move(dosya, f"{hedef_yol}/{dosya}")
                    print(f"Taşındı: {dosya} -> {klasor}")

def index_guncelle():
    """index.html dosyasını klasör içeriğine göre yeniler."""
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    for klasor in AYARLAR.keys():
        yol = f"veriler/{klasor}"
        linkler_html = ""
        
        if os.path.exists(yol):
            dosyalar = os.listdir(yol)
            for d in dosyalar:
                # GitHub Pages üzerinde dosya yolu oluşturma
                linkler_html += f'<a href="{yol}/{d}" target="_blank">🔗 {d}</a>\n'
        
        # HTML içindeki yorum satırlarını (placeholder) gerçek linklerle değiştirir
        isaretci = f"<!-- {klasor.upper()}_LISTESI -->"
        if isaretci in html:
            # Her güncellemede listeyi temizleyip yeniden yazmak için:
            html = html.replace(isaretci, linkler_html + isaretci)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    dosyalari_duzenle()
    index_guncelle()
