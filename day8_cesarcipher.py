from day8_cesarcipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)


def caesar(text, shift, direction):
    enkripsi = ''
    for kata in text:
        if kata in alphabet:
            katanya = alphabet.index(kata)
            if direction == 'encode':
                posisi_baru = (katanya + shift)
                if posisi_baru > len(alphabet):
                    katanya = posisi_baru - len(alphabet)
                else:
                    katanya = posisi_baru
            elif direction == 'decode':
                posisi_baru = (katanya - shift)
                katanya = posisi_baru
            enkripsi += alphabet[katanya]
        else:
            enkripsi += kata
    print(f'The {direction} text is {enkripsi}')

lanjut_lagi = True
while lanjut_lagi:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, direction)
    lanjut = input("Run again? 'y' or 'n' -> ")
    if lanjut == 'n':
        lanjut_lagi = False
    elif lanjut == 'y':
        lanjut_lagi = True
    else:
        lanjut_lagi = False
        print('Invalid command')

# def encrypt(text, shift):
#     enkripsi = ''
#     for kata in text:
#         katanya = alphabet.index(kata)
#         posisi_baru = (katanya + shift)
#         if posisi_baru > len(alphabet):
#             katanya = posisi_baru - len(alphabet)
#         else:
#             katanya = posisi_baru
#         enkripsi += alphabet[katanya]
#     print(f'The encoded text is {enkripsi}')
#
#
# def decrypt(text, shift):
#     dekripsi = ''
#     for kata in text:
#         katanya = alphabet.index(kata)
#         posisi_baru = (katanya - shift)
#         katanya = posisi_baru
#         dekripsi += alphabet[katanya]
#     print(f'The decoded text is {dekripsi}')
#
#
# if direction == 'encrypt':
#     encrypt(text, shift)
# elif direction == 'decrypt':
#     decrypt(text, shift)
# else:
#     print('Unknown command!')
