numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"
answer = ''	


keypad = [[1,2,3],[4,5,6],[7,8,9],[10,0,11]]

for num in numbers:
    matrix = [(i,j) for i in range(10) for j in range(10) if keypad[i][j] == num]

if matrix[a][0]:
    answer += "L"

elif matrix[a][2]:
    answer += "R"

else:
