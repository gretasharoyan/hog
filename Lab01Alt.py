def falling(n, k):

    if n == k + 1:
        return n
    else:
        return n * falling(n-1,k)
