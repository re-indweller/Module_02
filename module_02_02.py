# first = int(input("Введите первое целое число: "))
# second = int(input("Введите второе целое число: "))
# third = int(input("Введите третье целое число: "))
# if first == second == third:
#     print(3)
# elif first == second != third or first != second == third or first == third != second:
#     print(2)
# elif first != second != third:
#     print(0)

# # Нули ничто, отрицание недопустимо!
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
ind = 0
while len(my_list) > ind and my_list[ind] >= ind:
    if my_list[ind] != 0:
        print(my_list[ind])
    ind += 1
    continue
