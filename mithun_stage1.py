num1,num2,operator = input().split()
if operator == '+':
    print("Result=" + str(int(num1)+int(num2)))
elif operator == '-':
    print("Result=" + str(abs(int(num1)-int(num2))))
elif operator == '*':
    print("Result=" + str(int(num1)*int(num2)))
elif operator == '/':
    if int(num2) == 0:
        print("Error: Division by zero")
    else:
        print("Result=" + str(int(num1)/int(num2)))
