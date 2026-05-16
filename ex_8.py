import itertools
numbers = input().split()
result = []  # сюда будем складывать все подмножества

for r in range(len(numbers) + 1):
    # r — размер подмножества (от 0 до n)
    subsets = itertools.combinations(numbers, r)
    # генерируем все комбинации длины r
    result.extend(subsets)
print(result)
