print("            It's Mini Calculator              ")

print("If you want to Calculate two numbers by Adding, Subracting Multiple or Divisible. Here, you must type '1'. ")
a=int(input())
if(a==1):
    print("Okay, Done.")
    print("Enter two numbers for A and B ")
    A = int(input("A :"))
    B = int(input("B :"))
    C = input("Choose your Operator : 'add,sub,mul,div' Then Enter : ")
    if(C == "add"):
        print(A+B)
    elif(C == "sub"):
        print(A-B)
    elif(C == "mul"):
        print(A*B)
    elif(C == "div"):
        print(A/B)
    else:
        print("Sorry, You didn't choose the correct choice.")
else:
    print("Sorry, You didn't choose the correct choice.")

print("Bye Bye.. ")
                        
