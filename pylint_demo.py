'''
It has two simple functions sum_two_numbers and hello.
Then it runs hello function twice.
'''

def sum_two_numbers(a, b):
    '''
    It takes two numbers and returns the sum of the two numbers
    '''
    return a + b


def hello(name):
    '''
    It prints "Hello, " and the passed name, concatenated
    '''
    print(f"Hello, {name}!")


hello("Alice")
hello("John")
