"""
Write a function for Floyd's triangle of n rows in Python, you need to ask from user to enter the number of rows or lines up to which.
Sample run of program, with user input 10 as number of rows, is shown in the snapshot given below:
(fonksiyonu floyd diye tanımladım ve 10 satırlık bir  üçgen elde ettik)

"""
def floyd():
    n = int(input("number of rows : "))
    num = 1 #2,3,4,5,6


    for i in range(1, n+1):  # hangi satır
        for j in range(1, i+1):  # satırdaki eleman sayısı
            print(num, end=" ")  # satıra ne yazsın
            num += 1
        print()  # print default newline \n değeri içerir. 


floyd()

