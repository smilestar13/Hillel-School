num_0 = int(input('Введите 4-хзначное число:'))

# Разбил вводное число на 2 равные пары
part_1, part_2 = divmod(num_0, 100)

# Вывожу уже готовую переменную с пар, тем же методом
num_1, num_2 = divmod(part_1, 10)
num_3, num_4 = divmod(part_2, 10)

# Вывожу ответ пользователю
print('Вы ввели следующие цифры:')
print(num_1)
print(num_2)
print(num_3)
print(f'{num_4}.')

# Добавил точку в конце программы, для красоты.
