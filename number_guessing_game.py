import random
computer_number = random.randint(1,100)

def compare_numbers(my_guess):
    my_guess = int(my_guess)
    if computer_number < my_guess:
        print('Your guess is too high. ')
    elif computer_number > my_guess:
        print('Your guess is too low. ')
    #else:
        #print(f'CONGRATULATIONS! You won! The computer guessed {computer_number}.')

numbers_dont_match = True

user_guess = int(input('Guess a number between 1 and 100. '))
print(f'You guessed {user_guess}.')

compare_numbers(user_guess)

while numbers_dont_match: 
    if user_guess != computer_number:
        print('You need to guess again.')
        new_user_guess = int(input('Guess a number between 1 and 100. ')) 
        user_guess = new_user_guess
        compare_numbers(new_user_guess)
        continue
    numbers_dont_match = False
    print(f'CONGRATULATIONS! You won! The computer guessed {computer_number}.')