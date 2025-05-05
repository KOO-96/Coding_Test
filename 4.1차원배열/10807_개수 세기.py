N = int(input())
cnt = list(map(int, input().split()))
v = int(input())
res = 0
for _ in range(int(len(cnt))):
    if v == cnt[_]:
        res += 1
    else:
        res +=0
print(res)