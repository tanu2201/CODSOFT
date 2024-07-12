import random
def generate_password(length):
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    words = ["a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m", "n", "o","p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    base_word = random.choice(words)
    for i in range(length - len(base_word)):
        base_word += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-")
    password_list = list(base_word)
    random.shuffle(password_list)
    password = "".join(password_list)
    return password
length = int(input("Enter the length of the password: "))
print("Generated Password : ", generate_password(length))
