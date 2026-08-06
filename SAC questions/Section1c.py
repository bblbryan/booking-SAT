row1 = [None, None, None]
row2 = [None, None, None]
row3 = [None, None, None]
num = eval(input("Input a number between 1 and 9 inclusive:"))
if num < 1 or num > 9:
    print("Invalid input!")
else:
    row = eval(input("What row do you want this number to be?"))

if row == 2:
    row2.append(num)
elif row == 3:
    row3.append(num)
else: 
    row1.append(num)   

