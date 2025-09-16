#friendlypair number
a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))

sum = 0
sum1 = 0

for num in range(1,a):
  if(a % num == 0):
    sum = sum + a

for num1 in range(1,b):
  if(b % num1 == 0):
    sum1 = sum1 + b

if(sum % a == 0 and sum1 % b == 0):
  print(f"{a} and {b} are friendly pair numbers")

else:
  print(f"{a} and {b} are not friendly pair number")


  
