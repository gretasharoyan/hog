# def same_digits(a, b):
#     if a == b:
#         return True
#     if (a//10)% 10 == a%10:
#         return same_digits(a//10, b)
#     if (b//10)% 10 == b%10:
#         return same_digits(a, b//10)
#     else:return False




def unique_largest(n):

    assert n > 0
    top = 0
    while n:
        n, d = n // 10, n % 10
        if d > top:
            top, unique = d, True
        elif d == top:
            unique = False
    return unique
