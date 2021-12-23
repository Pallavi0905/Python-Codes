from typing import Mapping


try:
    a = int(input("Enter the number: "))
    b = 1/a
    print(b)
except Exception as e:
    print("Exception occured")
    print(e)

print("thanks for using my code!")