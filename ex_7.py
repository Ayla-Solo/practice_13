import itertools

number_list = list(map(str, input().split(" ")))
permutations = list(set((itertools.permutations(number_list))))
print(sorted(permutations))