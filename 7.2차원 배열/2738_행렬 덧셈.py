def read_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]

def print_matrix_sum(matrix_a, matrix_b):
    for row_a, row_b in zip(matrix_a, matrix_b):
        summed_row = [a + b for a, b in zip(row_a, row_b)]
        print(' '.join(map(str, summed_row)))

N, M = map(int, input().split())
matrix_A, matrix_B = read_matrix(N), read_matrix(N)
print_matrix_sum(matrix_A, matrix_B)

'''
for number, upper, lower in zip("12345", "ABCDE", "abcde"):
print(number, upper, lower)

1 A a
2 B b
3 C c
4 D d
5 E e
'''