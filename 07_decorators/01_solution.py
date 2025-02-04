import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} ran in  {end - start} time")
        return result
    return wrapper


@timer
def exmple_function(n):
    time.sleep(n)
    
    
exmple_function(2)