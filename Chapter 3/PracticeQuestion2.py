#Write a program that takes your favorite food name as input and prints: ● The middle 3 characters 
#● The last 2 characters 
food = input("Enter Your Favorite Food Name:")
middle_3 = food[1:4]
last_2 = food[-2:]
print("Middle 3 characters:", middle_3)
print("Last 2 characters:", last_2)