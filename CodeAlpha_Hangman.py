import random

words = ["python", "computer","program","keyboard","college"] 
word = random.choice(words) 
guessed_letters = [] 
attempts = 6
print("welcome to Hangman Game!")
print("guess the word one letter at a time.")
print("you have 6 incorrect guesses.")
display = ["_"] * len(word) 
while attempts > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Guessed letters:", " ".join(guessed_letters)) 
    print("Attempts left:", attempts)
    guess = input("Enter a letter:").lower()
    if len(guess) != 1 or not guess.isalpha(): 
        print("please enter only one letter.")
        continue
    if guess in guessed_letters:   
        print("you already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print("wrong guess!")
        
if "_" not in display: 
    print("\n Congratulations!")
    print("you guessed the word: " , word)
else:
    print("\n Game Over!")
    print("The correct word was:", word)    
                    
          