while(True):
    print("Press q to quit")
    a = input("Enter the number")
    if a == 'q':
        break
    try:
        print("Trying.....")
        a = int(a)
        if a>6:
            print("You entered the no. greater than 6")
    except Exception as e:
        print(f"Your input resulted an error:- {e}")

print("Thanks for playing")