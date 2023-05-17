from typing import List


def foo(nums: List[int]) -> List[int]:
    prod = 1
    for num in nums:
        prod *= num
    nums2 = []
    for num in nums:
        nums2.append((prod // num))
    return nums2
