"""
3
2
1
[3, 2, 4, 1, 5, 9]
[1]
True
False
False
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

# 1
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0] = 'ten'
print(numbers)

# 2
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[-1] = 1
print(numbers)

# 3
numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[2:])

# 4
numbers = [3, 1, 4, 1, 5, 9, 2]
print(9 in numbers)
