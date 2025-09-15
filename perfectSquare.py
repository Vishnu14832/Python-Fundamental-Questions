#perfect square 
import math

num = int(input("enter the number"))

# if(math.ceil(math.sqrt(num)) == math.floor(math.sqrt(num))):
#   print('True')

# else:
#   print('False')

square = int(num ** 0.5)
if(square * square == num):
  print("This is perfect square")
else:
  print("This is not perfect square")


