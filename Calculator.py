import math

intro = str="Welcome to Nishanth's Calculator"
print(intro)

int1 = input("Enter first number:")
int2 = input("Enter second number:")
operator = input("Enter operator(add, subtract, multiply, Divide, Square root, power, percentage)").lower

if operator == "add"or "Add"or"ADD":
    sum = float(int1) + float(int2)
    print(sum)
elif operator == "subtract"or "Subtract"or "SUBTRACT":
    sum = float(int1) - float(int2)
    print(sum)
elif operator == "multiply"or "Multiply"or"MULTIPLY":
    sum = float(int1) * float(int2)
    print(sum)
elif operator == "Divide"or"divide"or "DIVIDE":
    sum = float(int1) / float(int2)
    print(sum)
elif operator == "square root":
    sum = math.sqrt(float(int1))
    print(sum)
elif operator == "power"or"Power"or"POWER":
    sum = math.pow(float(int1), float(int2))
    print(sum)
elif operator == "percentage"or"Percentage"or"PERCENTAGE":
    sum = float(int1) / float(int2) *100
    print(sum)       
else:
    print("Invalid") 
    print("")   
