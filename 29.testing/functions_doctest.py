def contains_purple(*args):
    '''
    >>> contains_purple(25,2,4,'hello')
    False
    >>> contains_purple(25,2,4,'hello','purple')
    True
    >>> contains_purple(color='purple')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: contains_purple() got an unexpected keyword argument 'color'
    '''
    if "purple" in args:
        return True
    return False
