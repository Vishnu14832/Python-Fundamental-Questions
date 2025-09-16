#abundant number 

AbundantNum = int(input("Enter the number"))
sum = 0

for num in range(1,AbundantNum):
  if(AbundantNum % num == 0):
    sum = sum + num

if(sum > AbundantNum):
  print(f"{sum} greater {AbundantNum} so this is Abundant Number")
else:
  print(f"{sum} less than {AbundantNum} so this is not Abundant Number")