"""1. Write a program that takes a sentence and prints: 
● Total characters (len()) 
● Uppercase version 
● Lowercase version """
sentence = input("Enter a sentence: ")
total_characters = len(sentence)
uppercase_version = sentence.upper()
lowercase_version = sentence.lower()
print("Total characters:", total_characters)
print("Uppercase version:", uppercase_version)
print("Lowercase version:", lowercase_version)