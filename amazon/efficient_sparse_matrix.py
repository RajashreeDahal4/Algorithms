"""
Date: February 28, 2024
Name: Rajashree Dahal
Problem:
Create an 'efficient' sparse matrix from a given sparse matrix, Create a transpose of a sparse matrix store the indices where values are present in a hashmap/dictionary format.
For eg: If a 3x8 sparse matrix is something like [[0,1,0,0,0,0,1,1], [1,0,1,0,1,0,1,1],[ 1,1,0,1,1,0,0,0,0]], create its 'efficient' representations as follows:
{0: [1,6,7], 1: [0,2,4,6,7], 2: [0,1,3,4]}
"""

def create_sparse_matrix(matrix):
    sparse_matrix = {}
    for i, row in enumerate(matrix):
        sparse_matrix[i] = [j for j, val in enumerate(row) if val != 0]
    return sparse_matrix

def create_transpose(matrix):
    transpose_matrix = {}
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val != 0:
                if j in transpose_matrix:
                    transpose_matrix[j].append(i)
                else:
                    transpose_matrix[j] = [i]
    return transpose_matrix

# Example usage:
sparse_matrix = [[0,1,0,0,0,0,1,1], [1,0,1,0,1,0,1,1], [1,1,0,1,1,0,0,0]]
efficient_sparse_matrix = create_sparse_matrix(sparse_matrix)
efficient_transpose = create_transpose(sparse_matrix)

print("Efficient Sparse Matrix Representation:")
print(efficient_sparse_matrix)