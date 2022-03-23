"""
Kullanıcıdan integer bir değer alan ve sayının pozitif-çift sayı olup olmadığını kontrol eden program yazınız. Girilen sayıların muhtemel farklı durumlarını göz önünde bulundurunuz. (negatif, string vs. gibi durumlar)
"""
if __name__ == "__main__":  # modul olarak import ettiğimizde kodu çalıştırmadan 
                            # sadece built-in fonksiyonları göstersin diye yazdık!
                            # herhangi bir .py dosyası içinde import even_check_num dersek anlaşılır!

    number = input("gimme a number!: ")
    if not number.isdigit():
        print("integer pls!")
    elif number.isdigit() and int(number) % 2 == 0:
        print(f"{number} is an even number. ")
            
    else:
        print(f"{number} is not an even number. ")
        

    


