def rect(area, perimeter):
    """Return the longest side of a rectangle with area and perimeter that has integer sides.
    >>> rect(10, 14) # A 2 x 5 rectangle
    5
    >>> rect(5, 12) # A 1 x 5 rectangle
    5
    >>> rect(25, 20) # A 5 x 5 rectangle
    5
    >>> rect(25, 25) # A 2.5 x 10 rectangle doesn't count because sides are not integers
    False
    >>> rect(25, 29) # A 2 x 12.5 rectangle doesn't count because sides are not integers
    False
    >>> rect(100, 50) # A 5 x 20 rectangle
    20
    """
    side = 1
    while side * side <= area:
        other = round(perimeter - 2*side)
        if other*side==area and (2*other+2*side)==permiter:
            return other
        side = side + 1
    return False

def sequence(n, term):
    """Return the first n terms of a sequence as an integer.
    >>> sequence(6, abs) # Terms are 1, 2, 3, 4, 5, 6
    123456
    >>> sequence(5, lambda k: k+8) # Terms are 9, 10, 11, 12, 13
    910111213
    >>> sequence(4, lambda k: pow(10, k)) # Terms are 10, 100, 1000, 10000
    10100100010000
    """
    t, k = 0, 1
    while k<=n:
        m = 1
        x =  term(k)
________________________________________________________________________________ m <= x:
___________________________________________________________________________________
        t = t*10 + x
        k = k + 1
    return t


def repeat(k):
    """When called repeatedly, print each repeated argument.
    >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    """
    return detector(k)
    def detector(f):
        def g(i):
            if i in k:
                print(i)

            return repeat(k+[i])
        return g
