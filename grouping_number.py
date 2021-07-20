import sys
angka = [1,2,3,22,25,26,5,7,8,10,13,46,49,34,35,37,31,32,21,27,30,15,17,18,43,45,33,39,40,42,52,53,55,61,62,
         77,75,88,82,98,87,92,102,103,89,117,104,118,191,189,192]
bb = 0
ba = 10
dd = max(b for b in angka)
for i in range(bb, dd):
    cici = sum(a < ba and a >= bb for a in angka)
    print(f'angka {bb} s/d {ba}: {cici}')
    bb += 10
    if ba > dd:
        ba = dd
        sys.exit()
    else:
        ba += 10
        i += 1


# bb = 0
# ba = 10
# for i in range(bb, ba):
#     cici = sum(a < ba and a >= bb for a in angka)
#     print(f'angka {bb} s/d {ba}: {cici}')
#     bb += 10
#     ba += 10
#     i += 1


# angka_10 = sum(i < 10 for i in angka)
# print(f'angka kurang dari 10: {angka_10}')
# angka_20 = sum(i >= 10 and i < 20 for i in angka)
# print(f'angka kurang dari 20: {angka_20}')
# angka_30 = sum(i > 20 and i < 30 for i in angka)
# print(f'angka kurang dari 30: {angka_30}')
# angka_40 = sum(i > 30 and i <= 40 for i in angka)
# print(f'angka kurang dari 40: {angka_40}')
# angka_50 = sum(i >= 40 and i <= 50 for i in angka)
# print(f'angka kurang dari 50: {angka_50}')
# total_angka = len(angka) + 2
# print(f'total angka: {total_angka}')
