#Write a Python program that takes a user’s name as input and prints: 1. The first character 
#2. The last character 
#3. The total length of the name 
name = input("Enter your name: ")
print("First character: ", name[0])
print("Last character: ", name[-1])
print("Total length of the name: ", len(name))