"""
The first amicable number pair 220 and 284. What are Amicable numbers?
 The proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110. The sum proper divisors of 220 is 284. Also, proper divisors of 284 are 1, 2, 4, 71 and 142.
The sum proper divisors of 284 is 220. The first ten amicable pairs are: (220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368), (10744, 10856), (12285, 14595), (17296, 18416), (63020, 76084), and (66928, 66992).  So, what are the amicable numbers until 100000. Write a python code.


"""
num1 = int(input("looking for amicable number1!"))
num2 = int(input("looking for amicable number2!"))
total_div1 = 0
total_div2 = 0
for div_num1 in range(1, num1):
    if num1 % div_num1 == 0:
        total_div1 += div_num1

for div_num2 in range(1, num2):
    if num2 % div_num2 == 0:
        total_div2 += div_num2

if total_div1 == num2 and total_div2 == num1:
    print("These are amicable numbers : ", num1,",", num2)
else:
    print("these are not amicable numbers : ", num1, ",", num2)



