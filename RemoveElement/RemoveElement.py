# Given nums = [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.


class RemoveElement:

    def __init__(self, nums, val):
        self.nums = nums
        self.val = val

    def remove_element(self):
        count = 0
        for i in range(len(self.nums)):
            if self.nums[i] != self.val:
                self.nums[count] = self.nums[i]
                count = count + 1
        return count


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    remove_element = RemoveElement(nums, val)
    print(remove_element.remove_element())
