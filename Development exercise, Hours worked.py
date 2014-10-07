#Daniel Ogunlana
#07-10-2014
#Development exercise, Hours worked

hours_worked = int(input("How many hours have you worked this week?:"))
pay_recived = int(input("How much money do you get paid per hour(£)?:"))

if hours_worked <=0 or hours_worked >=60:
    print("The number of hours worked is invaild")

elif hours_worked >=40:
    print(hours_worked*1.5*pay_recived) 

else: print("You will be paid £{0}".format(hours_worked*pay_recived))

