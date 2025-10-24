x=int(input("enter the range: "))
for i in range(1,x+1):
    num=str(i)
    total=0
    length=len(num)
    for digit in num:
        total+= int(digit)**length
        if total==i:
            print(i)
            break

