#Task 1: Run the script and explain the implementation
## Break a name into two parts -- the last name and the first names.
fullName = input("Enter a full name: ")
n = fullName.rfind(" ") # index of the space preceding the last name
# Display the desired information.
print("Last name:", fullName[n+1:]) #n+1 will find the last space and using counting space until end and will take all word after that
print("First name(s):", fullName[:n]) #word will taken from start untul last space found

#Task 2:  Run the script and Explain the purpose of escape sequences used in the script
## Demonstrate use of escape sequences.
print("01234567890123456")
print("a\tb\tc") #Defaul tab size is 8
print("a\tb\tc".expandtabs(5)) #5 tab size
print("Nudge, \tnudge, \nwink, \twink.".expandtabs(11)) #11 tab size
#The expandtabs() method returns a copy of string with all tab characters '\t' replaced with whitespace characters until the next multiple of tabsize parameter.
#The expandtabs() takes an integer tabsize argument. The default tabsize is 8.

#Task 3: Run the script and elaborate the use of sep= in displaying output
# Demonstrate justificarion of output.
print("0123456789012345678901234567")
print("Rank".ljust(5), "Player".ljust(20), "HR".rjust(3), sep="")
print('1'.center(5), "Barry Bonds".ljust(20), "762".rjust(3), sep="")
print('2'.center(5), "Hank Aaron".ljust(20), "755".rjust(3), sep="")
print('3'.center(5), "Babe Ruth".ljust(20), "714".rjust(3), sep="")
#The sep separator is used between the values. It defaults into a space character.

#Task 4: Run the script and describe the formatting applied in the script
#Demonstrate use of the format method.
print("The area of {0:s} is {1:,d} square miles.".format("Texas", 268820))
str1 = "The population of {0:s} is {1:.2%} of the U.S. population."
print(str1.format("Texas", 26448000 / 309000000))
#The area of Texas is 268,820 square miles.
#The population of Texas is 8.56% of the U.S. population.

#The built-in format() method returns a formatted representation of the given value controlled by the format specifier.
#{0:s} first string (s) in format() located
#{1:,d} second with decimal (d) in format() located
#{1:.2%} second with .2 float number and % at the end
