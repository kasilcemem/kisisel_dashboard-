import os
import shutil

# 1. AYARLAR: Hangi dosya hangi klasöre gidecek?
AYARLAR = {
    "sinema": [".mp4", ".mkv", ".url", ".txt"],
    "bonsai": [".jpg", ".jpeg", ".png"],
    "mimari": [".pdf", ".dwg", ".dxf", ".url"], # .url buraya eklendi!
    "frekans": [".mp3", ".wav"]
}

def sistem_calistir():
    # 1. ADIM: Dosyaları Klasörlere Taşı
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

    # 2. ADIM: HTML Sayfasını (Dashboard) Güncelle
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            html = f.read()

        for klasor in AYARLAR.keys():
            isaretci = f"<!-- {klasor.upper()}_LISTESI -->"
            yol = f"veriler/{klasor}"
            linkler_html = ""
            
            if os.path.exists(yol):
                dosyalar = os.listdir(yol)
                for d in dosyalar:
                    # Tıklanabilir linkleri oluşturur
                    linkler_html += f'<a href="{yol}/{d}" target="_blank">🔗 {d}</a>\n'
            
            # HTML içindeki işareti bul ve listeyi oraya yerleştir
            if isaretci in html:
                # Önceki listeyi temizlemek için işareti koruyarak değiştirme yapıyoruz
                # Bu kısım her çalışma anında listeyi sıfırdan oluşturur
                parcalar = html.split(isaretci)
                if len(parcalar) > 1:
                    # Sadece işaretçinin olduğu yeri yeni linklerle doldurur
                    html = parcalar[0] + linkler_html + isaretci + parcalar[1].split(f"<!-- /{klasor.upper()} -->")[-1]

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)

if __name__ == "__main__":
    sistem_calistir()
