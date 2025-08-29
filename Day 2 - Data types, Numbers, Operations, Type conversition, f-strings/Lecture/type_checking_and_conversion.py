#Type Error

#len(12345) #Type error integers are not supported for the len function

#Challenge: fix type error by using a supported data type
print(len("12345"))# 5

#Find the data type of the value inside parenthesis (type checking)
print(type("Hello")) #<class 'str'>

#Challenge: print the type of the four main primitive data types
print(type("Hello World!")) #<class 'str'>
print(type(123)) #<class 'int'>
print(type(123.5)) #<class 'float'>
print(type(True)) #<class 'bool'>

#Type conversion/Type casting - change of the type type
#converting to int using int() function
print(int("123") + int("456"))
#works for converting digit type string to integers. Trying to convert characters
#causes ValueError
#other converting functions
#int() float() bool() str()
#Challenge: fix the following code: print("Number of letters in your name: " +
#len(input("Enter your name"))

print("Number of letters in your name: " + str(len(input("Enter your name: "))))
