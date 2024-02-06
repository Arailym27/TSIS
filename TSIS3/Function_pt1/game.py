def spy_game(nums):
    pos_0, pos_0_0 = False, False
    for num in nums:
        if num == 0 and not pos_0:
            pos_0 = True
        elif num == 0 and pos_0:
            if not pos_0_0:
                pos_0_0 = True
            elif pos_0_0 and pos_0:
                return True
        elif num == 7 and pos_0 and pos_0_0:
            return True
    return False

nums = input("Введите список целых чисел через пробел: ").split()
nums = [int(num) for num in nums] 
 # Преобразуем каждый элемент в список в целое число

# Проверяем  "007" во введенном списке и выводим результат
print(spy_game(nums))
