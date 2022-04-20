#Kiểm tra số


#Kiểm tra số hoàn hảo
def so_hoan_hao(n):
    #tính tổng ước của n trong khoảng 1 đến n - 1:
    S = 0
    for i in range(1, n):
        if( n % i == 0 ):
            S += i

    #kiểm tra nếu S = n thì số đó là số hoàn hảo và ngược lại
    if( S == n):
        print(f'{n} là số hoàn hảo')
    else:
        print(f'{n} không phải là số nguyên tố')

#Kiểm tra số chính phương
def so_chinh_phuong(n):
    # kiểm tra trong phạm vi từ 1 đến n có số nào bình phương lên bằng n hay không:
    check = False
    for i in range(1, n + 1):
        if ( i**2 == n):
            check = True

    # kiểm tra nếu True thì số đó là số chính phương và ngược lại
    if (check == True):
        print(f'{n} là số chính phương')
    else:
        print(f'{n} không phải là số chính phương')


#Kiểm tra số nguyên tố
def so_nguyen_to(n):
    flag = False
    if (n == 2):
        flag = True
    elif (n <= 1):
        flag = False
    elif (n % 2 == 0):
        flag == False
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                flag = False

    if (flag == True):
        print(f'{n} là số nguyên tố')
    else:
        print(f'{n} không phải là số nguyên tố')



