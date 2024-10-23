elements = {
    "Гідроген": 1.008,
    "Гелій": 4.0026,
    "Літій": 6.94,
    "Берилій": 9.0122,
    "Бор": 10.81,
    "Карбон": 12.011,
    "Нітроген": 14.007,
    "Оксиген": 15.999
}

# Додавання нових елементів
N = int(input("Скільки елементів ви хочете додати?"))
for _ in range(N):
    name = input("Введіть назву елемента: ")
    mass = float(input("Введіть атомну масу елемента:"))
    elements[name] = mass

# Сортування словника за атомною масою
sorted_elements = dict(sorted(elements.items(), key=lambda item: item[1]))

print("\n")
print("Відсортований словник (за атомною масою):")
for name, mass in sorted_elements.items():
    print(f"{name}: {mass}")
