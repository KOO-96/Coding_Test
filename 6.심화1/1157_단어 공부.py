word = input().lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_counts = [word.count(_) for _ in alphabet] 

max_count = max(letter_counts)
if letter_counts.count(max_count) > 1:
    print("?")
else:
    max_index = letter_counts.index(max_count)
    print(alphabet[max_index].upper())
