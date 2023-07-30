"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
ValueError occurs if the user enters a non-integer value when prompted for the numerator or denominator.
2. When will a ZeroDivisionError occur?
If the user enters 0 as the denominator value, a ZeroDivisionError occurs.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
The possibility of a ZeroDivisionError can be avoided by adding a conditional check to ensure that the
denominator is not zero before performing the division. The user can be prompted to enter a new denominator
until a valid non-zero value is provided.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("The denominator cannot be zero.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Finished.")
