#Write a python program to add two numbers and print the result using both comma and format method.
a = 10
b = 15
print("Sum of", a, "and",  b, "is ", a+b)
print("Sum of {} and {} is {}".format(a, b, a+b))


#write a python program to swap two numbers without a temporary variable.
x = 5
y = 10
x, y = y, x # swap x and y 
print("After swapping: x =", x, ", y =", y)  


#write a python program to get the absolute value of a number.
num = -20
abs_value = abs(num)    
print("The absolute value of", num, "is", abs_value)    