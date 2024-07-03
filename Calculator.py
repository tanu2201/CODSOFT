#required functions
def addition(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def exp(a,b):
    return(pow(a,b))

def div(a,b):
    try:
        d=a/b
    except ZeroDivisionError as msg:
        print(msg)
    except ValueError as msg:
        print(msg)
    else:
        return(d)




def main():
    print('''
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division
      5. Exponent
      ''')
    choice=int(input("Enter the operation you want to perform : "))
    if choice==1 or choice==2 or choice==3 or choice==4 or choice==5:
        a=int(input("Enter first operand="))
        b=int(input("Enter second operand="))
        if choice==1:
            y=addition(a,b)
        elif choice==2:
            y=sub(a,b)
        elif choice==3:
            y=mul(a,b)
        elif choice==4:
            y=div(a,b)
        elif choice==5:
            y=exp(a,b)
        print("Your solution is ",y)
        ch=None
        ch=input(("To do another calculation press (yes/no) : "))
        if ch=="yes":
            main()
        elif ch=="no":
            print("Thanks for using calculator!")
          
            
            
    else:
        print("invalid choice")
        main()

main()
