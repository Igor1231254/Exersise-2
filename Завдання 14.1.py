def check_number_properties(number):
    if number % 2 == 0:
        print(f"{number} є парним.")
        if number % 4 == 0:
            print(f"{number} також кратне 4.")
        else:
            print(f"{number} не кратне 4.")
    else:
        print(f"{number} є непарним.")

number = int(input("Введіть натуральне число: "))
check_number_properties(number)
