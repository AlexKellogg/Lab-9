def decode(password):
    new_pass = ''
    if len(password) <= 8:
        for i in range(0, len(password)):
            if int(password[i]) == 0:
                new_pass += "7"
            elif int(password[i]) == 1:
                new_pass += "8"
            elif int(password[i]) == 2:
                new_pass += "9"
            else:
                item = str(int(password[i]) - 3)
                item = item[-1]
                new_pass += item
    return new_pass
