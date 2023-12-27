def rotateImage(matrix: list):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

from ast import literal_eval
l = literal_eval(input("Enter a n*n matrix in form of list: "))
print(rotateImage(l))