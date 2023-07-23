import random

def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    user_score = float(input("Enter score: "))
    result = get_result(user_score)
    print(f"Result: {result}")

    random_score = random.randint(0, 101)
    result = get_result(random_score)
    print(f"Random score: {random_score}, Result: {result}")

main()
