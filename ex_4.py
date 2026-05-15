str1 = set(map(str, input().split(" ")))
str2 = set(map(str, input().split(" ")))
number = input()
if number in str1 & str2:
    print("Yes")
else:
    print("No")