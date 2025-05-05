text = input()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for pattern in croatia:
    text = text.replace(pattern, "*")
    
print(len(text)) 
