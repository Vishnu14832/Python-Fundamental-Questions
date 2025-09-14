#perfect number....

perfectNum = int(input("enter the number"))
a = perfectNum
sum = 0

for num in range(1,a):
  if(a % num == 0):
    print(num , end=" ")
    sum = sum + num

if(perfectNum == sum):
  print(f"{sum} this is perfect number")
else:
  print("not a perfect number")