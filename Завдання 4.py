a = 10
b = 20
str1 = "Apple"
str2 = "World"
str3 = "Python"
str4 = "Quant"

expression1 = (a > b) or (str1 == "Apple")                 # False or True -> True
expression2 = (str3 == "Python") or (str4 == "Coding")     # True or False -> True

expression3 = (a > b) or (str2 == "Universe")              # False or False -> False
expression4 = (str1 == "Hi") or (str4 == "Coding")         # False or False -> False

print("expression1:", expression1)  # Повинно вивести: True
print("expression2:", expression2)  # Повинно вивести: True
print("expression3:", expression3)  # Повинно вивести: False
print("expression4:", expression4)  # Повинно вивести: False
