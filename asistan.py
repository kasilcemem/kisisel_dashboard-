import os
import shutil

# Kategoriler ve uzantılar
KLASORLER = {
    "bonsai": [".jpg", ".jpeg", ".png"],
    "mimari": [".pdf", ".dwg", ".dxf"],
    "sinema": [".mp4", ".mkv", ".avi"], # Film dosyaları veya fragmanlar
    "frekans": [".mp3", ".wav"]
}

def index_guncelle():
    # Klasörlerdeki dosyaları listele ve HTML'e yazılacak hale getir
    html_icerik = ""
    for klasor in KLASORLER.keys():
        yol = f"veriler/{klasor}"
        if os.path.exists(yol):
            dosyalar = os.listdir(yol)
            liste_elemanlari = "".join([f'<a href="{yol}/{d}">{d}</a>' for d in dosyalar])
            # HTML içindeki ilgili id alanını bulup güncellemek için işaretler
            print(f"{klasor.capitalize()} listesi güncellendi.")

def dosyalari_duzenle():
    for dosya in os.listdir("."):
        if os.path.isfile(dosya) and dosya not in ["asistan.py", "index.html"]:
            _, uzanti = os.path.splitext(dosya)
            for klasor, uzantilar in KLASORLER.items():
                if uzanti.lower() in uzantilar:
                    hedef = f"veriler/{klasor}"
                    if not os.path.exists(hedef): os.makedirs(hedef)
                    shutil.move(dosya, f"{hedef}/{dosya}")
                    break

if __name__ == "__main__":
    dosyalari_duzenle()
