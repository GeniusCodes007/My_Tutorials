


def mean(n):
    n_count = 0
    item = 0
    total = 0
    while n_count < n :
        item = float(input("'X': "))
        n_count += 1
        total = total + item

    if n_count == n:
        return total/n




def com_mean(n):
    n_count = 0
    sum_f = 0
    sum_fx = 0
    total = 0
    while n_count < n:
        x = float(input("X: "))
        f = float(input("f: "))
        fx = f * x
        sum_fx = sum_fx + fx
        sum_f = sum_f + f
        n_count += 1

    if n_count == n:
        return sum_fx / sum_f



def com_mean_dev(n):
    n_count = 0
    sum_f = 0
    sum_fx = 0
    com_m = com_mean(n)
    d = 0
    while n_count < n:
        x = float(input("x: "))
        f = float(input("f: "))
        fx = f * abs(x - com_m)
        sum_fx = sum_fx + fx
        sum_f = sum_f + f
        n_count += 1

    if n_count == n:
        return sum_fx / sum_f


def mean_dev(n):
    n_count = 0
    x = 0
    sum_x = 0
    m = mean(n)
    d = 0

    while n_count < n :
        x = float(input("x: "))
        sum_x = sum_x + x
        d = d + abs(x - m)
        n_count += 1


    if n_count == n:
        return d/n


def Variance(n):
    n_count = 0
    x = 0
    sum_x = 0
    m = mean(n)
    d = 0
    vans = 0

    while n_count < n:
        x = float(input("x: "))
        sum_x = sum_x + x
        d = (x - m) ** 2
        vans = vans + d
        n_count += 1

    if n_count == n:
        return vans / n


#print(Variance(5))

def Com_Variance(n):
    n_count = 0
    x = 0
    sum_x = 0
    com_m = com_mean(n)
    vans = 0
    sum_f = 0
    sum_fx = 0

    while n_count < n:
        x = float(input("x: "))
        f = float(input("f: "))
        sum_f = sum_f + f
        d = (x - com_m) ** 2
        fx = f * d
        sum_fx = sum_fx + fx
        vans = vans + d
        n_count += 1

    if n_count == n:
        return sum_fx / sum_f



def Std_dev(n):
    vans = Variance(n)
    std = vans ** 0.5
    return std


def Com_Std_Dev(n):
    try:
        vans = Com_Variance(n)
        std = vans ** 0.5
        return std
    except ValueError:
        return "Check Your Values"


def root_mean_square(n):
    n_count = 0
    sum_square = 0

    while n_count < n:
        x = float(input("x:"))
        square_x = x ** 2
        sum_square = sum_square + square_x
        n_count += 1

    if n_count == n:
        mean = sum_square / n
        root = (mean) ** 0.5
        return root

print(root_mean_square(2))


