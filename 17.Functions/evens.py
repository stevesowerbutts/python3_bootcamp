# Generate even numbers using list comprehension
def generate_evens():
    '''
    >>> generate_evens()
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
    '''
    evens = [num for num in range(1,50) if num % 2 == 0]
    return evens
print(generate_evens())
