"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) bulan bir program yazınız..

Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katını (EKOK) bulan bir program yazınız..

"""

# from math import gcd, lcm

# print(gcd(12, 18))
# print(lcm(8, 9))

num1 = int(input("Write a number : "))
num2 = int(input("Write a number again : "))
s1 = []
s2 = []
for i in range(1,num1 + 1):
    if num1 % i == 0:
        s1.append(i)
for j in range(1,num2 + 1):
    if num2 % j== 0:
        s2.append(j)
s1_set =set(s1)
print(s1_set)
s2_set =set(s2)
print(s2_set)
ebob = max(s1_set.intersection(s2_set))
print(f"ebob = ", ebob)

"""
ekok = (sayi1*sayi2)/ebob
"""