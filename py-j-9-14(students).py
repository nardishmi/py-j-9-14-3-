


while True:
    score_=float(input("add youre score pls:"))
    if score_<0 or score_>20 :
        print("your score is incorrect.")
        continue
    if 17<=score_<=20 :
        if 19.5<=score_<=20 :
            print("your score is A++.")
            break 
        if 18<=score_<19.5 :
            print("your score is A+.")
            break
        if 17<=score_<18 :
            print("your score is A.")
            break
    if 14<=score_<17 :
        if 16.5<=score_<17 :
            print("your score is B++.")
            break
        if 15<=score_<16.5 :
            print("your score is B+.")
            break 
        if 14<=score_<15 :
            print("your score is B.")
            break
    if 11<=score_<14 :
        if 13.5<=score_<14 :
            print("your score is C++.")
            break
        if 12<=score_<13.5 :
            print("your score is C+.")
            break
        if 11<=score_<12 :
            print("your score is C.")
            break
    if 10<=score_<11 :
        if 10.75<=score_<11 :
            print("your score is D++.")
            break
        if 10.5<=score_<10.75 :
            print("your score is D+.")
            break
        if 10<=score_<10.5 :
            print("your score is D.")
            break
    else :
        print("you failed the exam.")
    break
    
   
       
    
    
    
