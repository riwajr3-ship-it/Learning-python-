#integers and operators + = add,- = subt, *= multi, / = div, % = modular]
#ADDITION
x = int(input("what is the value for x "))
y = int(input("what is the value for y "))

print(f"The sum of x and y = {x + y: ,}")

#floats and round off
u = float(input("what is the value for u? "))
v = float(input("what is the value for v? "))
#to round off the value
w = round (u + v, 3)
print(f"The value of the sum of the decimals u and v = {w:,}")
#DIVISION
print(f"The answer is {x/y, 3: .3f}")