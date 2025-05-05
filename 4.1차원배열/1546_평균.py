N = int(input())
grade = list(map(int, input().split()))
M = max(grade)
grade2 = []
for _ in range(int(len(grade))):
    grade2.append((grade[_]/M*100))
print(sum(grade2)/N)