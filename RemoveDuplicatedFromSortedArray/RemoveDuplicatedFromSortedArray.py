# nums = [0,0,1,1,1,2,2,3,3,4],
class RemoveDuplicatedFromSortedArray:

    def __init__(self, input):
        self.input = input

    def remove_duplicated_from_sorted_array(self):
        if not self.input:
            return 0
        count = 0
        for i in range(len(self.input)):
            if self.input[count] != self.input[i]:
                count = count + 1
                self.input[count] = self.input[i]
        return count + 1


if __name__ == '__main__':
    input = [1, 1, 2, 2, 3, 4, 5, 1]
    remove_duplicated_from_sorted_array_obj = RemoveDuplicatedFromSortedArray(input)
    print(remove_duplicated_from_sorted_array_obj.remove_duplicated_from_sorted_array())
