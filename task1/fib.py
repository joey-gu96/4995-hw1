def fib(x):
    l = []
    l.append(1)
    l.append(1)
    if x > 2:
        for i in range(x-2):
            l.append(l[i]+l[i+1])
    return l[-1]
