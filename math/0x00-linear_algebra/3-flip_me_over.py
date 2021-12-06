def matrix_transpose(matrix):
    """ Function to transpose a matrix """
    rows = len(matrix)
    colums = len(matrix[0])
    r = []
    result = [[0 for x in range(rows)] for y in range(colums)]
   
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix)):
            result[i][j] = matrix[j][i]
    return result