import sys
students = set([i for i in range(1, 31)])
submit = set([int(sys.stdin.readline()) for _ in range(28)])
not_yet = list(students - submit)
print(*sorted(not_yet), sep = "\n")