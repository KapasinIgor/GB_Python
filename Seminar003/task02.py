# Задача №2

def compos_list(user_list: list):
    length = len(user_list) // 2 + 1 if len(user_list) % 2 != 0 else len(user_list) // 2
    result_list = [user_list[i] * user_list[len(user_list) - i - 1] for i in range(length)]
    print(result_list)


list1: list = [2, 3, 4, 5, 6]
list2: list = [2, 3, 5, 6]

compos_list(list1)
compos_list(list2)
