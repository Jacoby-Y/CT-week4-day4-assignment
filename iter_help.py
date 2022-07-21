def first_match(func, iterable):
    for item in iterable:
        if func(item) == True:
            return item
    return None