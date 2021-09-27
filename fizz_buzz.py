class Number:
    def __init__(self, value):
        self.value = value

    def get_fizz_buzz_representation(self):
        if self.value % 3 == 0:
            return 'Fizz'
        if self.value % 5 == 0:
            return 'Buzz'
        if self.value % 7 == 0:
            return 'Baz'
        return self.value



def fizz_buzz(number):
    number = Number(number)

    return number.get_fizz_buzz_representation()
