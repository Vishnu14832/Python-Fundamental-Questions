factorialNum = int(input("Enter the number"))
fact = 1
sum = 0

for num in range(1, factorialNum + 1):
  fact = fact * num


print(f"factorial of a number is {fact}")
