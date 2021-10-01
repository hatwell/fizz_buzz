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

# certain kind of relationship between two sets of values
# domain // co-domain
# in fizz buz the domain is (positive, non-zero ) integers. the co-domain is strings (and integers) 
# this is a lookup 
# a function is a fact
# ths is a specificatio for a machine that will do a lookup 
# instead of a sequnece of instructions, a combination of statements (facts)
# program text con build up structure of context and at runtime information flows thru
# "evaluatios in a context"
# shape of context && sequence of evaluations 
# facts can be generic / paramaterized 
# arguments to a functions as pronouns
# "combinations of parameterized statements"
