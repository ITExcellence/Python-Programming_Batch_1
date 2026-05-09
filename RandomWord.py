from wonderwords import RandomWord

r = RandomWord()

word = r.word(include_parts_of_speech=["verb"], word_min_length=5, word_max_length=8)

n = len(word)
guess = []
for i in range(n):
    guess.append('_')

lives = 9999999

while True:
    print(f"Lives: {lives}")    
    print(guess)
    char = input("Guess an alphabet: ")
    
    correct = False
    for i in range(n):
        if char == word[i]:
            correct = True
            guess[i] = char

    if correct == False:
        lives -= 1
            
    checker = True
    for i in range(n):
        if guess[i] != word[i]:
            checker = False
            break 
        
    if checker == True:
        print(guess)
        print("Congratulations you guessed it")
        break 
        
    if lives == 0:
        print(word)
        print("Sorry you are out of lives")
        break  
