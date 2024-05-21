from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
scontinue = True

while scontinue:
    directio_n = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26

    def ceaser(plain_text, shift_amount, direction):
        end_text= ""
        if direction== "decode":
                shift_amount*= -1
        for letters in plain_text:
            if letters in alphabet:
             position = alphabet.index(letters)
             new_position = position + shift_amount
             end_text += alphabet[new_position]
            else:
                end_text +=letters
        print(f"Here's the {directio_n}d result: {end_text}")

    ceaser(plain_text=text,shift_amount=shift,direction=directio_n)
    result = input("Tye 'yes' if you want to continue. Otherwise 'No' \n").lower()
    if result=="no":
        scontinue = False
        print("Good Bye")

