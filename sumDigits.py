#sum of digits of a number
num = int(input("Enter the sum digit"))
rem = 0
sum = 0

while(num > 0):
  rem = num % 10
  sum = sum + rem
  num = num // 10

print(sum)