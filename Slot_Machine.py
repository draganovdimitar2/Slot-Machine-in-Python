import random

def spin_reels():
    symbols = ['🍒', '🍋', '🔔', '💎', '7️⃣', \
               '🍎', '🍍', '🍓', '🍇', '🍌']
    reels = [[random.choice(symbols) for _ in range(3)],  # this prints 3 random symbols which will be our first row
             [random.choice(symbols) for _ in range(3)],  # this prints 3 random symbols which will be our second row
             [random.choice(symbols) for _ in range(3)]]  # this prints 3 random symbols which will be our third row
    return reels

def win_check(reels):
    lines = 0  # adds 1 line when we have equal row/column or diagonal

    lines += 1 if reels[0][0] == reels[0][1] == reels[0][2] else 0  # across the top
    lines += 1 if reels[1][0] == reels[1][1] == reels[1][2] else 0  # across the middle
    lines += 1 if reels[2][0] == reels[2][1] == reels[2][2] else 0  # across the bottom

    lines += 1 if reels[0][0] == reels[1][0] == reels[2][0] else 0  # down the left side
    lines += 1 if reels[0][1] == reels[1][1] == reels[2][1] else 0  # down the middle
    lines += 1 if reels[0][2] == reels[1][2] == reels[2][2] else 0  # down the right side

    lines += 1 if reels[0][0] == reels[1][1] == reels[2][2] else 0  # diagonal from top-left to bottom-right
    lines += 1 if reels[0][2] == reels[1][1] == reels[2][0] else 0  # diagonal from top-right to bottom-left

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
        spin_reels()
        reels = spin_reels()
        print(reels[0])  # printing the first row
        print(reels[1])  # printing the second row
        print(reels[2])  # printing the third row
        lines = win_check(reels)

        if lines > 0:  # winning case
            print(
                f'Congratulations! You win {winnings}!\n'
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
            game_on = False  # this sets the flag variable to false so we can break the main loop later
            break  # this breaks inner (nested) loop

    if not game_on:  # we break main loop here and game ends
        break

print('Game over!')
