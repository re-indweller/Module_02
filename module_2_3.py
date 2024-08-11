# Нули ничто, отрицание недопустимо!
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while len(my_list) > i and (my_list[i] >= 0):
    if my_list[i] > 0:
        print(my_list[i])
    i += 1