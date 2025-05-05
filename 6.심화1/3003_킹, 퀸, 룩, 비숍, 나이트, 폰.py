complited = [1, 1, 2, 2, 2, 8]
chess = list(map(int, input().split()))
res = []
for _ in range(6):
    res.append(complited[_] - chess[_])
print(*res)