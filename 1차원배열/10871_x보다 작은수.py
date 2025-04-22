N, X = map(int, input().split())
A = list(map(int,input().split()))
res = []
for _ in range(int(len(A))):
    if A[_] < X:
        res.append(A[_])
    else:
        continue
print(*res)

