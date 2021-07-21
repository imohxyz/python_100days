student_heights = input("Input a list of student heights ").split()
total = 0
for n in range(0, len(student_heights)):
    total += int(student_heights[n])
rata = round(total / len(student_heights))
print(rata)