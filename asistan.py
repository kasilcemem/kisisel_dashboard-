import os
import shutil

# Ayarlar: Uzantıları ve hedef klasörleri tanımlıyoruz
AYARLAR = {
    "sinema": [".mp4", ".mkv", ".url", ".txt"],
    "mimari": [".pdf", ".dwg", ".url"],
    "bonsai": [".jpg", ".png", ".jpeg"]
}

def baslat():
    # 1. Ana dizindeki dosyaları tara
    for dosya in os.listdir("."):
        # Sadece dosyaları al, asistan ve index dosyalarını elleme
        if os.path.isfile(dosya) and dosya not in ["asistan.py", "index.html"]:
            dosya_adi, uzanti = os.path.splitext(dosya)
            
            for klasor, uzantilar in AYARLAR.items():
                if uzanti.lower() in uzantilar:
                    # Klasör yoksa oluştur (Hata almamak için kritik adım)
                    hedef_klasor = os.path.join("veriler", klasor)
                    os.makedirs(hedef_klasor, exist_ok=True)
                    
                    # Dosyayı taşı
                    hedef_yol = os.path.join(hedef_klasor, dosya)
                    try:
                        shutil.move(dosya, hedef_yol)
                        print(f"Başarıyla taşındı: {dosya} -> {hedef_klasor}")
                    except Exception as e:
                        print(f"Taşıma hatası: {e}")

    # 2. HTML'i güncelleme kısmını koru (Ekranda görünmesi için)
    # (Buradaki kodların index.html ile uyumlu olduğundan emin ol)

if __name__ == "__main__":
    baslat()
