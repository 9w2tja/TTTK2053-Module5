#Task 1 : Run the script and explain based on the generated output
## Calculate average of grades.
grades = [] # Create the variable grades and assign it the empty list.

num = float(input("Enter the first grade: "))
grades.append(num)
num = float(input("Enter the second grade: "))
grades.append(num)
num = float(input("Enter the third grade: "))
grades.append(num)
num = float(input("Enter the fourth grade: "))
grades.append(num)
num = float(input("Enter the fifth grade: "))
grades.append(num) 

minimumGrade = min(grades) #Get minimum grades
grades.remove(minimumGrade) #Remove minimum grades
minimumGrade = min(grades) #Get minimum grades
grades.remove(minimumGrade)#Remove minimum grades

average = sum(grades) / len(grades) 
print("Average Grade: {0:.2f}".format(average))
