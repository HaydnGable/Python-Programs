class Solution:
    def __init__(self, arr):
        self.arr = arr
    def sort012(self):
        self.arr.insert(3, self.arr.pop(1))
        self.arr.append(self.arr.pop(1))
        print(self.arr)
array = Solution([0, 1, 2, 0, 1, 2])

array.sort012()


