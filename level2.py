import unittest


def quickSelect(nums, k, left, right):
    pivot, p = nums[right], left
    for i in range(left, right):
        if nums[i] <= pivot:
            nums [p], nums[i] = nums[i], nums[p]
            p += 1
    nums[p], nums[right] = nums[right], nums[p]
    
    if p > k:
        return quickSelect(nums, k, left, p - 1)
    elif p < k:
        return quickSelect(nums, k, p + 1, right) 
    else:
        return nums[p]


def findKthLargest(nums, k):
    if k < 0 or k > len(nums):
        return None
    copy = nums[:]
    kth_largest = quickSelect(nums, len(nums) - k, 0, len(nums) - 1)
    return f"Знайдений {k}-й найбільший елемент: {kth_largest}. Позиція {k}-ro найбільшого елемента в масиві: {copy.index(kth_largest)}"

class Test(unittest.TestCase):
    def test_findKthLargest1(self):
        self.assertEqual(findKthLargest([15, 7, 22, 9, 36, 2, 42, 18], 3), "Знайдений 3-й найбільший елемент: 22. Позиція 3-ro найбільшого елемента в масиві: 2")

    def test_findKthLargest2(self):
        self.assertEqual(findKthLargest([15, 7, 22, 9, 36, 2, 42, 18], 10), None)

    def test_findKthLargest3(self):
        self.assertEqual(findKthLargest([], 5), None)        

if __name__ == '__main__':
    unittest.main()