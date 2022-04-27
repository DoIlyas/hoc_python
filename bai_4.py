def xin_chao(name):
    """Hàm này sẽ hiển thị câu chào"""
    print(f'Xin chào, {name}, rất vui được gặp bạn!')


def so_nguyen_to(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                return False
    return True

for i in range(1, 101):
    if so_nguyen_to(i):
        print(i, end=' ')
