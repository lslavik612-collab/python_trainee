def leed_nums(nums):
    n = len(nums)
    rez = []
    for i in range(n):
        for j in range(i+1,n):
            if nums[j] > nums[i]:
                break
        else:
            rez.append(nums[i])
    return rez


nums = [int(x) for x in input().split()]
print(*leed_nums(nums))


