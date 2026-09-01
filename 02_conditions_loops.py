# Module 1 - Conditions and Loops

marks = 78

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print("Marks:", marks)
print("Grade:", grade)

print("\nFor loop:")
for i in range(1, 6):
    print(i)

print("\nWhile loop:")
count = 1
while count <= 5:
    print(count)
    count += 1
