S = input()
alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for _ in range(len(alpabet)):
    if alpabet[_] in S:
        print(S.index(alpabet[_]), end=' ')
    else:
        print('-1', end=' ')
