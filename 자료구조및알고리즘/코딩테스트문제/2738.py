"""
문제: N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다.
N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

"""
# 1. 첫 줄 N x M 입력받기
row_size, col_size = map(int, input().split())
matrix_A = []
matrix_B = []

# 2. 행렬 A 입력받기
for _ in range(row_size):
    row = list(map(int, input().split()))
    matrix_A.append(row)

# 3. 행렬 B 입력받기
for _ in range(row_size):
    row = list(map(int, input().split()))
    matrix_B.append(row)

# 4. 행렬의 합 출력
for i in range(row_size):
    for j in range(col_size):
        print(matrix_A[i][j] + matrix_B[i][j], end=" ")
    print()

