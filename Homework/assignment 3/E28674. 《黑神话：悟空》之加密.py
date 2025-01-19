k = int(input())
s = input()

decrypted_test = ""
for letter in s:
    if 'a' <= letter <= 'z':
        new_letter = chr((ord(letter)- ord('a')-k) % 26 + ord('a'))
    elif 'A' <= letter <= 'Z':
        new_letter = chr((ord(letter)- ord('A')-k) % 26 + ord('A'))
    else:
        new_letter = letter
    decrypted_test += new_letter

print(decrypted_test)