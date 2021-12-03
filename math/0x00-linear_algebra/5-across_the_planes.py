def add_matrices2D(mat1, mat2):
    """ Adds 2 matrices """
    if (len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0])):
        return None
    
    result = [[0 for x in range(len(mat2))] for y in range(len(mat1))]
    for i in range(0, len(mat1)):
        for j in range(0, len(mat2)):
            result[i][j] = mat1[i][j] + mat2[i][j]
        
    return result