#tính giai thừa bằng đệ quy
def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x - 1))

#tính giai thừa bằng khử đệ quy
def calc_factorial_non(x):
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result
