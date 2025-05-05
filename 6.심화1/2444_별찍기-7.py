n = int(input())
for i in range(1, (2*n)):
  if i < n:
    print(' '*(n-i), '*'*(i*2-1), sep='')
  elif i == n:
    print('*'*(2*n-1))
  else:
    print(' '*(i-n), '*'*((2*n-1)-2*(i%n)), sep='')