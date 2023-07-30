# 1
dir(str)

# 2
import random
dir(random)

# 3
import random
help(random.randint)
help(random.randrange)

# 4
import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# Print a random integer between 5 and 20 (Includes 5 and 20).

# What was the smallest number you could have seen, what was the largest?
# The smallest number that could be seen is 5.
# The largest number that could be seen is 20.

# What did you see on line 2?
# Print a random integer between 3 and 10 (Includes 3), stepping by 2.

# What was the smallest number you could have seen, what was the largest?
# The smallest number that could be seen is 3.
# The largest number that could be seen is 9.

# Could line 2 have produced a 4?
# No, line 2 can only produce odd numbers in the range.

# What did you see on line 3?
# Print a random floating-point number between 2.5 and 5.5.

# What was the smallest number you could have seen, what was the largest?
# The smallest number that could be seen is 2.5.
# The largest number that could be seen is 5.5.

# produce a random number between 1 and 100 inclusive.
import random
random_number = random.randint(1, 100)
print(random_number)




