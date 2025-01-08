def number(num1, num2, num3, num4, num5):
   
    numbers = []
    numbers.append(int(input(f" Enter  number {num1}: ")))
    numbers.append(int(input(f" Enter  number {num2}: ")))
    numbers.append(int(input(f"Enter  number {num3}: ")))
    numbers.append(int(input(f"Enter  number {num4}: ")))
    numbers.append(int(input(f"Enter  number{num5}: ")))

  
    return numbers


result = number('Fist', 'Second', 'third', 'fourth', 'fifth')
print("Your numbers:", result)
