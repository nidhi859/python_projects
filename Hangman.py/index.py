import random_word
# function changes the current word's status
def change_current_word_state(selected_word,current_word_state,input_char):
    modified_word_state = ""

    for i in range(len(selected_word)):
        if current_word_state[i] == "_" and selected_word[i] == input_char:
            modified_word_state += input_char
        else:
            modified_word_state += current_word_state[i]    

    return modified_word_state        

# function to print the current state of the game
def print_current_state(current_word_state,attempts_remaining):
    print("current state: ", end=" ")

    for i in current_word_state:
        print(i,end=" ")
    
    print("\t attempts remaining : {}".format(attempts_remaining))

#function to check wether the entered caharacter is in selected word or not
def input_character_in_word(selected_word, input_char, current_word_state, attempts_remaining):
    if input_char in selected_word:
        current_word_state = change_current_word_state(selected_word, current_word_state, input_char)
    else:
        attempts_remaining -= 1
    return current_word_state, attempts_remaining 
 
# function checks the current game status
def check_game_status(selected_word,current_word_state,attempts_remaining):
    """ IF game has ended or not """

    if current_word_state == selected_word:
        print("You Won :D")
        return True
    elif attempts_remaining <= 0:
        print("You Loose :( Please! Try Again")
        print("Word was : {}".format(selected_word))
        return True

    return False        


# main logic function of our game
def play_game(attempts = 5):
    selected_word = random_word.pick_random_word()

    current_word_state = ""

    for i in selected_word:
        if i == " " or i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            current_word_state+=i
        else:
            current_word_state+="_"

    attempts_remaining = attempts

    print_current_state(current_word_state,attempts_remaining)
 
    while True:
        input_char = input(" Guess a character: ")
        print("")

        # check whether the input character is in selected word or not
        current_word_state, attempts_remaining = input_character_in_word(selected_word, input_char, current_word_state, attempts_remaining)
        
        print_current_state(current_word_state,attempts_remaining)

        game_ended = check_game_status(selected_word,current_word_state,attempts_remaining)

        if game_ended:
            break

if __name__ == "__main__":
    play_game()