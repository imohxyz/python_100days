import random
from day14_higherlower_art import logo, vs
from day14_higherlower_data import data

print(logo)

skor = 0
is_game_over = False
while not is_game_over:
    compare_a = data[random.randint(0, len(data))]
    compare_b = data[random.randint(0, len(data))]
    if compare_a == compare_b:
        compare_a = data[random.randint(0, len(data))]
        compare_b = data[random.randint(0, len(data))]
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    print(vs)
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    follower_a = compare_a['follower_count']
    follower_b = compare_b['follower_count']
    if answer == 'a':
        if follower_a > follower_b:
            skor += 1
            print(f"You're right! Current score: {skor}")
        else:
            print(f"Sorry, that's wrong. Final score: {skor}")
            is_game_over = True
    elif answer == 'b':
        if follower_b > follower_a:
            skor += 1
            print(f"You're right! Current score: {skor}")
        else:
            print(f"Sorry, that's wrong. Final score: {skor}")
            is_game_over = True
