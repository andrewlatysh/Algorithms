def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid  
        elif nums[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1 
    return -1  
nums = [1, 3, 5, 7, 9, 11, 15]
target = 7
result = binary_search(nums, target)
#O(logn)
