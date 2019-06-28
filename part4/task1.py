setNumber = [5, 1, 8, 92, 7, 30]

# for i in setNumber:
#     if i%2 != 0:
#         setNumber.remove(i)

# print("EvenList:",*setNumber,sep=' ')

setEven = []
for i in setNumber:
    if i%2 == 0:
        setEven.append(i)

print("EvenList:",*setEven,sep = ' ')