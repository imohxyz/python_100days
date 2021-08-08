import math

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

saldo = 0


def cek_isi(kopinya, harganya):
    global saldo
    komposisi = MENU[kopinya]['ingredients']
    biaya = MENU[kopinya]['cost']
    pemasukan = harganya / 100
    if resources['water'] < komposisi['water']:
        return 'Sorry there is not enough water'
    elif resources['milk'] < komposisi['milk']:
        return 'Sorry there is not enough milk'
    elif resources['coffee'] < komposisi['coffee']:
        return 'Sorry there is not enough coffee'
    if pemasukan < biaya:
        return 'Not enough money'
    elif pemasukan > biaya:
        KEMBALIAN = round(pemasukan - biaya, 2)
        saldo += biaya
        resources['water'] -= komposisi['water']
        resources['milk'] -= komposisi['milk']
        resources['coffee'] -= komposisi['coffee']
        return f"Here is your {kopinya}. Enjoy! \nHere is ${KEMBALIAN} in change."
    elif pemasukan == biaya:
        saldo += biaya
        resources['water'] -= komposisi['water']
        resources['milk'] -= komposisi['milk']
        resources['coffee'] -= komposisi['coffee']
        return f"Here is your {kopinya}. Enjoy!"


is_empty = False
while not is_empty:
    pilih_menu = input("What would you like? (espresso/latte/cappuccino): ")
    if pilih_menu == 'report':
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${saldo}")
    elif pilih_menu == 'latte' or pilih_menu == 'espresso' or pilih_menu == 'cappuccino':
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        uangnya = (quarters * 25) + (dimes * 10) + (nickles * 5) + pennies
        print(cek_isi(pilih_menu, uangnya))
