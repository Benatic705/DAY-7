def twoSumBrute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSumOptimized(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i


# Example Test
nums = [2, 7, 11, 15]
target = 9

print("Brute Force Result:")
print(twoSumBrute(nums, target))

print("\nOptimized Result:")
print(twoSumOptimized(nums, target))