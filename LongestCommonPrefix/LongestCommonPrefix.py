# Input: ["flower","flow","flight"]
# Output: "fl"


class LongestCommonPrefix:
    def __init__(self, input):
        self.input = input

    def longest_common_prefix(self):
        if len(self.input) == 0:
            return False
        if len(self.input) == 1:
            return self.input
        self.input.sort()
        first = self.input[0]
        last = self.input[-1]
        i = 0
        container = ""
        while i < len(first) and i < len(last) and first[i] == last[i]:
            container = container + first[i]
            i = i + 1
        if not container:
            return False
        return container


if __name__ == '__main__':
    input = ["flower", "flow", "flight"]
    longest_common_prefix_obj = LongestCommonPrefix(input)
    print(longest_common_prefix_obj.longest_common_prefix())
