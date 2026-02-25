class Solution:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
    def search(self):
        if self.k not in self.arr:
            print("-1")
        else:
            for i in self.arr:
                if i == self.k:
                    print (self.arr.index(i))
                    break

array = Solution([1, 2, 3, 4, 5], 4)
array.search()

array2 = Solution([11, 22, 33, 44, 55], 445)
array2.search()

array3 = Solution([1, 1, 1, 1, 2], 1)
array3.search()
