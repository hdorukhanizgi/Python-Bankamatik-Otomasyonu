# Bankamatik Uygulaması

hesaplar = [
    {
        "ad": "Doruk İzgi",
        "hesapID": "12345",
        "bakiye": 30000,
        "ekHesap": 7000,
        "password": "1234"
    },
    {
        "ad": "Emir Boztaş",
        "hesapID": "12346",
        "bakiye": 45000,
        "ekHesap": 12000,
        "password": "1235"
    }
]

def menu(hesap):
    while True:

        print(f"\nSayın {hesap['ad']}, hoşgeldiniz...")

        print("1- Bakiye Sorgulama")
        print("2- Para Çekme")
        print("3- Para Yatırma")
        print("4- Çıkış")


        islem = input("Yapmak istediğiniz işlemi seçiniz: ")

        if islem == "1":
                bakiyeSorgula(hesap)
        elif islem == "2":
                paraCekme(hesap)
        elif islem == "3":
            paraYatirma(hesap)
        elif islem == "4":
            print("İyi günler dileriz...")
            break
        else:
            print("Hatalı seçim, lütfen tekrar seçim yapınız...")


def paraYatirma(hesap):
    while True:
        try:
            yatirilacakPara = float(input("Yatırmak istediğiniz tutarı giriniz..."))

            if yatirilacakPara > 0:
                hesap["bakiye"] += yatirilacakPara
                print("Paranız yatırılmıştır...")
                print(f"Güncel hesap bakiyeniz: {hesap['bakiye']}")
                break
            else:
                print("Hatalı tutar girşi! Lütfen tekrar deneyiniz...")
        except ValueError:
            print("Hatalı giriş! Lütfen tekrar deneyiniz!")


def bakiyeSorgula(hesap):
    print(f"Bakiyeniz: {hesap['bakiye']}")
    print(f"Ek Hesap Bakiyeniz: {hesap['ekHesap']}")


def paraCekme(hesap):
    while True:
        try:
            cekilecekPara = float(input("Çekmek istediğiniz tutarı giriniz: "))

            if cekilecekPara > 0:
                if hesap["bakiye"] >= cekilecekPara:
                    hesap["bakiye"] -= cekilecekPara
                    print(f"Güncel Bakiyeniz: {hesap['bakiye']}")
                    print("Paranızı alabilirsiniz...")
                    break

                toplam = hesap["bakiye"] + hesap["ekHesap"]
                if toplam >= cekilecekPara:

                    while True:
                        ekHesapKullanimİzni = input("Hesabınızda yeterli bakiye bulunmamakta, ek hesap kullanılsın mı? (E/H): ")

                        if ekHesapKullanimİzni.upper() == "E":
                            kullanilacakMiktar = cekilecekPara - hesap["bakiye"]
                            hesap["bakiye"] = 0
                            hesap["ekHesap"] -= kullanilacakMiktar
                            print(f"Kalan Ek Hesap Tutarı: {hesap['ekHesap']}")
                            print("Paranızı alabilirsiniz...")
                            break

                        elif ekHesapKullanimİzni.upper() == "H":
                            print("İşlem iptal edildi...")
                            break
                        else:
                            print("Hatalı giriş! Tekrar deneyiniz...")
                            continue
                else:
                    print("Limit yetersiz! İşlem iptal edildi.")
                    break

        except ValueError:
            print("Hatalı giriş! Lütfen tekrar deneyiniz...")


def login():
    while True:
        hesapID = input("Hesap numaranızı giriniz: ")
        password = input("Parolanızı giriniz: ")

        isLoggedIn = False

        for hesap in hesaplar:
            if hesap["hesapID"] == hesapID and hesap["password"] == password:
                isLoggedIn = True
                menu(hesap)
                break

        if not (isLoggedIn):
            print("Hesap numaranız ya da parolanız yanlış, lütfen tekrar deneyiniz...")

login()