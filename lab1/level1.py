import unittest

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

def double(array):
    array2 = [x ** 2 for x in array]
    array2 = quicksort(array2)
    return array2

class Test(unittest.TestCase):
    def test_double1(self):
        self.assertEqual(double([1, 2, 3]), [1, 4, 9])

    def test_double2(self):
        self.assertEqual(double([-4,-2,0,1,3]), [0,1,4,9,16])   

    def test_double3(self):
        self.assertEqual(double([1,2,3,4,5]), [1,4,9,16,25])    

if __name__ == '__main__':
    unittest.main()