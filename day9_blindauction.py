from day9_blindauction_art import logo

print(logo)
semua_bid = {}


def max_bid():
    bid_tinggi = 0
    namanya = ""
    for bidder in semua_bid:
        bid_nilai = semua_bid[bidder]
        if int(bid_nilai) > int(bid_tinggi):
            bid_tinggi = bid_nilai
            namanya = bidder
    print(f"bid tertinggi jatuh ke tangan {namanya} di harga ${bid_tinggi}")


bidding_finished = False
while not bidding_finished:
    nama = input('What is your name? ')
    bid = int(input('What is your bid? $'))
    semua_bid[nama] = bid
    lanjut = input("Run again? 'y' or 'n' -> ")
    if lanjut == 'n':
        bidding_finished = True
        max_bid()
    elif lanjut == 'y':
        bidding_finished = False
    else:
        bidding_finished = True
        print('Invalid command')