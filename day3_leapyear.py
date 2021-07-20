tahun = int(input('tahun berapa yang ingin di cek: '))
kabisat = 0
if tahun % 4 == 0:
    kabisat += 1
    if tahun % 100 == 0:
        kabisat -= 1
        if tahun % 400 == 0:
            print('tahun kabisat')
            kabisat += 1
        else:
            print('bukan tahun kabisat')
            kabisat -= 1
    else:
        print('tahun kabisat')
        kabisat += 1
else:
    print('bukan tahun kabisat')
    kabisat -= 1
# cek kabisat
if kabisat >= 2:
    print(f'{tahun} adalah tahun kabisat')
else:
    print(f'{tahun} bukan tahun kabisat')