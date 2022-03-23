"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. 
İlk olarak kullanıcıdan 
üçgenin mi 
dörtgenin mi 
tipini bulmak istediğini sorun.
Eğer kullanıcı "Dörtgen" cevabını verirse , 
4 tane kenar isteyip bu dörtgenin
kare mi , 
dikdörtgen mi 
yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.
Eğer kullanıcı "Üçgen" cevabını verirse , 
3 tane kenar isteyip bu üçgenin 
ikizkenar mı , 
eşkenar mı 
yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. 
Eğer verilen kenarlar bir üçgen belirtmiyorsa, 
ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.
(üçgen olma şartı : uzun kenar iki kısa kenar toplamından büyük olamaz)

"""
shape = input("is it a rectangle or triangle? : ")
if shape == "rectangle" :
    a = input( "first side: " )
    b = input( "second side: " )
    c = input( "third side: " )
    d = input( "fourth side: " )
    if a == b == c == d:
        print("it's a square")
    elif a == c and b == d:
        print("it's a rectangle")
    else:
        print("it's a trapezoid")
elif shape == "triangle" :
    a = input( "first side: " )
    b = input( "second side: " )
    c = input( "third side: " )
    if (a + b > c) or (a + c > b) or (b + c > a):
        print("yeah, it's a triangle, and...")
        if a == b == c:
            print("it's a equilateral triangle")
        elif a == b or a == c or b == c:
            print("it's a isosceles triangle")
        else:
            print("it's a scalene triangle")
    else:
        print("lenghts don't indicate a triangle")
else:
    print("please, input rectangle or triangle, next time!")




















