import random
orang = input('berikan nama nama, dipisahkan dengan tanda koma -> ')
nama = orang.split(', ')
total_data = len(nama)
bayar = nama[random.randint(0, total_data-1)]
print(f'yang bayar kali ini adalah : {bayar}')