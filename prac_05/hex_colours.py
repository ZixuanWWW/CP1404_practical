"""
CP1404 Practical
Complete prac 5 hex colours exercise
"""

COLOUR_CODES = {"aliceblue": "#f0f8ff", "amaranth": "#e52b50", "amber": "#ffbf00",
                "amethyst": "#9966cc", "antiqueWhite": "#faebd7", "antiquewhite1":
                "#ffefdb", "antiquewhite2": "#eedfcc", "antiquewhite3": "#cdc0b0",
                "antiquewhite4": "#8b8378", "apricot": "#fbceb1"}

colour_name = input("Enter a colour name: ").lower()  # Convert input to lowercase
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()  # Convert input to lowercase
