highScore = [45, 67, 56, 78]
for i,score in enumerate(highScore):
    print(str(i+1)+'.',score)

highScore.append(int(input("Enter your new score:")))
for i,score in enumerate(highScore):
    print(str(i+1)+'.',score)