N, M = map(int, input().split())
bucket = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):
        bucket[idx] = k
print(*bucket)
