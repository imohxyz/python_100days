tinggi = float(input('masukkan tinggi cm: '))
berat = float(input('masukkan berat kg: '))
bmi = round(berat / ((tinggi / 100) ** 2), 2)
print(bmi)
if bmi < 17:
    print('gizi buruk')
elif bmi > 17 and bmi <= 18.5:
    print('kurus')
elif bmi > 18.5 and bmi <= 25:
    print('normal')
elif bmi > 25 and bmi <= 27:
    print('gemuk')
else:
    print('obesitas')