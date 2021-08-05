color1 = input('')
color2 = input('')
color3 = input('')

color = ["black", "brown", "red", "orange", "yellow",
         "green", "blue", "violet", "grey", "white"]
gopnum = [1, 10, 100, 1000, 10000, 100000,
          1000000, 10000000, 100000000, 1000000000]
answerlist = []

for i in range(10):
    if color1 == color[i]:
        answerlist.append(str(i))

for i in range(10):
    if color2 == color[i]:
        answerlist.append(str(i))

str = "".join(answerlist)

for i in range(10):
    if color3 == color[i]:
        str = int(str)*gopnum[i]

print(str)
