def binary_search(nums, target):
    """
    二分搜尋法用於在已排序的數字列表中尋找目標數字的索引。
    
    :param nums: 數字列表，已排序（升序或降序）
    :param target: 目標數字
    
    :return: 目標數字的索引，若不存在則返回 -1
    """
    left, right = 0, len(nums) - 1  # 左右邊界

    while left <= right: # 當左邊界小於等於右邊界時
        mid = left + (right - left) // 2 # 取中間索引
        if nums[mid] == target: # 若中間數字等於目標數字
            return mid      # 返回中間索引
        elif nums[mid] < target: # 若中間數字小於目標數字
            left = mid + 1  # 更新左邊界
        else:               # 若中間數字大於目標數字
            right = mid - 1 # 更新右邊界

    return -1 # 若不存在目標數字，返回 -1