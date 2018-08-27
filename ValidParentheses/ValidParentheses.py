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
        container = []
        if len(self.input) % 2 == 1 or len(self.input) == 0:
            return False
        for parentheses in self.input:
            if parentheses in self.container:
                container.append(parentheses)
            elif len(container) == 0 or self.container[container.pop()] != parentheses:
                return False
        return len(container) == 0


if __name__ == '__main__':
    input = "()"
    valid_parentheses_obj = ValidParentheses(input)
    print(valid_parentheses_obj.valid_parentheses())
