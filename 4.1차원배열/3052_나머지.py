import sys
res = set()
for _ in range(10):
    num = int(sys.stdin.readline())%42
    res.add(num)
print(len(res))