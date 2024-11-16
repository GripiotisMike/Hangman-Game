import random

# Hangman stages representing the player's life status
stages = [
    '''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
    '''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    '''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    '''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''  +---+
  |   |
      |
      |
      |
      |
========='''
]

# Hangman logo
logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
'''

# Word list
word_list = [
    'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes',
    'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm',
    'buzzard', 'caliph', 'cobweb', 'cycle', 'daiquiri', 'dizzying', 'duplex', 'embezzle', 'equip',
    'exodus', 'fuchsia', 'galaxy', 'gizmo', 'haiku', 'ivory', 'jackpot', 'jigsaw', 'jinx', 'juicy',
    'jukebox', 'kayak', 'kilobyte', 'luxury', 'mystify', 'onyx', 'oxygen', 'pajama', 'pixel', 'quartz',
    'quiz', 'quizzes', 'rhubarb', 'sphinx', 'strength', 'twelfth', 'unknown', 'vaporize', 'vodka',
    'waltz', 'whizzing', 'wizard', 'xylophone', 'yachtsman', 'zephyr', 'zodiac', 'zombie'
]

def hangman():
    """Main function to play Hangman."""
    print(logo)
    
    # Randomly select a word
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    # Initialize variables
    display = ["_"] * word_length
    lives = len(stages) - 1
    guessed_letters = []
    end_of_game = False

    # Main game loop
    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        # Check for repeated guesses
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again!")
            continue
        guessed_letters.append(guess)

        # Update the display if the guess is correct
        if guess in chosen_word:
            for position in range(word_length):
                if chosen_word[position] == guess:
                    display[position] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose!")
                print(f"The word was: {chosen_word}")
        
        # Show progress
        print(f"{' '.join(display)}")
        print(stages[lives])

        # Check for a win
        if "_" not in display:
            end_of_game = True
            print("Congratulations, you win!")

if __name__ == "__main__":
    hangman()
