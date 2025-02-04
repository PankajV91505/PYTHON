def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')
        
print_kwargs(name="shaktiman" , power= "lazer")
print_kwargs(name="shaktiman" , power= "lazer", age= 25)
print_kwargs(name="shaktiman" , power= "lazer", age= 25, city= "mumbai" , emamy ="Dr.jackal")