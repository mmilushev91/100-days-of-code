#Mathematical operators

print(12 + 3) # 15
print(12 - 3) # 9
print(12 * 3) # 36
#result is a float due to implicit casting. Python automatically
#converts the result to float
print(12 / 4) # 3.0 
#result is integer. Decimal decimal places are removed
print(12 // 5) # 2
#exponent operator
print(2 ** 2) # 4
#Order of operations: PEMDASLR
# 1. Parenthesis 2. Exponent 3. Multiplication 4. Division
# 5. Addition 6. Subtraction 7. Left to right
# Multiplication and Division has the same priority
# Addition and Subtraction has the same priority
# When equal priority the leftmost operation is first
# ()
# **
# * OR /
# + OR -

#Challenge: right down the order of operations
print(3 * 3 + 3 / 3 - 3)# 9 + 1.0 - 3 = 10.0 - 3 = 7.0
#Challenge: change the order of operations so the result is 3
print(3 * (3 + 3) / 3 - 3) # 3 * 6 / 3 - 3 = 18 / 3 - 3 = 6.0 - 3 = 3.0
