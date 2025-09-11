year = int(input("Enter the year"))

if(year % 4 == 0 and year % 100!=0):
  print(f"{year} leap year")
elif(year % 400 == 0):
  print(f"{year} is century leap year")

else:
  print("Not a leap year")