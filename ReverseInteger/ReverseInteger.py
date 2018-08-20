# input = 123
# output = 321


class ReverseInteger:

    def __init__(self, input):
        self.input = input

    def reverse_integer(self):
        flag = False
        answer = 0
        if self.input < 0:
            flag = True
            self.input = 0 - self.input
        while self.input:
            answer = answer + (self.input % 10) * 10 ** (len(str(self.input)) - 1)
            self.input = self.input // 10
        if flag:
            answer = 0 - answer
        return answer


if __name__ == '__main__':
    input = 120
    reverse_integer_obj = ReverseInteger(input)
    print(reverse_integer_obj.reverse_integer())
