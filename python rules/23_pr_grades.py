marks = int(input("enter the marks: \n"))

if(marks<=100 and marks>90):
    print("You have grade EX")
elif(marks<=90 and marks>80):
    print("You have grade A")
elif(marks<=80 and marks>70):
    print("You have grade B")
elif(marks<=70 and marks>60):
    print("You have grade C")
elif(marks<=60 and marks>50):
    print("You have grade D")
else:
    print("you are fail")