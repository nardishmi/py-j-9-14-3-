

while True:
    salary_=int(input("Enter your salary pls:"))

    if salary_<5 or salary_>200 :
        print("Error! Invalid salary.")
        continue
    elif 100<=salary_<=200 :
        payment_=salary_*0.65
        print(payment_)
        
    elif 90<=salary_<100 :
        payment_=salary_*0.80
        print(payment_)
        
    elif 70<=salary_<90 :
        payment_=salary_*0.85
        print(payment_)
        
    elif 60<=salary_<70 :
        payment_=salary_*0.90
        print(payment_)
        
    elif 50<=salary_<60 :
        payment_=salary_*0.95
        print(payment_)
        
    elif 40<=salary_<50 :
        payment_=salary_*0.97
        print(payment_)

    elif  salary_<40 :
        payment_=salary_
        print(payment_)
    break
    
    