num1= int(input("Enter 3 Number\n"))
num2= int(input())
num3= int(input())

if num1 >= num2 and num1 >= num3:
   numLarge = num1
   print('Max number:', numLarge)
elif num2 >= num1 and num2 >= num3:
   numLarge = num2
   print('Max number:', numLarge)
else:
   numLarge = num3
   print('Max number:', numLarge)

print("The greatest is " + str(numLarge))
