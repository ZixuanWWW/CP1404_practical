import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

def main():
    times_of_pick = int(input("How many quick picks? "))

    for i in range(1, times_of_pick + 1):
        quick_picks = []
        while len(quick_picks) < NUMBERS_PER_LINE:
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            if random_number not in quick_picks:
                quick_picks.append(random_number)
        quick_picks.sort()
        for number in quick_picks:
            print(f"{number:2}", end=" ")
        print("\n")

main()
