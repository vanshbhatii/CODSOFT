# Simple Calculator
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
#Choose operation
print("+ Addition")
print("- subtraction")
print("* multiplication")
print("/ division")
operation = input("Enter operation:")
if operation == '+':
    print("Result:",a+b)
elif operation =='-':
    print("Result:",a-b)
elif operation =='*':
    print("Result:",a*b)
elif operation =='/':
    print("Result:",a/b)
else:
    print("Invalid Operation Found")
