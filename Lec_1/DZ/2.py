# Даны N целых чисел подсчитайте общее количество пар целых
# чисел, которые имеют разность K.

# 1-я строка содержит N и K (целые числа).
# 2-я строка содержит N номеров набора.

def count_pairs_with_difference(arr, n, k):
    count = 0
    num_count = {}

    # Заполняем хеш-таблицу с числами из массива
    for num in arr:
        num_count[num] = num_count.get(num, 0) + 1

    # Ищем пары с разностью k
    if k != 0:
        for num in arr:
            if (num + k) in num_count:
                count += num_count[num + k]
            if (num - k) in num_count:
                count += num_count[num - k]

        # Учтем, что каждая пара рассматривается дважды, поэтому делим на 2
        count //= 2
    else:
        for num in arr:
            # Считаем только уникальные пары, если разность равна 0
            if num_count[num] > 1:
                count += (num_count[num] * (num_count[num] - 1)) // 2
                num_count[num] = 0  # Обнуляем, чтобы не считать больше одной пары

    return count


# Чтение данных
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Подсчет пар с разностью k
result = count_pairs_with_difference(arr, n, k)
print(result)

