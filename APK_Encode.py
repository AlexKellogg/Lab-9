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
