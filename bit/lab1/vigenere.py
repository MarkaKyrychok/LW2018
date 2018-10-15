from string import ascii_letters


def encrypt(plaintext, key_phrase):
    ciphertext = ''
    i = 0
    keys = [ascii_letters.index(key_char) for key_char in key_phrase]
    for char in plaintext:
        if char not in ascii_letters:
            ciphertext += char
            continue
        key = keys[i]
        i = (i + 1) % len(key_phrase)
        ciphertext += ascii_letters[(ascii_letters.index(char) + key) % len(ascii_letters)]
    return ciphertext


def decrypt(cipher_text, key_phrase):
    text = ''
    i = 0
    keys = [ascii_letters.index(key_char) for key_char in key_phrase]
    for char in cipher_text:
        if char not in ascii_letters:
            text += char
            continue
        key = keys[i]
        i = (i + 1) % len(key_phrase)
        text += ascii_letters[(ascii_letters.index(char) - key + len(ascii_letters)) % len(ascii_letters)]
    return text
