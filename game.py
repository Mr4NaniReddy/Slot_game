import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_values = {
    "A": 5,
    "B": 4,
    "C": 4,
    "D": 2
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_counts in symbols.items():
        for _ in range(symbol_counts):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines


def deposit():
    while True:
        amount = input("What would you like to deposit ?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("Enter valid lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        bet = input("Enter the bet amount? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ({MIN_BET}-{MAX_BET}).")
        else:
            print("Please enter a number.")

    return bet


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total = lines * bet
        if total > balance:
            print(f"Insufficient balance. Your current balance is {balance}.")
        else:
            break
    print(f"you are betting {bet} on {lines} lines. Total bet is {total}.")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won {winnings}.")
    print(f"You won on lines: ", *winnings_lines)
    return winnings - total


def main():
    balance = deposit()
    while True:
        print(f"Current balance is {balance}")
        play = input("Press enter to play (q to quit):")
        if play == "q":
            break
        balance += spin(balance)


main()
