#trying out a basic encryption algorithm (caesar cipher)
password = input("Save Password:")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(password):
    encrypted_password = []
    for char in range(len(password)): 
        for l in range(len(letters)): 
            if password[char] == letters[l]:
                new_char = letters[l + 3]
                encrypted_password.append(new_char)
    return encrypted_password 

def decrypt(key):
    decrypted_password = []
    for char in range(len(key)):
        for l in range(len(letters)):
            if key[char] == letters[l]:
                new_char = letters[l - 3]
                decrypted_password.append(new_char)
    return decrypted_password

key = encrypt(password)
print(key)
print(decrypt(key))
