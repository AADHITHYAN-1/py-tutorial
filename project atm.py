pin=7200
blance=10000
num=int(input("enter your pin :" ))
if (num==pin):
    print("pin verification succesfully")
    bank=int(input("withdra:1,deposite:2,enquary:3,exit:4  :"))
    if(bank==1):
        withdra=int(input("enter a amount :"))
        blance=blance-withdra
        print("your blance amount is :",blance)
    elif(bank==2):
        dep=int(input("enter a amount:"))
        blance+=dep
        print("your blance is:",blance)
    elif(bank==3):
        bank1=int(input("blance check:1,complaint:2"))
        if(bank1==1):
            print("your blance is :",blance)
        elif(bank1==2):
            complain=int(input("staf or worst:1,very slow process:2,others:3"))
            if(complain==1):
                print("your complain was registered succeffuly")
            elif(complain==2):
               print("your complain was registered succeffuly")
            elif(complain==3):
                print("can you see manager")
    elif(bank==4):
        print("thank you")
else:
    print("enter correct pin")




