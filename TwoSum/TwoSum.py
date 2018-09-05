# nums = [2,7,9,11]
# target = 9


class TwoSum:

    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def two_sum_optimize(self):
        container = dict()
        for index, value in enumerate(self.nums):
            if self.target - value in container:
                return container[self.target - value], index
            container[value] = index


if __name__ == '__main__':
    nums = [2, 5, 5, 11]
    target = 10
    two_sum_obj = TwoSum(nums, target)
    print(two_sum_obj.two_sum_optimize())
