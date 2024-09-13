def problem01():
    def f(n):
        return 3*n + 2

    c = 4
    n0 = 2
        
    def g(n):
        return n

    return f, g, c, n0


def problem02():
    def f(n):
        return 2*n*n + 3*n + 2

    c = 5
    n0 = 5
        
    def g(n):
        return n*n

    return f, g, c, n0


def problem03():
    def f(n):
        return 2*n*n*n + 3*n*n + 3*n + 3

    c = 5 
    n0 = 3
        
    def g(n):
        return n*n*n

    return f, g, c, n0


def problem04():
    def f(n):
        return 4*n + 5

    c = 5
    n0 = 2
        
    def g(n):
        return n

    return f, g, c, n0


def problem05():
    def f(n):
        return 2*(3**n) + 3*n 

    c = 8
    n0 = 2
        
    def g(n):
        return (3**n)

    return f, g, c, n0