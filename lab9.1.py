countries = []
print("Введіть назви 10 країн Європи:")

for i in range(10):
    country = input(f"Країна {i+1}: ")
    countries.append(country)

countries_tuple = tuple(countries)
print("\n")
print("Кортеж країн Європи:")
print(countries_tuple)