# # Problem 1
# def is_word_guessed(secret_word, letters_guessed):
#     '''
#     secret_word: string, the word the user is guessing
#     letters_guessed: list, what letters have been guessed so far
#     returns: boolean, True if all the letters of secret_word are in letters_guessed;
#       False otherwise
#     '''
#     """
#     for every letter in secret_word
#         if the letter is not in letter_guessed
#             stop looking and return false
#     return true
#     """
 
#     for letter in secret_word:
#         if letter not in letters_guessed:
#             return False
#     return True
       
 
# ### Testcases
# print(is_word_guessed('banana', ['b', 'e', 'i', 'k', 'a', 'r', 's']))
# print(is_word_guessed('watermelon', ['z', 'x', 'q', 'w', 'a', 't', 'e', 'r', 'm', 'e', 'l', 'o', 'n']))
# print(is_word_guessed('mango', []))
 
# # Problem 2
# def get_guessed_word(secret_word, letters_guessed):
#     '''
#     secret_word: string, the word the user is guessing
#     letters_guessed: list, what letters have been guessed so far
#     returns: string, comprised of letters and underscores that represents
#       what letters in secret_word have been guessed so far.
#     '''
#     output_string = ""
#     for letter in secret_word:
#         if letter in letters_guessed:
#             output_string += letter + " "
#         else:
#             output_string += "_ "
#     return output_string
 
# print(get_guessed_word('melon', ['o', 'i', 'k', 'm', 'r', 's']))
# print(get_guessed_word('grape', ['h', 'e', 'c', 'g', 'p', 'm', 'n', 'a', 't', 'r']))
# print(get_guessed_word ('strawberry', []))
 
# # Problem 3
# def get_available_letters(letters_guessed):
#     '''
#     letters_guessed: list, what letters have been guessed so far
#     returns: string, comprised of letters that represents what letters have not
#       yet been guessed.
#     '''  
#     import string
#     alphabet = list(string.ascii_lowercase)
 
#     for letter in alphabet:
#         if letter in letters_guessed:
#             alphabet.remove(letter)
 
#     return ' '.join(alphabet)
   
# print(get_available_letters('pineapple'))
# print(get_available_letters(''))

#Problem 4
import random
import string

def get_available_letters(letters_guessed):
    all_letters = string.ascii_lowercase
    return ''.join(letter for letter in all_letters if letter not in letters_guessed)

def get_guessed_word(secret_word, letters_guessed):
    return ''.join(letter if letter in letters_guessed else '_' for letter in secret_word)

def is_word_guessed(secret_word, letters_guessed):
    return all(letter in letters_guessed for letter in secret_word)

def choose_word(word_list):
    return random.choice(word_list)

def game_loop(secret_word):
    letters_guessed = []
    mistake_made = 0

    print("Let the game begin!")
    print(f"Here's a word with {len(secret_word)} letters.")

    while True:
        print(f"You have {8 - mistake_made} guesses remaining")
        print(f"Letters available to you: {get_available_letters(letters_guessed)}")
        guess = input("Guess a letter: ").lower()

        if guess in letters_guessed:
            print(f"You already tried this letter: {get_guessed_word(secret_word, letters_guessed)}")
        elif guess in secret_word:
            letters_guessed.append(guess)
            print(f"Correct! {get_guessed_word(secret_word, letters_guessed)}")
        else:
            print(f"Incorrect! This letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            mistake_made += 1

        print()

        if is_word_guessed(secret_word, letters_guessed):
            print("You WIN!")
            break
        if mistake_made == 8:
            print(f"GAME OVER! Here's the word: {secret_word}")
            break

def main():
    word_list = ["apple", "banana", "cherry", "orange", "grape"]
    secret_word = choose_word(word_list)
    game_loop(secret_word)

if __name__ == "__main__":
    main()
