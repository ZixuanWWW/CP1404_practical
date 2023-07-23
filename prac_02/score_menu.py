def main():
    MENU = """
    (G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit"""

    print(MENU)
    score = get_valid_score()
    choice = input(">>> ").upper()

    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = convert_to_result(score)
            print(f"Score: {score}, Result: {result}")
        elif choice == 'S':
            print('*' * int(score))
        else:
            print("Invalid")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you!")


def get_valid_score():
    score = float(input("Entry your score, between 0 and 100: "))
    while score < 0 or score > 100:
        print("Invalid score! Re-entry")
        score = float(input("Entry your score, between 0 and 100: "))
    return score

def convert_to_result(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"

    return result

main()
