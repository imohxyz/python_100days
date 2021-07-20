import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('------------Game Gunting Batu Kertas------------')
pemain = int(input('Batu = 0, Kertas = 1, Gunting = 2 -> '))
bot = random.randint(0, 2)
pilihan = [rock, paper, scissors]
nama_pilihan = ['Batu', 'Kertas', 'Gunting']
print(f'Pemain pilih : {nama_pilihan[pemain]}\n{pilihan[pemain]}')
print(f'Komputer pilih : {nama_pilihan[bot]}\n{pilihan[bot]}')

if (pemain == 0 and bot == 2) or (pemain == 1 and bot == 0) or (pemain == 2 and bot == 1):
    print('Pemain Menang')
elif (bot == 0 and pemain == 2) or (bot == 1 and pemain == 0) or (bot == 2 and pemain == 1):
    print('Komputer Menang')
elif pemain == bot:
    print('Seri')
else:
    print('Input tidak ditemukan di list')