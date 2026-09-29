



while True:
    username_=input("Enter your username pls:")
    password_=input("Enter your password pls:")
    
    if len(username_)<10 :
        print(" Your username must be at least 10 characters.")
    if len(password_)<10 :
        print("Your password must be at least 10 characters.") 

    age_=int(input("Enter your age pls:"))
    print(age_)
    if age_<16 :
        print("Your age must be at least 16.")

    if len(username_)>=10 and len(password_)>=10 and age_>=16 :
        print("Your username and password are valid.")
        print("Your age is valid.")
        if 14<=len(username_)<=16 :
            print("Your username is strong.")
        elif 12<=len(username_)<14 :
            print("Your username is acceptable.")
        elif 10<=len(username_)<12 :
            print("Your username is week.")
        if 14<=len(password_)<=16 :
            print("Your password is strong.")
        elif 12<=len(password_)<14 :
            print("Your password is acceptable.")
        elif 10<=len(password_)<12 :
            print("Your password is week.")    
        break

   
        



