# import Dequi
#
# print('Nhập vào 1 số: ')
# num = int(input())
#
# print(f'Giai thừa của {num} là: ')
# print(Dequi.calc_factorial(num))
#
# print(f'Sau khi khử đệ quy:')
# print(Dequi.calc_factorial_non(num))


n = int(input('Mời nhập số phần tử trong mảng: '))

try:
    if n <= 0:
        exit()
except:
    print('Phải nhập số tự nhiên!')
    exit()

my_list = []
prompt = '> '

for i in range(n):
    my_list.append((input(prompt + f'Mời nhập số thứ {i + 1}: ')))

print('Danh sách các số nguyên vừa nhập: ', my_list)

#ép kiểu sang int
my_list_int = []

for i in my_list:
    my_list_int.append(int(i))

list_even = list(filter(lambda x : (x % 2 == 0), my_list_int))
print('Danh sách các số chẵn có trong mảng vừa nhập:', list_even)