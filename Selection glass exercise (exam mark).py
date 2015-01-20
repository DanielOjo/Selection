#Daniel Ogunlana
#09-10-2014
#Selection glass exercise (exam mark)

exam_mark = int(input("Please enter your exam mark?:"))
if exam_mark <0 or exam_mark <=40:
    print("Your grade is U")
elif exam_mark ==41 or exam_mark <=50:
    print("Your grade is E")
elif exam_mark ==51 or exam_mark <=60:
    print("Your grade is D")
elif exam_mark ==61 or exam_mark <=70:
    print("Your grade is C")
elif exam_mark ==71 or exam_mark <=80:
    print("Your grade is B")
elif exam_mark ==81 or exam_mark <=100:
    print("Your grade is A")
