# number = int(input("is that a prime number, let's check it!: "))


# if number > 1:
#     for i in range(2, number):
#         if number % i == 0:
#             print(f"{number} is not a prime number!")
#             break
#     else:
#         print(f"{number} is a prime number!")


# else:
#     print(f"{number} is not a prime number!")

n = int(input("enter a positive integer: "))
counter = 0
for i in range(1, n + 1):
    if n % i == 0:
        counter += 1

if (n == 0) or (n == 1) or (counter >= 3):
    print(n, "is NOT a prime number")
else:
    print(n, "is a prime number")