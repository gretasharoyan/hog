def parabola(x):
    """A parabola function (for testing the again function)."""
    return (x-3) * (x-6)
def vee(x):
    """A V-shaped function (for testing the again function)."""
    return abs(x-2)

def again(f):
    n = 1
    while n:
        m = 0
        while m<n:
            if f(m) == f(n):
                return n
            else:
                m+=1
        n+=1
