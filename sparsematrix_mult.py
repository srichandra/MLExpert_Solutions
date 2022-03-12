def get_keys(matrix):
    sparse_dict={}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]!=0:
                sparse_dict[(i,j)]=matrix[i][j]
    return sparse_dict

def sparse_matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a[0])!=len(matrix_b):
        return [[]]
    sparse_a=get_keys(matrix_a)
    sparse_b=get_keys(matrix_b)
    matrix_c=[[0 for i in range(len(matrix_b[0]))] for j in range(len(matrix_a))]
    for i,k in sparse_a.keys():
        for j in range(len(matrix_b[0])):
            if (k,j) in sparse_b.keys():
                matrix_c[i][j]+=sparse_a[(i,k)]*sparse_b[(k,j)]
    return matrix_c
