print("simple calculator")
print("type exit to stop ")

while True:
    op=input('choose operation(,+,-,*,/):')
    
    if op=="exit":
        print("calculator closed")
        break
    if op not in["+","-","*","/"]:
        print("invalid operations")
        continue
    
    num1=float(int(input("enter a number:")))
    num2=float(int(input("enter a number:")))
    
    if op=="+":
        result=num1+num2
    
    elif op=="-":
        result=num1-num2
    
    elif op=="*":
        result=num1*num2
    elif op=="/":
        if num2==0:
            print("x cannot divide by zero.")
        result=num1/num2
    print("result:",result,"\n")    
