# day 2 project calculator tips
total = float(input('berapa jumlah total tagihan? Rp.'))
tip = float(input('berapa persen kasih tips nya? '))
qty = int(input('berapa orang? '))
hasil1 = (total * (tip / 100)) + total
hasil2 = hasil1 / qty
hasil = round(hasil2, 2)
hasil = "{:.2f}".format(hasil2)
print(f'tiap orang harus bayar : Rp.{hasil}')