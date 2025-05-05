import sys
T = int(input())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{_+1}: {A+B}')