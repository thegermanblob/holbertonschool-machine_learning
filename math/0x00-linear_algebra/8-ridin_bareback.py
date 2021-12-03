def mat_mul(mat1, mat2):
    """  Multiplies 2 matrixes """
    if (len(mat1) != len(mat2[0]) and len(mat1[0]) != len(mat2)):
        return None
    result = [[0 for x in range(len(mat2[0]))] for y in range(len(mat1))]
    for i in range(0, len(mat1)):
        for j in range(0, len(mat2[0])):
            for k in range(0, len(mat1[0])):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
