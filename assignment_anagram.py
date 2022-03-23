anagram_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
empty_dict = {}

for i in anagram_list:
    # print(sorted(i))
    x = "".join(sorted(i)) # stringe çevirdik
    # print(type(x))
    if x not in empty_dict:
        empty_dict[x] = [i]  # sorted olmayan i
    else:
        empty_dict[x].append(i)
           # {aet: ["eat", "tea"], "tea"}
print(list(empty_dict.values()))