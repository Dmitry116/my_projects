# TODO здесь писать код

def slicer(nums, num):
    if num in nums:
        num_index_start = nums.index(num)
        num_revers = nums[::-1]
        num_index_end = num_revers.index(num)
        index_end = (len(nums) - num_index_end - 1)
        if num <= nums.count(num):
            return (nums[num_index_start:index_end])
        else:
            return (nums[num_index_start::])
    else:
        return ()


number = int(input('Введите номер: '))
print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), number))
