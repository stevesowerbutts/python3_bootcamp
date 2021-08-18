
# Return Truth itens from a list:
# eg. compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]

def compact(items):
    return [a for a in items if a]


# Return true/false list of items from passed function
# eg.
# def isEven(num):
#     return num % 2 == 0

# partition([1,2,3,4], isEven) # [[2,4],[1,3]]

# Traditional:
def partition(items,func):
    truthy_list = []
    falsy_list = []
    for a in items:
        if func(a):
            truthy_list.append(a)
        else:
            falsy_list.append(a)
    return [truthy_list, falsy_list]

# List comprehension
def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]


# kwargs exercise
# Calculate Fucntion that accepts make_float, operation, message and numbers to calculate based on the operation
'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''
# First attempt:
def calculate(message="The result is", **kwargs):
    first = kwargs['first']
    second = kwargs['second']
    if kwargs['make_float']:
        first = float(first)
        second = float(second)
    operation = kwargs['operation']
    if operation == 'add':
        result = first + second
    elif operation == 'subtract':
        result = first - second
    elif operation == 'multiply':
        result = first * second
    else:
        result = first / second
    return "{0} {1}".format(message, result)

# Solution - use kwarg.get to handle None values
# Operation as a dict to reduce code
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final
