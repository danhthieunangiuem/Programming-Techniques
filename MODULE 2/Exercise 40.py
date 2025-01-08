import random

def initialize_matrix(m, n):
    return [[random.randint(0, 100) for _ in range(n)] for _ in range(m)]

def print_matrix(matrix):
    for row in matrix:
        print(row)

def print_row(matrix, row_index):
    if 0 <= row_index < len(matrix):
        print("Row", row_index, ":", matrix[row_index])
    else:
        print("Invalid row index!")

def print_column(matrix, col_index):
    if 0 <= col_index < len(matrix[0]):
        print("Column", col_index, ":", [row[col_index] for row in matrix])
    else:
        print("Invalid column index!")

def find_max(matrix):
    return max(max(row) for row in matrix)

def find_min(matrix):
    return min(min(row) for row in matrix)

def zigzag_sort(matrix):
    for i in range(len(matrix)):
        if i % 2 == 0:
            matrix[i].sort()
        else:
            matrix[i].sort(reverse=True)

def main():
    m = int(input("Enter number of rows (M): "))
    n = int(input("Enter number of columns (N): "))
    matrix = initialize_matrix(m, n)
    print("\nOriginal Matrix:")
    print_matrix(matrix)

    row_index = int(input("\nEnter row index to display: "))
    print_row(matrix, row_index)

    col_index = int(input("\nEnter column index to display: "))
    print_column(matrix, col_index)

    print("\nMaximum value in the matrix:", find_max(matrix))
    print("Minimum value in the matrix:", find_min(matrix))

    zigzag_sort(matrix)
    print("\nMatrix after Zigzag Sorting:")
    print_matrix(matrix)
main()