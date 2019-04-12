#Task 1: Run the script and explain the meaning of [1], [5] and [2:4], and the use of find.
print("Python")
print("Python"[1], "Python"[5], "Python"[2:4]) 
str1 = "Hello World!"
print(str1.find('W'))
print(str1.find('x'))
print(str1.rfind('l'))
#y n th Word Python in array like [0][1][2][3][4][5] = [P][y][t][h][o][n]. [1] = [y], [5] = n. [2:4] is start with 2 end with 4th in array [3] = [t][h]

#Task 2: Run the script and explain the meaning of [-1], [-4], [-5:-2], [-2], [-8:-3] and [0:-1] 
print("Python")
print("Python"[-1], "Python"[-4], "Python"[-5:-2])
str1 = "spam & eggs"
print(str1[-2])
print(str1[-8:-3])
print(str1[0:-1])

# Word Python in reverse array like [-6][-5][-4][-3][-2][-1] = [P][y][t][h][o][n]
# n t yth Start from last array [-1]=[n], [-4]=[t], [-5:-2] start with [-5] until end without [-2] = [y][t][h]

# Word spam & eggs in reverse array like [-11][-10][-9][-8][-7][-6][-5][-4][-3][-2][-1] = [s][p][a][m][ ][&][ ][e][g][g][s]
#[-2] = [g]
#[-8:-3] start with [-8] until end without [-3] = [m][ ][&][ ][e]
#[0:-1] start with [0] or [-11] until end without [-1] = [s][p][a][m][ ][&][ ][e][g][g]
...

#Task 3: Run the script and explain the meaning of [2:], [:4], [:], [-3:] and [:-3] 
print("Python"[2:], "Python"[:4], "Python"[:]) #thon Pyth Python
print("Python"[-3:], "Python"[:-3]) #hon Pyt

#Word Python in array like
#[P][y][t][h][o][n]
#[0][1][2][3][4][5] - Normal Array List
#[-6][-5][-4][-3][-2][-1] - Reverse Array List

#[2:] start with [2] until end of Array List = [t][h][o][n]
#[:4] start with empty same as [0] until end without [4] = [P][y][t][h]
#[:] start with empty same as [0] until end of Array List = [P][y][t][h][o][n]
#[-3:] start with [-3] until end of Array List = [h][o][n]
#[:-3] start with empty same as [0] until end without [-3] = [P][y][t]

#Task 4: Run the script and explain the use of int, float and eval
print(int("23")) #23
print(float("23")) #23.0
print(eval("23")) #23
print(eval("23.5")) #23.5
x = 5
print(eval("23 + (2 * x)"))#33

#int() method returns an integer object from any number or string.
#float() method returns a floating point number from a number or a string.
#eval() method parses the expression passed to this method and runs python expression (code) within the program.

