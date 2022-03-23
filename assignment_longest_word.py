sentence = input("Gimme a sentence. : ")
print(sentence)

word_list = sentence.split()

longest = 0
i = 0

while i < len(word_list) :
    
    if len(word_list[i]) > longest :
        longest = len(word_list[i])
        
    i += 1
    
print("The length of the longest word : ", longest)

"""
sentence = input("gimme the sentence")
print(sentence)
words_list = list(sentence.split())
while True:
    print(len(max(words_list, key=len)))
    break

"""