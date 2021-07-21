student_scores = input("Input a list of student scores ").split()
# cara cepet dapetin value max
# print(max(student_scores))
# cara pake for
maks = 0
for i in student_scores:
    if int(i) > int(maks):
        maks = i
print(f'skor tertinggi adalah : {maks}')