from calculator import basic , scitific 

while True: 
    cal=int(input("Enter your choice :\n1.basics\n2.Scitific\n3.exit\nchoice=")) 
    if cal==1: 
        a=int(input("Enter a :")) 
        b=int(input("Enter b :")) 
        ch=int(input("Enter your choice\n1.addition\n2.subtraction\n3.multiplication\n4.dvision\n5.modulus\n6.power\n 7.squre root\nchoice=")) 
        if ch==1: 
            print(basic.add(a,b)) 
        elif ch==2: 
            print(basic.sub(a,b)) 
        elif ch==3: 
            print(basic.mul(a,b)) 
        elif ch==4: 
            print(basic.div(a,b)) 
        elif ch ==5: 
            print(basic.mod(a,b)) 
        elif ch==6: 
            print(basic.pow(a,b))         
        elif ch==7: 
            print(basic.sqrt(a))     
        else: 
            print("invalid choice") 
    elif cal==2: 
        a=int(input("Enter a :")) 
        ch=int(input("Enter your choice: \n1.natural log\n2.log base_10\n3.trignometry\nchoice=")) 
        if ch==1: 
            print(scitific.natural_log(a)) 
        elif ch==2: 
            print(scitific.log_base_10(a)) 
        elif ch==3:
            opt=int(input("Enter your choice: \n1.sine\n2.cosine\n3.tan\nchoice=")) 
            if opt==1: 
                print(scitific.sine(a)) 
            elif opt==2: 
                print(scitific.cosine(a)) 
            elif opt==3: 
                print(scitific.tangent(a)) 
        else: 
            print("invalid choice")             
    elif cal==3: 
        break         
