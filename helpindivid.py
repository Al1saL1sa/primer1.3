def fun1(a, t):
    if t == 0:
        x = a / 2
    else:
        x = a
    def fun2(b):
        nonlocal x
        return b * x
    return fun2
