import sys
from random import randint

# ANSI color codes
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[34m"


def main():
    if len(sys.argv) == 1:
        # Quick mode
        min_val = randint(1, 50)
        max_val = randint(51, 100)
        answer = randint(min_val, max_val)
    elif len(sys.argv) == 3:
        # Custom range mode
        try:
            min_val = int(sys.argv[1])
            max_val = int(sys.argv[2])
            if min_val >= max_val:
                print('The minimum value must be smaller than the maximum value.')
                return False

            answer = randint(min_val, max_val)
        except ValueError:
            print(f'{RED}The provided arguments are not valid numbers.{RESET}')
            return False
    else:
        # Invalid usage
        print('Usage:')
        print(
            f'{BLUE}  python guess.py <min> <max>{RESET}  ➡  play with a custom range')
        print(
            f'{BLUE}  python guess.py{RESET}              ➡  play in quick mode (1-100)')
        return False

    print(
        f'I\'m thinking of a number between {BLUE}{min_val}{RESET} and {BLUE}{max_val}{RESET}.')
    print('Type "exit" to quit the game at any time.\n')

    tries = 0

    while True:
        print(BLUE, end='')  # set typing color to blue
        guess_input = input('Guess the number: ').strip()
        print(RESET, end='')  # reset color after typing

        if guess_input.lower() == 'exit':
            print('Thanks for playing! 👋\nGoodbye!')
            return False

        try:
            guess = int(guess_input)
        except ValueError:
            print(f'{RED}Please enter a valid whole number.{RESET}')
            continue

        tries += 1
        if guess == answer:
            attempt_word = 'try' if tries == 1 else 'tries'
            print(
                f'{GREEN}You guessed it after {tries} {attempt_word}! 🎉')
            print(f'The secret number was {answer}.\n{RESET}')
            play_again_input = input(
                'Do you want to play again? (y/n): ').strip().lower()
            if play_again_input not in ('yes', 'y'):
                print('Thanks for playing! 👋')
                return False
            return True
        elif guess < answer:
            print(f'{RED}Too low{RESET} - try again!\n')
        else:
            print(f'{RED}Too high{RESET} - try again!\n')


if __name__ == '__main__':
    while True:
        print()
        play_again = main()
        if not play_again:
            break
