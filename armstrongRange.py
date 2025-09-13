start,stop = 150,10000

for i in range(start,stop + 1):
  num = i
  rem = 0
  sum = 0
  n = len(str(num))

  while(num > 0):
    rem = num % 10
    sum = sum + (rem ** n)
    num //= 10
  if(i == sum):
    print(sum)
