numberee = input("Is this an Armstrong number? Pls try it!:")

if not numberee.isdecimal():  # isdecimal ile positive integer olmasını sağladık. 
    print("Pls, input a positive integer, not float or negative. ")
else:
    str_digitee = str(numberee)
    sumee = 0
    for i in str_digitee:
        digitee = (int(i)**len(str_digitee))
        sumee += digitee
    if sumee == int(numberee):
        print(numberee, "It is an Armstrong number.")
    else:
        print(numberee, "It is NOT an Armstrong number.")


# 3 basamağa kadar armstrong çözümü
# x = int(input("pls enter 3 digit number : "))
# a = (x) // 100
# b = (x) // 10 % 10
# c = (x) % 10
# if (a ** 3 + b ** 3 + c ** 3) == (x):
#   print("your number is astronout number ")
# elif int(x) < 0 :
#   print("do not use negatif number")
# else:
#   print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")





