value = int(input("Введите номер химического элемента:\n"))
if value:
    number_of_element = value
    if number_of_element == 3:
        print("Li")
    elif number_of_element == 25:
        print("Mn")
    elif number_of_element == 80:
        print("Hg")
    elif number_of_element == 17:
        print("Cl")
    else:
        print("такого элемента в базе данных нет")
else:
    print("Неверный формат входных данных")
