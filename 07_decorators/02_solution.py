def debug (func):
    def wrapper(*args, **kwargs):
        arg_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f'{key}={value}' for key, value in kwargs.items())
        print(f'Function {func.__name__} called with arguments {arg_value} and keyword arguments {kwargs_value}')
        return func(*args, **kwargs)
        
    
    return wrapper
    
    
@debug
def hello():
    print('Hello!')
    
@debug
def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}!')
    
hello()
greet('chai', greeting='Good morning')

    