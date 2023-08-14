#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to bill calc.")
Total_bill = float(input("what is the total bill :"))
tip_percentage = int(input("what percentage of tip do u want to pay 10 , 12 or 15 :"))
homies = int(input("how many people to split that bill :"))
each_one = (Total_bill+(tip_percentage/100)*Total_bill)/homies
#each_one = round(each_one , 2)
formated_bill="{:.2f}".format(each_one)   ## two decimal including zero  150 12 5  
print(formated_bill)