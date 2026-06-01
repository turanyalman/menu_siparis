import menu 
import islemler

while True:
    print("\n1. Menüyü Gör")
    print("2. Sepete Ürün Ekle")
    print("3. Sepeti ve Toplam Tutarı Gör")
    print("4. Çıkış")
    
    secim = input("Yapmak istediğiniz işlemi seçin (1-4): ")
    
    if secim == "1":
       islemler.menuyu_goster()
        
    elif secim == "2":
        urun = input("Eklenecek ürünün adını yazın: ")
        if urun in menu.restoran_menusu:
            islemler.sepete_ekle(urun)
        else:
            print("Maalesef bu ürün menümüzde yok.")
            
    elif secim == "3":
        
        print("\nSepetinizdeki Ürünler:", islemler.sepetim)
        toplam = islemler.toplam_hesapla(islemler.restoran_menusu)
        print("Toplam Ödenecek Tutar:", toplam, "TL")
        
    elif secim == "4":
        print("Bizi tercih ettiğiniz için teşekkürler, iyi günler!")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
