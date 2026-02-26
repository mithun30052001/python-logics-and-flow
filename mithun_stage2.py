num1,num2,operator = input().split()
result = None
if operator == '+':
    result = int(num1) + int(num2)
elif operator == '-':
    result = abs(int(num1) - int(num2))
elif operator == '*':
    result = int(num1) * int(num2)
elif operator == '/':
    if int(num2) == 0:
        result="Error: Division by zero"
    else: 
        result = int(num1) / int(num2)

print("Result=" + str(result))
if type(result) == int or type(result) == float:
    if result > 0:
        print("Positive")
    elif result < 0:
        print("Negative")
    else:
        print("Zero")
