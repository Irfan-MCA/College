# a. Generate positive list of numbers from a given list of integers
numbers = [-5, 3, -1, 0, 7, -9, 2]
positive_numbers = [num for num in numbers if num > 0]
print("a. Positive numbers:", positive_numbers)

# b. Square of N numbers
N = 5
squares = [x**2 for x in range(1, N+1)]
print("b. Squares of first", N, "numbers:", squares)

# c. Form a list of vowels selected from a given word
word = "ListComprehension"
vowels = [char for char in word if char.lower() in 'aeiou']
print("c. Vowels in the word:", vowels)

# d. List ordinal value of each element of a word
word2 = "Hello"
ordinals = [ord(char) for char in word2]
print("d. Ordinal values of characters in the word:", ordinals)
