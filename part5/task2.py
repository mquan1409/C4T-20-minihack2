setName = ['ST','BD','BTL','CG','DD','HBT']
setPop = [150300,247100,333300,266800,420900,318000]
max = 0
min = 99999999999

for i,name in enumerate(setName):
    if setPop[i] > max:
        max = setPop[i]
        maxName = name
    if setPop[i] < min:
        min = setPop[i]
        minName = name

print("Max:",maxName,max)
print("Min:",minName,min)