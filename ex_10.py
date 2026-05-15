nums = list(map(int, input().split()))

result = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):

            if nums[i] + nums[j] + nums[k] == 0:

                triple = sorted([nums[i], nums[j], nums[k]])
                if triple not in result:
                    result.append(triple)

print(result)  