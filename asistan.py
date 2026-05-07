import os
import shutil

def calistir():
    # Dosyaları düzenle
    for dosya in os.listdir("."):
        if dosya.endswith(".pdf"):
            os.makedirs("veriler/mimari", exist_ok=True)
            shutil.move(dosya, f"veriler/mimari/{dosya}")
        elif dosya.endswith(".url") or dosya.endswith(".mp4"):
            os.makedirs("veriler/sinema", exist_ok=True)
            shutil.move(dosya, f"veriler/sinema/{dosya}")

    # HTML'i güncelle
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            html = f.read()

        # Mimari PDF'leri ekle
        if os.path.exists("veriler/mimari"):
            kitaplar = "".join([f'<a href="veriler/mimari/{d}" target="_blank">📕 {d}</a>' for d in os.listdir("veriler/mimari")])
            html = html.replace("<!-- MIMARI_DURAK -->", kitaplar + "<!-- MIMARI_DURAK -->")

        # Filmleri ekle
        if os.path.exists("veriler/sinema"):
            filmler = "".join([f'<a href="veriler/sinema/{d}" target="_blank">🎬 {d}</a>' for d in os.listdir("veriler/sinema")])
            html = html.replace("<!-- SINEMA_DURAK -->", filmler + "<!-- SINEMA_DURAK -->")

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)

if __name__ == "__main__":
    calistir()
