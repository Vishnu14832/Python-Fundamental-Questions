#calculate the factor of a number

factor = int(input("Enter the number"))

for num in range (2,factor):
  if(factor % num == 0):
    print(num , end=" ")