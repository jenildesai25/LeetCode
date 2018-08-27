# number = 121
# answer = True


class PalindromeNumber:

    def __init__(self, number):
        self.number = number

    def palindrome_number(self):
        reverse_number = 0
        original_number = self.number
        if self.number < 0:
            return False
        while self.number:
            reverse_number = reverse_number + (self.number % 10) * 10 ** (len(str(self.number)) - 1)
            self.number = self.number // 10
        if reverse_number == original_number:
            return True
        else:
            return False


if __name__ == '__main__':
    number = 123
    palindrome_number_obj = PalindromeNumber(number)
    print(palindrome_number_obj.palindrome_number())