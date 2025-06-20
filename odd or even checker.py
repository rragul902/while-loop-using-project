while True:
    num=int(input("enter a number"))
    if num==0:
        print("skips the round")
        continue
    if num==-1:
        print("the game stops")
        break
    if num%2==0:
        print("even numbers:",num)
    else:
        print("odd numbers:",num)
