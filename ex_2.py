n = int(input())
courses = set()
for i in range(n):
    courses.update(set(map(str, input().split(" "))))
print(len(courses))