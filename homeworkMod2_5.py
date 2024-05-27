

def get_matrix(n, m, value):
    matrix = []
    for i in range(1, n+1):
        temp = []
        for j in range(1, m+1):
            temp.append(value)
        matrix.append(temp)
    return matrix


get_matrix1 = get_matrix(2, 3, 10)
get_matrix2 = get_matrix(3, 5, 42)
get_matrix3 = get_matrix(4, 4, 13)
print(get_matrix1)
print(get_matrix2)
print(get_matrix3)