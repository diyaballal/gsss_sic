def my_function(num1,num2=0): #Setting the default value of num1 and num2.
    return num1 +  num2
print(f'Sum = {my_function(10,20)}')
print(f'Sum= {my_function(*(40,90))}')
#print(f'Sum= {my_function((40,90))}') This will show a TypeError because the star has been removed which results in not having a value for num2.

print(f'Sum= {my_function(num2 = 50, num1 = 100)}') #The placement of num1 and num2 doesnt matter because num1 and num2 have just been set with the value 0 from 1st line

