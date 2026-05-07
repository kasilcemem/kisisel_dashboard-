import os
import shutil

# Hedef klasörleri tanımlayalım
KLASORLER = {
    "bonsai": [".jpg", ".png", ".jpeg"], # Bonsai fotoğrafları
    "mimari": [".pdf", ".dwg"],          # Mimari planlar
    "frekans": [".mp3", ".wav"]          # Ses dosyaları
}

def dosyalari_duzenle():
    # Ana dizindeki dosyaları tara
    for dosya in os.listdir("."):
        # Klasörleri atla, sadece dosyalara bak
        if os.path.isfile(dosya):
            dosya_adi, uzanti = os.path.splitext(dosya)
            
            # Uzantıya göre hangi klasöre gideceğini bul
            hedef_bulundu = False
            for klasor, uzantilar in KLASORLER.items():
                if uzanti.lower() in uzantilar:
                    # Eğer klasör yoksa oluştur
                    if not os.path.exists(f"veriler/{klasor}"):
                        os.makedirs(f"veriler/{klasor}")
                    
                    # Dosyayı taşı
                    shutil.move(dosya, f"veriler/{klasor}/{dosya}")
                    print(f"Taşındı: {dosya} -> {klasor}")
                    hedef_bulundu = True
                    break
            
            if not hedef_bulundu and dosya != "asistan.py":
                print(f"Atlandı (Uygun klasör yok): {dosya}")

if __name__ == "__main__":
    dosyalari_duzenle()
