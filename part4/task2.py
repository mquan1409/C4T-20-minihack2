setNumber = input().split(',')

setEven = []
for i in setNumber:
    if int(i)%2 == 0:
        setEven.append(i)

print("EvenList:",*setEven,sep = ' ')