"""
Given a function that accepts unlimited arguments, 
check and count how many data types are in those arguments. 
Finally return the total in a list.
List order is:
[int, str, bool, list, tuple, dictionary]

Examples
[1, 45, "Hi", False] >>>> [2, 1, 1, 0, 0, 0]
[[10, 20], ("t", "Ok"), 2, 3, 1] >>>> [3, 0, 0, 1, 1, 0]
["Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23]>>>> [2, 2, 3, 1, 0, 2]
[4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6] ]>>>>> [2, 0, 1, 2, 2, 0]

"""
#  [int, str, bool, list, tuple, dictionary]
complex_list = [1, 45, "Hi", 5, "string", [1, 2, 3], {"hakan" : "david"}, (1,)]
# a = [0, 0, 0, 0, 0, 0]
# for i in complex_list:
#     print(type(i))
#     if type(i) == int:
#         a[0] +=1
#     elif type(i) == str:
#         a[1] +=1
#     elif type(i) == bool:
#         a[2] +=1
#     elif type(i) == list:
#         a[3] +=1
#     elif type(i) == tuple:
#         a[4] +=1
#     elif type(i) == dict:
#         a[5] +=1
# print(a)
print(list(map(type, complex_list)).count(int))
print(list(map(type, complex_list)).count(str))
print(list(map(type, complex_list)).count(bool))
print(list(map(type, complex_list)).count(list))
print(list(map(type, complex_list)).count(tuple))
print(list(map(type, complex_list)).count(dict))

    







