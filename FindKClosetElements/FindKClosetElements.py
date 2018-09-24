# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]


class FindKClosetElement:

    def __init__(self, input, k, x):
        self.input = input
        self.k = k
        self.x = x

    def find_k_closet_element(self):
        if not self.input or self.k <= 0:
            return []
        while len(self.input) > self.k:
            if abs(self.input[0] - self.x) > abs(self.input[-1] - self.x):
                self.input.pop(0)
            else:
                self.input.pop(-1)
        return self.input


if __name__ == '__main__':
    input_data = [0, 0, 1, 2, 3, 3, 4, 7, 7, 8]
    k = 3
    x = 5
    find_k_closet_element = FindKClosetElement(input_data, k, x)
    print(find_k_closet_element.find_k_closet_element())
