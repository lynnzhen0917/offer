import sys
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
i = len(matrix)-1
j = 0
#print(matrix[i][j])
while i >= 0 and j <= len(matrix[0])-1:
    if matrix[i][j] > target:
        i -= 1
    elif matrix[i][j] < target:
        j += 1
    elif matrix[i][j] == target:
        print("True")
        sys.exit()
print("False")