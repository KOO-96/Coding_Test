result = []

words = [str(input()) for _ in range(5)]

for i in range(5):
    for j in range(int(len(words[0]))):
        result.append(words[i][j])


# 0,0 -> 1,0 -> 2,0 -> 3,0 -> 4,0
# 0,1 -> 1,1 -> 2,1 -> 3,1 -> 4,1