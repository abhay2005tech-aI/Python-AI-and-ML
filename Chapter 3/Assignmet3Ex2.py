""" Write a Python program that takes any word or sentence as input and prints: ● The first character 
● The last character 
● The total number of characters
"""
word = input("Enter a word or sentence: ")
first_character = word[0]
last_character = word[-1]
total_characters = len(word)
print("First character :", first_character)
print("Last character :", last_character)
print("Total number of characters :", total_characters)