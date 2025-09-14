#calculate the strong number

strongNum = int(input("enter the number"))
num = strongNum
sum = 0
rem = 0

while(num > 0):
  rem = num % 10
  f = 1
  for i in range(1,rem+1):
    f = f*i
  sum = sum + f 
  num = num // 10



if(strongNum == sum):
  print(f"{sum} this is strong number")

else:
  print(f"{sum} this is not a strong number")
