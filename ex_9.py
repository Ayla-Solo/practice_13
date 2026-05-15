import itertools  # подключаем модуль для работы с комбинациями

number_set = set(map(str, input().split(" ")))
n = len(number_set)  # количество уникальных элементов в множестве
k = int(input())
print(list(itertools.combinations(number_set, k)))  