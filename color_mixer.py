# Программа для смешивания цветов

# Ввод цветов от пользователя
red1 = int(input("Введите значение красного цвета (0-255) для первого цвета: "))
green1 = int(input("Введите значение зеленого цвета (0-255) для первого цвета: "))
blue1 = int(input("Введите значение синего цвета (0-255) для первого цвета: "))

red2 = int(input("Введите значение красного цвета (0-255) для второго цвета: "))
green2 = int(input("Введите значение зеленого цвета (0-255) для второго цвета: "))
blue2 = int(input("Введите значение синего цвета (0-255) для второго цвета: "))

# Вычисление смешанного цвета
red_mixed = (red1 + red2) // 2
green_mixed = (green1 + green2) // 2
blue_mixed = (blue1 + blue2) // 2

# Вывод смешанного цвета
print("Смешанный цвет: R={}, G={}, B={}".format(red_mixed, green_mixed, blue_mixed))
