#greatest of three numbers
a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
c = int(input("Enter the value of c"))

if(a > b and a > c):
  print(f"{a} is greater")
elif (b > a and b > c):
  print(f"{b} is greater")
else:
  print(f"{c} is greator")
  

