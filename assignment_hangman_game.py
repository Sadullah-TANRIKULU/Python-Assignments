import random
import string

words = ["LONDON", "PARIS", "ISTANBUL", "TORINO", "TOKYO", "TEXAS"]

def hangman():
    word = random.choice(words)  # listedeki rastgele bir kelime seçilir. 
    word_letters = set(word)  # kelimenin harfleri ayrılır. 
    alphabet = set(string.ascii_uppercase)  # büyük harfleri küme şeklinde yazdırdık ascii sırasıyla import string lib ile. 
    used_letters = set()  # kullanılmış harfler için boş küme açtık. 
    lives = 6


    while len(word_letters) > 0 and lives > 0:
        print("You have used these letters: ", " ".join(used_letters)) # araya bir boşluk vererek, kullanılmış harfleri yanda gösteriyoruz. 

        word_list = [letter if letter in used_letters else "-" for letter in word]  
        # üstte list comprehension ile kelimenin her harfini gezip #tahmin edilen harf varsa yazdır, yoksa - şeklinde print ediyoruz. 
        print("Current word: ", " ".join(word_list))
        print(f"Your lives: {lives}")

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in used_letters:
            print("You have already used this letter..")

        else:
            print("Invalid character..")

    if lives == 0:
        print(f"Sorry, you lost... The correct word was {word} ")
    else:
        print(f"Congratulations!! You won! The word is {word} ")


hangman()