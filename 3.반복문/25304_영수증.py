X = int(input())
N = int(input())
cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    mul = a * b
    cnt += mul
if X == cnt:
    print("Yes")
else:
    print("No")