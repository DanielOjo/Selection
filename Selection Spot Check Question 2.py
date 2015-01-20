#Daniel Ogunlana
#10-10-2014
#Selection Spot Check Question 2

first_name = input("Please enter you First name:")
last_name = input("Please enter your Last name:")
person_gender = input("Please enter your Gender e.g.(M for male or F for female):")
school_attendance = int(input("Please enter your Attendance percentage:"))

if person_gender == M:
    print("Mr {0} {1}".format(first_name,last_name))
elif person_gender == F:
    print("Mrs {0} {1}".format(first_name,last_name))
    
if school_attendance <=85:
    print("Your attendance is only {0}%. You must improve you attendance.".format(school_attendance))
elif school_attendance >=85:
    print("Your attendance is {0}%. Keep up the good attendance.".format(school_attendance))

