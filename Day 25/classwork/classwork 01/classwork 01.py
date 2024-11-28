num1 = float(input("first number: "))
num2 = float(input("second number: "))
goa = input("operators (+, -, *, /): ")

if goa == "+":
    print(num1 + num2)
elif goa == "-":
    print(num1 - num2)
elif goa == "*":
    print(num1 * num2)
elif goa == "/":
    if num2 != 0:
        print(num1 / num2)
    

  
