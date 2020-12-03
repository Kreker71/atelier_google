import myModule

def your_function(*args, **kwargs):
    sum = 0
    for arg in args:
        if type(arg) == int or type(arg) == float:
            sum += arg
    return sum

# print(your_function(2, 4, 'abc', param_1=2))

def function():
    try:
        x = int(input())
        return x
    except ValueError:
        return 0

# print(function())

