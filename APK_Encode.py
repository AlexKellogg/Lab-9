def encode(password):
    #Alex Kellogg
    newpassword = []
    list(password)
    for i in list:
        if i == 7:
            newpassword.append(0)
        elif i == 8:
            newpassword.append(1)
        elif i == 9:
            newpassword.append(2)
        else:
            newpassword.append(password[i] + 3)
    "".join(newpassword)
    return newpassword


if __name__ == "__main__":
    while True:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")
        choice = int(input("Please enter an option: "))
        if choice == 3:
            break
        elif choice == 1:
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            new_pass = MS_decode.decode(password)
            print(f"The encoded password is {password}, and the original password is {new_pass}.")