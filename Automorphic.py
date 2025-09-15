# automorphic number like (6) power of 2 = 36, (376) power of 2 = 141376

num = int(input("Enter the number"))
a = str(num)
b = num ** 2
c = str(b)

if(c.endswith(a)):
  print("Automorphic number")
else:
  print("Not Automorphic number")