def get_column(B, idx):
    column = []
    for row in B:
        column.append(row[idx])
    return column


def row_column_multiplication(row, column):
    res = 0
    row_len = len(row)
    for i in range(row_len):
        res = res + row[i] * column[i]
    return res


def matrix_multiplication(A, B):
    C = []
    for row in A:
        if len(row) != len(B):
            return "Wrong input"

    for row in B:
        if len(row) != len(A):
            return "Wrong input"
    for row in A:
        column_number = len(B[0])
        c_row = []
        for column_idx in range(column_number):
            column = get_column(B, column_idx)
            c_row.append(row_column_multiplication(row, column))
        C.append(c_row)
    return C


def print_matrix_modified(matrix):

    for rows in range(len(matrix)):
        row_res = ""
        for cols in range(len(matrix[rows])):
            indent = max(map(lambda x: len(str(x)), (elem[cols] for elem in matrix[0:len(matrix)])))
            row_res = row_res + str(matrix[rows][cols]).rjust(indent) + "  "
        print(row_res)