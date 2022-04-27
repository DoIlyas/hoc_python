#Chương trình giải phương trình bậc 2
print('\n')
print('Chương trình giải phương trình bậc 2 ax^2 + bx + c = 0')

import math

print('Mời nhập a:')
a = int(input())
print('Mời nhập b:')
b = int(input())
print('Mời nhập c:')
c = int(input())

delta = b*b - 4*a*c

while True:
    if a == 0 and b != 0:
        print('Phương trình bậc hai ax^2 + bx + c = 0 trở thành phương trình bậc nhất ax + b = 0')
        x = -c / b
        print(f'Phương trình có 1 nghiệm duy nhất x = {x}.')
        if delta < 0:
            print('Phương trình vô nghiệm!')
        if delta == 0:
            xc = -b / (2 * a)
            print(f'Phương trình có nghiệm kép x1 = x2 = {xc}.')
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print(f'Phương trình có hai nghiêm:\n x1 = {x1}\n x2 = {x2}')
    elif b == 0:
        print("b phải khác 0. Mời nhập lại b.")
        b = int(input())
    else:
        break






