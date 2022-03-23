"""
Task : Print the prime numbers which are between 1 to entered limit number (n).

You can use a nested for loop.
Collect all these numbers into a list
The desired output for n=100 :

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
61, 67, 71, 73, 79, 83, 89, 97]
"""

n = int(input("a number to make a prime number list : "))
empty_list = []
if n > 0:
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            empty_list.append(i)

else:
    print("it must be greater than 0!")


print(empty_list)