# Import the random module here
import random as rd
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
x=len(names)
random_selection = rd.randint(0,x)
print(f"{names[random_selection]} is going to buy the meal today!")
