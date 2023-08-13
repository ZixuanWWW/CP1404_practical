"""
CP1404 Practical
Complete prac 5 word occurrences exercise
"""

count_of_word = {}
text = input("Text: ")
#  Text: this is a collection of words of nice words this is a fun thing it is
words = text.split()
for word in words:
    frequency = count_of_word.get(word, 0)
    count_of_word[word] = frequency + 1

words = list(count_of_word.keys())
words.sort()

maximum_length = max(len(word) for word in words)
for word in words:
    print(f"{word:{maximum_length}} : {count_of_word[word]}")
