laborer = []
information_list = []
toplam = 0
repeater = "y"
while repeater == "y":

    laborer.append(input("name:"))
    # phone = int(input("phone number"))
    # address = input("address pls.")
    information_list.append({"phone" : int(input("phone number")), "address" : input("address pls.")})
    toplam += 1
    repeater = input("for new input press 'y' otherwise press 'n' : ").lower().strip()
    

Result = dict(zip(laborer, information_list))
print(Result)