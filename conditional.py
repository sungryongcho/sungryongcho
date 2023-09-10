import re
user_input = input("Provide a password: ")

def password_check(user_input) :
    if len(user_input) < 8 :
        return print("error")
    for char_num in user_input :
        if char_num.isalnum() == False :
            return print("error")
    if bool(re.search(r'\d', user_input)) == False :
        return print("error")

    upper = False
    lower = False

    for char_num in user_input:
        if upper and lower:
            break

        if char_num.isalpha():
            if not upper:
                upper = char_num.isupper()

            if not lower:
                lower = char_num.islower()

    if not upper or not lower:
        return print("error")
    return print("success")

password_check(user_input)
