setColor = ['Red','Yellow','Black','Brown']
a=input()
if a.isdigit(): setColor.pop(int(a)-1)
else: setColor.remove(a)

for i, color in enumerate(setColor):
    print(str(i+1)+'.'+color)

