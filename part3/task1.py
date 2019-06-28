setNumber = [1,5,3,8,9,15]

print('setnumber:')
print(*setNumber,sep = ',')
a = int(input())
if not a in setNumber:
    print("Not Found")
else:
    print("Found"+",","Position",setNumber.index(a)+1)