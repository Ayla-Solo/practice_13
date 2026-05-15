n = int(input())
array = []

for i in range(n+1):
    array.append(i)

i = 2                         # начинаем с первого простого числа
while i <= n ** 0.5:
    if array[i] != 0:         # если число не "вычеркнуто"
        j = i ** 2            # начинаем с i² (меньшие кратные уже обработаны)
        while j <= n:         # идём по всем кратным i
            array[j] = 0      # "вычёркиваем" составное число
            j += i            # переходим к следующему кратному
    i = i + 1                 # проверяем следующее число

array = set(array)
array.remove(0)

print(array)