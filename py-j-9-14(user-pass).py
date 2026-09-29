


while True:
    username_=input("Enter your username pls:")
    password_=input("Enter your password pls:")
    age_=int(input("Enter your age pls:"))

    if len(username_)>=10 and len(password_)>=10 and age_>=16 :
        print("Your username and password are valid.")
        print("Your age is valid.")
        break
    if len(username_)<10 :
        print(" Your username must be at least 10 characters.")
        continue
    if len(password_)<10 :
        print("Your password must be at least 10 characters.")
        continue  
    if age_<16 :
        print("Your age must be at least 16.")
        continue

