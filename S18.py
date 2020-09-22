def repeat_digits(n):
    """Given a positive integer N, returns a number with each digit repeated.
    >>> repeat_digits(1234)
    11223344
    """
    last, rest = n%10, n//10
    if n<10:
    return n*10+n
    return repeat_digits(rest) * 100 + last+10*last


def eight_path(t):
    """Returns a path of the labels from the root to a leaf whose sum is a multiple of eight,
    or return None if no path exists.
    >>> t1 = tree(5, [tree(2),
    tree(1, [tree(3),
    tree(2)])
    ])
    >>> eight_path(t1)
    [5, 1, 2]
    >>> t2 = tree(9, [t1])
    >>> eight_path(t2)
    [9, 5, 2]
    """
    def helper(t, path_so_far):
        _____________________________________________________________________________________
        if sum(path_so_far)%8 == 0:
            return path_so_far
        for _________________________________________________________________________________:
            result = ________________________________________________________________________
            if result:
                return ______________________________________________________________________
    return __________________________________________________________________________________
