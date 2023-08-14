
year = int(input("Which year do you want to check? "))

l=0
if year % 4 == 0 :
    l=l+1
    if year % 100 == 0 :
        l=l-1
        if year % 400 == 0:
            l = l+1
if l >= 1 :
    print("Leap year.")
else:
    print("Not leap year.")            
