#palindrome number
num = int(input("Enter the number"))
n = num
sum = 0
rem = 0

while(num > 0):
  rem = num % 10
  sum = sum * 10 + rem
  num = num // 10

if(n == sum):
  print(f"{sum} is palindrome number")
else:
  print(f"{sum} not a palindrome number")