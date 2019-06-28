setPop = [150300,247100,333300,266800,420900,318000]
setArea = [11743,6.224,43.35,12.04,9.96,10.09]
setDen = []

for i,pop in enumerate(setPop):
    setDen.append(setPop[i]/setArea[i])

print(setDen)