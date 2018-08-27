# Input: "()"
# Output: true


class ValidParentheses:

    def __init__(self, input):
        self.input = input
        try:
            self.container = {k: v for k, v in (('(', ')'), ('{', '}'), ('[', ']'))}
        except Exception as e:
            print(e)

    def valid_parentheses(self):
        index = 0
        container = ""
        if len(self.input) % 2 == 1 or len(self.input) == 0:
            return False
        if self.input[0] not in self.container:
            return False
        while index < len(self.input):
            if self.container[self.input[index]] == self.input[index + 1]:
                container = container + self.input[index]
                container = container + self.input[index + 1]
                index = index + 2
            else:
                return False
        if container == self.input:
            return True
        else:
            return False


if __name__ == '__main__':
    input = "{[]}"
    valid_parentheses_obj = ValidParentheses(input)
    print(valid_parentheses_obj.valid_parentheses())