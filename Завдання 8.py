#А
a, b = 0, 1


print("Перші 20 чисел ряду Фібоначчі:")
for _ in range(20):
    print(a, end=" ")
    a, b = b, a + b
print()

#B
print("Парні числа від 0 до 20:")
number = 0
while number <= 20:
    print(number, end=" ")
    number += 2
print()


print("Кожне третє число від -1 до -21:")
number = -1
while number >= -21:
    print(number, end=" ")
    number -= 3
print()
