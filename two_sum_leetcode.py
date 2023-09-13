def two_sum(nums  , target ):
    num_indices = { }

    for i  , num in enumerate(nums):
        complemenet = target - num
        if complemenet in num_indices:
            return [num_indices[complemenet],i]
        num_indices[num] = i

    return []


nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)