size = input('Masukkan ukuran pizza : S, M or L -> ')
add_pepperoni = input('Mau tambah pepperoni? Y or N -> ')
extra_cheese = input('Mau tambah extra keju? Y or N -> ')
total = 0
if size == 's' or size == 'S':
    total = 20000
    print('harga pizza S : Rp. 20000')
elif size == 'm' or size == 'M':
    total = 35000
    print('harga pizza M : Rp. 35000')
elif size == 'l' or size == 'L':
    total = 50000
    print('harga pizza L : Rp. 50000')
else:
    print('ukuran pizza tidak ada di list')

if add_pepperoni == 'Y' or add_pepperoni == 'y':
    total += 5000
    print('harga tambah pepperoni : Rp. 5000')

if extra_cheese == 'Y' or extra_cheese == 'y':
    total += 10000
    print('harga extra keju : Rp. 10000')

print(f'Total yang harus dibayar adalah : Rp. {total}')