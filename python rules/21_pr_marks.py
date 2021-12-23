sub1 = int(input("Enter marks of sub1: "))
sub2 = int(input("Enter marks of sub2: "))
sub3 = int(input("Enter marks of sub3: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail")
elif(sub1+sub2+sub3)/3 <40:
    print("you are not pass")
else:
    print("you are pass")
   