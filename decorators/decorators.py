def inspect(func, *args):## any nubmer of arguments
    print(f"Running {func.__name__}")
    val = func(*args)
    print(val)
    return(val)

def combine(a,b):
        return(a+b)

def sub(x,y,z):
    return(x-y-z)