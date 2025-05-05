T = int(input())
for _ in range(T):
    num, word = input().split()
    for i in range(int(len(word))):
        res = word[i]*int(num)
        print(res, end="", sep = "\n")
    print('\n', end='')