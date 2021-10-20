import math

#extensional definition
#intentional definition is also a statement of a fact


fizz_buzz_index_lookup = {
    0:3,
    1:5,
    2:7
}



def get_modulii(value):
    # keys = filter(lambda key: key <= value, fizz_buzz_map.keys())
    mods =  [value % key for key in fizz_buzz_map.keys() ]
    


def fizz_buzz(value):
    fizz_buzz_map = {
        3:lambda x: 'Fizz',
        5:lambda x: 'Buzz',
        7: lambda x: 'Baz',
        0: lambda x: x
    } 
    return [fizz_buzz_index_lookup.get(i) for i,x in enumerate(get_modulii(value))]




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
