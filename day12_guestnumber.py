import random

nomornya = random.randint(1, 100)
print(nomornya)
lives = 0
levels = input('Select level hard or easy -> ').lower()
if levels == 'hard':
    print('Your life is 5')
    lives = 5
elif levels == 'easy':
    print('Your life is 10')
    lives = 10
is_game_over = False
while not is_game_over:
    nomor = int(input('Guess the number in range 1-100? '))
    if nomor > nomornya:
        print('Too High')
        lives -= 1
    elif nomor < nomornya:
        print('Too Low')
        lives -= 1
    elif nomor == nomornya:
        print('You Won')
        is_game_over = True
    if lives == 0:
        print('Too Many Guest, Game Over')
        is_game_over = True