array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


answer = []
cut = []

for a in range(len(commands)):
    cut = array[commands[a][0] -1 : commands[a][1]]
    cut.sort()
    answer.append( cut[commands[a][2]-1])

print(answer)


