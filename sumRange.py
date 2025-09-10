start = int(input("Enter the starting number"))
stop = int(input("Enter the stopping number"))
sum = 0
for i in range(start , stop + 1):
  print(i , end="")
  sum = sum + i
print("\n")
print(sum)
