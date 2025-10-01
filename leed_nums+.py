def leed_nums(nums):
    rez = []
    max_el = nums[-1]
    n = len(nums)
    for i in range(n-1,-1,-1):
        if nums[i] > max_el:
            rez.append(nums[i])
            max_el = nums[i]
    return rez


nums = [int(x) for x in input().split()]
print(leed_nums(nums))