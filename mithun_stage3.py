name,mark1, mark2, mark3 = input().split(',')
total = int(mark1) + int(mark2) + int(mark3)
percentage = (total / 300) * 100

if percentage >= 75:
    grade = 'A'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 40:
    grade = 'C'
else:
    grade = 'F'

print(name)
print(f"Total: {total}/300")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
