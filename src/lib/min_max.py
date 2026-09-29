def min_max(nums):
    '''возвращает минимальный и максимальный элементы списка nums в виде кортежа (min,max)'''

    if len(nums) == 0:
        raise ValueError('пустой список')

    mn = nums[0]
    mx = nums[0]
    for x in nums:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    return (mn, mx)
