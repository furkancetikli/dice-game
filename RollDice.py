import random

def roll_dice(num_dice):
    total_rolls = 0
    for _ in range(num_dice):
        die = random.randint(1, 6)
        print(f'({die})', end=" ")
        total_rolls += 1
    print()  # New Line / Yeni Satır
    return total_rolls

def main():
    total_rolls = 0
    while True:
        choice = input('Roll the dice? (y/n): ').lower()
        if choice == 'y':
            try:
                num_dice = int(input('How many dice would you like to roll? '))
                if num_dice <= 0:
                    print("Please enter a positive number.")
                    continue
                total_rolls += roll_dice(num_dice)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == 'n':
            print("\nThanks for playing!")
            print(f"You rolled the dice {total_rolls} times in total.")
            break
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
