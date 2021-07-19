print('selamat datang di pulau harta karun')
jalan = input('Posisi kamu sekarang ada di antara dua jalan. jalan mana yang kamu pilih? kiri atau kanan? -> ').lower()
print(jalan)
if jalan == 'kiri' or jalan == 'KIRI':
    print('game over!')
elif jalan == 'kanan' or jalan == 'KANAN':
    sungai = input('Kamu sampai di sungai, ditengah tengah sungai ada sebuah pulau. ketik S untuk berenang atau ketik T'
                   ' untuk menunggu perahu datang -> ').lower()
    print(sungai)
    if sungai == 't' or sungai == 'T':
        print('game over!')
    elif sungai == 's' or sungai == 'S':
        pulau = input(
            'Kamu sampai di pulau. Disana ada 3 pintu, pintu mana yang kamu pilih? kuning, merah atau hijau? -> ').lower()
        print(pulau)
        if (pulau == 'kuning' or pulau == 'KUNING') or (pulau == 'merah' or pulau == 'MERAH'):
            print('game over!')
        elif pulau == 'hijau' or pulau == 'HIJAU':
            print('Selamat kamu mendapatkan harta karun senilai 1 milyar rupiah')
        else:
            print('pintu tidak ada di list')
    else:
        print('aksi tidak ada di list')
else:
    print('jalan tidak ada di list')
