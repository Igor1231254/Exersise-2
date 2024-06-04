numbers = []
for i in range(6):
    number = float(input(f"Введіть число {i + 1}: "))
    numbers.append(number)

average = sum(numbers) / len(numbers)

print(f"Середнє арифметичне введених чисел: {average}")
