"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
MIN_BONUS = 0.1
MAX_BONUS = 0.15
MIN_SALES = 0
EDGE_SALES = 1000
sales = float(input("Enter sales: $"))
while sales >= MIN_SALES:
    if sales < EDGE_SALES:
        bonus = sales * MIN_BONUS
    else:
        bonus = sales * MAX_BONUS
    print(f"Bonus: ${bonus}")
    sales = float(input("Enter sales: $"))
