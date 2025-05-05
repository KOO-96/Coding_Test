A, B = map(str,input().split())
result = max(int(A[::-1]), int(B[::-1]))
print(result)