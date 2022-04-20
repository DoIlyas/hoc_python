#Tính tổng S(n) = 1 + 2 + 3 + ... + n. N nhập từ bàn phím.

print('Chương trình tính tổng S(n) = 1 + 2 + 3 + ... + n.')

S = 0
n = 0

print('Mời nhập n: ')
n = int(input())

print(f'Với n = {n} ta có:')

for i in range(0, n + 1):
    S = S + i

print(f'Tổng S(n) = {S}')

