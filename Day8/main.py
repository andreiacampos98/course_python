alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    new_text=""
    for letter in text: 
        index = alphabet.index(letter)
        new_index = index + shift
        if new_index > 25:
            new_index = new_index -26
        new_text += alphabet[new_index]
    print(new_text)
    return(new_text)

def decrypt(text, shift):
    new_text=""
    for letter in text: 
        index = alphabet.index(letter)
        new_index = index + 1 - shift
        if new_index < 0:
            new_index = 25 + new_index 
        print(index, letter, new_index )
        new_text += alphabet[new_index]
    print(new_text)
    return(new_text)

def main():
    direction = input("Type 'encode to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    if direction=='encode':
        encrypt(text, shift)
    elif direction=='decode':
        decrypt(text, shift)
    else:
        print("Please type 'encode' or 'decode'")

main()