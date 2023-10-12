print(" *** Summation of each digit ***")
n = str(input("Enter a positive number : "))

x = len(n)

if x <= 30:
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    print("Summation of each digit = ",sum)
    

    
#  def getSum(n):
    
#     sum = 0
#     for digit in str(n): 
#       sum += int(digit)      
#     return sum
   
#  print(getSum(n))