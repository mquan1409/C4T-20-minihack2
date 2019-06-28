highScore = [45, 67, 56, 78,90]
highScore.sort(reverse = True)
for i,score in enumerate(highScore):
    print(str(i+1)+'.',score)

highScore.append(int(input("Enter your new score:")))
highScore.sort(reverse = True)
for i,score in enumerate(highScore):
    print(str(i+1)+'.',score)
    if i == 4: break