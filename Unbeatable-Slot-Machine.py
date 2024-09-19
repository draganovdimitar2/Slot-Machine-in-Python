import random

def spin_reels_loss():
    symbols = ['🍒', '🍋', '🔔', '💎', '7️⃣', \
               '🍎', '🍍', '🍓', '🍇', '🍌', \
               '🥭', '🍐', '🥝', '🥥', '🍬',]
    
    passed_symbols = []
    
    first_row = []
    for _ in range(3):
        new_symbol = symbols[random.randint(0,14)]
        while new_symbol in passed_symbols:
            new_symbol = symbols[random.randint(0,14)]
        first_row.append(new_symbol)
        passed_symbols.append(new_symbol)
        
    second_row = []
    for _ in range(3):
        new_symbol = symbols[random.randint(0,14)]
        while new_symbol in passed_symbols:
            new_symbol = symbols[random.randint(0,14)]
        second_row.append(new_symbol)
        passed_symbols.append(new_symbol)
    
    third_row = []
    for _ in range(3):
        new_symbol = symbols[random.randint(0,14)]
        while new_symbol in passed_symbols:
            new_symbol = symbols[random.randint(0,14)]
        third_row.append(new_symbol)
        passed_symbols.append(new_symbol)
    
    return first_row, second_row, third_row

def win_check_loss(first_row, second_row, third_row):
    lines = 0  # adds 1 line when we have equal row/column or diagonal

    lines += 1 if first_row[0] == first_row[1] == first_row[2] else 0  # across the top
    lines += 1 if second_row[0] == second_row[1] == second_row[2] else 0  # across the middle
    lines += 1 if third_row[0] == third_row[1] == third_row[2] else 0  # across the bottom

    lines += 1 if first_row[0] == second_row[0] == third_row[0] else 0  # down the left side
    lines += 1 if first_row[1] == second_row[1] == third_row[1] else 0  # down the middle
    lines += 1 if first_row[2] == second_row[2] == third_row[2] else 0  # down the right side

    lines += 1 if first_row[0] == second_row[1] == third_row[2] else 0  # diagonal from top-left to bottom-right
    lines += 1 if first_row[2] == second_row[1] == third_row[0] else 0  # diagonal from top-right to bottom-left

    return lines


def ready_to_play(question):
    if question.startswith("y"):
        game_on = True  # when this is true we go to the main game loop
    else:
        game_on = False

    return game_on

# here starts the game logic ↓
print('Welcome to the slot machine')
game_on = ready_to_play(question=input('Are you ready to play? (press y or n)'))

while game_on:
    balance = int(input('Please choose starting balance:'))
    bet = int(input('Please choose your bet:'))

    while bet > balance:  # this loop will continue to iterate until our bet is <= balance
        bet = input('Invalid balance! Please choose your bet:')
    print(f'Your balance is {balance - bet}')
    balance -= bet

    while balance > 0:  # this nested while loop will repeat until your balance is equal or less than 0
        spin_reels_loss
        first_row, second_row, third_row = spin_reels_loss()
        print(first_row)  # printing the first row
        print(second_row)  # printing the second row
        print(third_row)  # printing the third row
        lines = win_check_loss(first_row, second_row, third_row)

        if lines > 0:  # winning case
            print(
                f'Congratulations! You win {lines * bet}!\n'
                f'Your current balance is: {balance}!'
            )
            balance += bet + (bet * lines)  # this will add your current bet plus lines multiplied by your bet

        else:  # losing case
            print(
                f'Better luck next time!\n'
                f'Your current balance is {balance}!'
            )

        bet = int(input('Please choose your bet:'))
        balance -= bet

    if balance <= 0:  # if we run out of money we enter the body of this condition
        print("You don't have enough money!")
        question = ready_to_play(input('Do you want to play again?'))

        if question:  # if we want to play again
            continue

        else:  # if we want to quit the game
            game_on = False  # this sets the flag variable to false so we can bryeak the main loop later
            break  # this breaks inner (nested) loop

    if not game_on:  # we break main loop here and game ends
        break

print('Game over!')