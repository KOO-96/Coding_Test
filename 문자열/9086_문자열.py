import sys
T = int(input())
for _ in range(T):
    word = sys.stdin.readline().rstrip()
    print(word[0]+word[-1])