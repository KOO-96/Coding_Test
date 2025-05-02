word = input()
cnt = 0
dial = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R", "S"], ["T", "U", "V"], ["W", "X", "Y", "Z"]]
for d in range(int(len(dial))):
    for _ in range(len(word)):
        if word[_] in dial[d]:
            cnt += int(d)+3
        else:
            pass
print(cnt)