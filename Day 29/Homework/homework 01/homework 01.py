def calculate_bmi(weight, height):

    bmi = weight / (height ** 2)
    
  
    if bmi < 18.5:
       print("Low weight")
    elif 18.5 <= bmi < 24.9:
        print("Normal weight")
    elif 25 <= bmi < 29.9:
        print("Hight weight")
    
    print(bmi)
   
Weight = int(input("Enter your weight: "))
Height = int(input("Enter your height: "))


calculate_bmi(Weight,Height)
