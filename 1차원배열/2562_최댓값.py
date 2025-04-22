res = []
for i, _ in enumerate(range(9)):
    res.append(int(input()))
    m, i = max(res), res.index(max(res)) + 1
print(m, i, sep = "\n")