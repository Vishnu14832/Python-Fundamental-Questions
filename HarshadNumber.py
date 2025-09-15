#harshad number like a number is 21 ---> 2 + 1 ---> 3 --> so 21 is divisible by 3 then it is harshad number

num = int(input("enter the number"))
sum = 0
p = num

while(num > 0):
  rem = num % 10
  sum = sum + rem
  num //= 10

if(p % sum == 0):
  print(f"{p} is divisible by {sum} , it is harshad number")
else:
  print("try another number this is not harshad number")
