import random

words=["apple","orange","cherry","banana","grape"]

hangman_art = {
    0: ("      ",
        "      ",
        "      "),
    1: ("  O   ",
        "      ",
        "      "),
    2: ("  O   ",
        "  |   ",
        "      "),
    3: ("  O   ",
        " /|   ",
        "      "),
    4: ("  O   ",
        " /|\\  ",
        "      "),
    5: ("  O   ",
        " /|\\  ",
        " /    "),
    6: ("  O   ",
        " /|\\  ",
        " / \\ ")}


def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
     print(" ".join(hint))



def main():
    answer= random.choice(words)
    hint=["_"] * len(answer)
    wrong_guesses=0
    guessed_letters=set()

    while True:
        display_man(wrong_guesses)
        display_hint(hint)

        guess=input("Enter a letter: ").lower()

        if len(guess) != 1 or  not guess.isalpha():
            print("Please enter a letter:")
            continue

        if guess in guessed_letters:
            print("You have already guessed that: ")
            continue
        guessed_letters.add(guess)


        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

            if "_" not in hint:
                display_hint(hint)
                print("You won!")
                break

        else:
            wrong_guesses += 1

            if wrong_guesses == 6:
                display_man(wrong_guesses)
                print("You lost!")
                break



if __name__=="__main__":
    main()