#Differentiation Program
#Single Function, To the Power, product of two functions, dividsion of two
#functions, Polynomial Function,Chain Rule, Inverse Trigonometric function, Hyperbolic
#function, Successive Differentiation.
import math
def home():
    print("------------------------------------------------------------")
    print("Press 1 for Single Function.")
    print("Press 2 for Power Function.")
    print("Press 3 for Product of two functions.")
    print("Press 4 for Division of two functions.")
    print("Press 5 for Polynomial Functions.")
    print("Press 6 for Function of Function.")
    print("Press 7 for Inverse Trigonometric Function.")
    print("Press 8 for Hyperbolic Function.")
    print("Press 9 for Higher Order Derivatives.")
    print("------------------------------------------------------------")
    ch=input("Enter your Choice:")
    if ch=='1':
        Single_Function()
    elif ch=='2':
        Power_Function()
    elif ch=='3':
        Product_Function()
    elif ch=='4':
        Division_Function()
    elif ch=='5':
        Polynomial_Function()
    elif ch=='6':
        Function_Function()
    elif ch=='7':
        Inverse_Function()
    elif ch=='8':
        Hyperbolic_Function()
    elif ch=='9':
        Higher_Order()
    else:
        print("Please Enter Correct Choice.")
    home()
def Single_Function():
    f=input("Please Input your function.")
    if 'x^' in f:
        s=f.split("^")
        a=int(s[1])-1
        if a==1:
            print("Differentiation =",s[1]+s[0])
        else:
            print("Differentiation =",s[1]+s[0]+"^"+str(a))
    elif 'e^' in f and (f.split("^"))[1].isdigit()==False:
        s=f.split("^")
        if '-' in s[1]:
            a=s[1].replace('-','')
            if a.isalnum()==True:
                for i in s[1]:
                    if i.isdigit()==True:
                        b=i
                        break
                print("Differentiation =",'-'+b+f)
            else:
                print("Differentiation =",'-'+f)
        else:
            if s[1].isalnum()==True:
                for i in s[1]:
                    if i.isdigit()==True:
                        b=i
                        break
                print("Differentiation =",b+f)
            else:
                print("Differentiation =",f)
    home()
home()
