nama1 = input('Masukkan nama kamu : \n').lower()
nama2 = input('Masukkan nama dia : \n').lower()
kombinasi = nama1 + nama2
t = kombinasi.count('t')
r = kombinasi.count('r')
u = kombinasi.count('u')
e = kombinasi.count('e')
l = kombinasi.count('l')
o = kombinasi.count('o')
v = kombinasi.count('v')
e = kombinasi.count('e')
total1 = t + r + u + e
total2 = l + o + v + e
total = str(total1) + str(total2)
if int(total) <= 10 or int(total) >= 90:
    print(f'presentasi love kamu : {total}%, kamu selalu bersama seperti coke dan mentos')
elif int(total) >= 40 and int(total) <= 50:
    print(f'presentasi love kamu : {total}%, kamu sudah pantas bersama')
else:
    print(f'presentasi love kamu : {total}%')