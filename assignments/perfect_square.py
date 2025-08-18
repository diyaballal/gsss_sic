#Check if a number is a perfect square 
import math
num=int(input("Enter a number of your choice:"))
root=math.isqrt(num)

if root * root == num:
    print("The number entered is a perfect square!!")
