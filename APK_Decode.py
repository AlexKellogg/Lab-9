def decode(password):
    list(password)
    originalpassword = []
    for i in password:
        if i == 3:
            originalpassword.append(0)
        elif i == 2:
            originalpassword.append(9)
        elif i == 1:
            originalpassword.append(8)
        else:
            originalpassword.append(password[i] - 3)
    "".join(originalpassword)
    return originalpassword