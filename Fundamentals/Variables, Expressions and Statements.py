#Task 1 : Run the following Python script, and explain the difference between * and ** 
print(3 + 2, 3 - 2, 3 * 2) #multiplication
print(8 / 2, 8 ** 2, 2 * (3 + 4)) #power of

print(3 * 2, 3 ** 2) #* use for multiplication and ** is for power of

#Task 2 : Using the given Python script, explain why variables in Python do not need to be declared, and how are the types of the variables determined ?
speed = 50
timeElasped = 14
distance = speed * timeElasped
print(distance)
#In Python, variables do not require forward declaration. All you need to do is provide a variable name and assign it some value.

# Task 3 : Identify the built-in functions in the following Python Script and explain the tasks performed by those functions ?
a = 2
b = 3
print(abs(1 - (4 * b))) #returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude
print(int((a ** b) + .8))#returns an integer object from any number or string
print(round(a / b, 3)) #returns the floating point number rounded off to the given ndigits digits after the decimal point. If no ndigits is provided, it rounds off the number to the nearest integer



# Task 5 : Explain the differences between // and %
totalInches = 41
feet = totalInches // 12 #Floor division - division that results into whole number adjusted to the left in the number line
inches = totalInches % 12 #Modulus - remainder of the division of left operand by the right
print(feet, inches)
