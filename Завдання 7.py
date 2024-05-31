first_variable = float(input("Введіть значення першої змінної: "))
second_variable = float(input("Введіть значення другої змінної: "))

if first_variable > second_variable:
    third_variable = first_variable - second_variable
elif first_variable < second_variable:
    third_variable = first_variable + second_variable
else:
    third_variable = first_variable

print("Значення третьої змінної:", third_variable)
