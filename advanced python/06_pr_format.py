name = input("Enter your name: ")
marks = input("Enter your number: ")
phoneNumber = input("Enter your phone number: ")

template = "The name of the student is {} and his marks are {} and his phone number is {}."
output = template.format(name, marks, phoneNumber)
print(output)