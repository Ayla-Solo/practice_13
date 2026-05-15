number_array = list(map(int, input().split(" ")))
one_number = int(input())
if one_number in number_array and number_array.count(one_number) >= 2:
    print("Yes")
else:
    print("No")