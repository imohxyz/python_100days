from day10_calculator_art import logo

print(logo)


def hitung(b1, b2, aksinya):
    if aksinya == '+':
        return b1 + b2
    elif aksinya == '-':
        return b1 - b2
    elif aksinya == 'x':
        return b1 * b2
    elif aksinya == '/':
        return b1 / b2
    else:
        return 'Aksi tidak ditemukan'


selesai = False
while not selesai:
    n1 = float(input('Input bilangan 1? '))
    n2 = float(input('Input bilangan 2? '))
    aksi = input('Pilih aksi -> (+) (-) (x) (/)\n')
    hasil = hitung(n1, n2, aksi)
    print(f"Hasil dari {n1} {aksi} {n2} = {hasil}")
    lanjut = input("Hitung lagi? 'y' or 'n' -> ")
    if lanjut == 'n':
        selesai = True
    elif lanjut == 'y':
        selesai = False
    else:
        selesai = True
        print('Invalid command')