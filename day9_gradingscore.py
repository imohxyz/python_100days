student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
for nama in student_scores:
    if student_scores[nama] > 90 and student_scores[nama] < 100:
        student_grades[nama] = 'Outstanding'
    elif student_scores[nama] > 80 and student_scores[nama] < 90:
        student_grades[nama] = 'Exceeds Expetations'
    elif student_scores[nama] > 70 and student_scores[nama] < 80:
        student_grades[nama] = 'Acceptable'
    elif student_scores[nama] <= 70:
        student_grades[nama] = 'Fail'

print(student_grades)