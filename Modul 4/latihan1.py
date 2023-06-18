max_attemps = 3
attemps = 0

while attemps < max_attemps:
    username = "wahyu"
    password = "wahyu123"
    username = input(f"Username: ")
    password = input(f"Password: ")
    if username == "wahyu" and password == "wahyu123":
        print(f"Anda Masuk!")
        break
    else:
        print(f"Maaf password atau username anda salah!")
        attemps += 1
        if max_attemps == attemps:
            print(f"Akun anda terblokir")
