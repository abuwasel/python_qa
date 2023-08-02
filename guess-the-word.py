import random
import time

def lottery_number_and_get_word():
    file = open('guess-the-word.txt', 'r')
    lines = file.readlines()
    word_choice = random.randint(0, len(lines))
    return lines[word_choice].split()

def underscores(lst):
    result = []
    for word in lst:
        underscored_word = "_" * len(word)
        result.append(underscored_word.strip())
    return result


word_list = lottery_number_and_get_word()
underscores_list = underscores(word_list)
print(word_list)
print(underscores_list)
score = 0
bonus = 100
start_time = time.time()

while True:
    letter_to_check = input("Enter a letter: ")
    for index, word in enumerate(word_list):
        for position, letter in enumerate(word):
            if letter.lower() == letter_to_check.lower():
                underscores_list[index] = underscores_list[index][:position] + letter + underscores_list[index][position + 1:]
                score += 5

    letter_is_present = any(letter_to_check.lower() in word.lower() for word in word_list)

    if letter_is_present == False:
       print("Sorry, that letter isn't here! try again...")
       score = 0 if score == 0 else score - 5

    print(underscores_list)
    print(f'Your score is:{score}')

    elapsed_time = time.time() - start_time
    bonus = 0 if elapsed_time >= 30 else bonus

    underscore_not_found = '_' not in ''.join(underscores_list)
    if underscore_not_found:
        print("Congratulations, you won!")
        print(f'Your score is:{score + bonus}')
        break