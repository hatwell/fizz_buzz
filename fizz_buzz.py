import math

fizz_buzz_map = {
    1:1,
    2:2,
    3:'Fizz',
    4:4,
    5:'Buzz',
    6:'Fizz',
    7: 'Baz',
    8:8,
    9:'Fizz'
}



def prime_factors(n):
    factors = [1]
    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    for i in range(3,int(math.sqrt(n))+1,2):

        while (n % i == 0):
            factors.append(i)
            n = n / i
    if n > 2:
        factors.append(int(n))
    return list(filter(lambda x: x > 2 and x < 8, factors))

def fizz_buzz(value): 
    fizz_buzz_elements = list(map(lambda x: fizz_buzz_map.get(x),  prime_factors(value)))
    return " ".join(fizz_buzz_elements)




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
