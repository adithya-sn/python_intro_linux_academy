def inspect(func):
    def wrapped_func(*args, **kwargs):
        print(f"Running {func.__name__}")
        val = func(*args, **kwargs)
        print(f"Result: {val}")
        return(val)
    return(wrapped_func)


@inspect##allows to call the function via inspect; combine(1,2) instead of inspect(combine,1,2)##
def combine(a,b):
        return(a+b)

def sub(x,y,z):
    return(x-y-z)