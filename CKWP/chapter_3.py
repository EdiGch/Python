from contracts import contract
import numpy


@contract(a=int, b='int,>0')
def my_sum(a, b):
    return a + b


my_sum("text", 1)
my_sum(1, 0)
