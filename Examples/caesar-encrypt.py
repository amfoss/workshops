import sys


def caesar_encrypt(input_message, key):
    if not 0 < key <= 26:
        print('Key should be number between 1 and 26')
        sys.exit()

    output = ''

    for letter in input_message:
        # add the key to the letter
        new_letter_ascii = ord(letter) + key

        if letter.isupper():
            if new_letter_ascii > ord('Z'):
                new_letter_ascii = new_letter_ascii - 26
        else:
            if new_letter_ascii > ord('z'):
                new_letter_ascii = new_letter_ascii - 26

        new_letter = chr(new_letter_ascii)

        output = output + new_letter

    return output


def caesar_decrypt(encrypted_message, key):
    if not 0 < key <= 26:
        print('Key should be number between 1 and 26')
        sys.exit()

    original_message = ''

    for letter in encrypted_message:
        # subtract the key to get the original message
        new_letter_ascii = ord(letter) - key

        if letter.isupper():
            if new_letter_ascii < ord('A'):
                new_letter_ascii = new_letter_ascii + 26
        else:
            if new_letter_ascii < ord('a'):
                new_letter_ascii = new_letter_ascii + 26

        new_letter = chr(new_letter_ascii)

        original_message = original_message + new_letter

    return original_message


if __name__ == '__main__':
    message = input('Enter a message: ')
    key = int(input('Enter a key: '))
    type = input('E/D - Encrypt or decrypt')

    if type == "E":
        e = caesar_encrypt(message, key)
        print(e)
    elif type == "D":
        d = caesar_decrypt(message, key)
        print(d)
    else:
        print("Enter a valid option")