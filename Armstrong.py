#check armstrong number
class checkArmstrong:
  def __init__(self,num):
    self.num = num
  
    rem = 0
    arm = 0
    sum = 0
    
    a = num

    while(a > 0):
      rem = a % 10
      arm = rem * rem * rem
      sum = sum + arm
      a //= 10

    if(num == sum):
      print(f"{sum} is armstrong number")
    else:
      print(f"{sum} not a armstrong number")

check = checkArmstrong(371)
print(check.num)
    