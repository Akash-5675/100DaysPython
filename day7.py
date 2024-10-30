import random
word_list = ["aardvark" , "baboon" , "camel"]

choosenWord = random.choice(word_list)
print(choosenWord)

lives = 6
placeholder = ""
 
wordLength = len(choosenWord)
for i in range(wordLength):
    placeholder += "_" 
print(placeholder)

gameover = False
correctList = []

while not gameover:
    guess = input("Guess a letter in the word ").lower()
    display = ""


    for i in choosenWord:
        if i == guess:
            display += guess
            correctList.append(guess)
        elif i in correctList:
            display += i
        else:
            display += "_"
    
    print(display)
    
    
    while guess not in choosenWord:
        lives -= 1
        if lives == 0:
            print("you lose")
    
    if "_" not in display:
        gameover = True
        print("you win!!!")

