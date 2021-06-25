
def fun(dist):
    pf = 0.9
    fact = [(1 / (i ** pf)) for i in range(1, dist + 1)]
    coeff = sum(fact)
    return (coeff * (dist ** pf))

def f2(dist):
    return (dist ** 1.43 + dist ** 1.44) / 1.98


for i in range(1,10):
    print(fun(i),f2(i))
    # print()