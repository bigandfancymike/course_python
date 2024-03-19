# Напишіть самостійно функції котрі буде повторювати поведінку built-in функції
# map
# filter

#map
def my_map(func, iterable):

    result = []
    for item in iterable:
        result.append(func(item))
    return result

#filter
def my_filter(func, iterable):

    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result
