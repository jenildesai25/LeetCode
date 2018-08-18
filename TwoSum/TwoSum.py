# nums = [2,7,9,11]
# target = 9


class TwoSum:

    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def two_sum_naive_approach(self):
        for i in range(len(self.nums)):
            for j in range(1, len(self.nums)):
                if self.target - self.nums[i] == self.nums[j]:
                    return i, j

    def two_sum_optimize(self):
        pass


if __name__ == '__main__':
    nums = [2, 7, 9, 11]
    target = 9
    two_sum_obj = TwoSum(nums, target)
    print(two_sum_obj.two_sum_naive_approach())
