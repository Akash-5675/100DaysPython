import random
word_list = ["aardvark" , "baboon" , "camel"]

choosenWord = random.choice(word_list)

print(choosenWord)
 
 
guess = input("Guess a letter in the word ").lower()
print(guess)
for i in choosenWord:
    if i == guess:
        print("Right")
    else:
        print("Wrong")
