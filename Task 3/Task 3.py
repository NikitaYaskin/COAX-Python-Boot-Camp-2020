import time

def time_takes(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start)* 1000) + "mil seconds")
        return result
    return wrapper

@time_takes
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result

arr = range(1, 100000)
square = calc_square(arr)
