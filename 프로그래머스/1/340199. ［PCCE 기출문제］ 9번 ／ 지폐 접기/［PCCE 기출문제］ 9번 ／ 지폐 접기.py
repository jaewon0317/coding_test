def zero_one(size_x, size_y, b_size_x, b_size_y):
    x = [int(size_x >= b_size_x), int(size_y >= b_size_x)]
    y = [int(size_x >= b_size_y), int(size_y >= b_size_y)]
    return x, y

def solution(wallet, bill):
    size_x, size_y = wallet
    b_size_x, b_size_y = bill
    
    count = 0  # 반복 횟수
    
    while True:
        x, y = zero_one(size_x, size_y, b_size_x, b_size_y)

        # "2차원 배열의 대각선"이 [1,1]인지 확인
        if x[0] == 1 and y[1] == 1:
            return count 
        elif x[1]== 1 and y[0]==1:
            return count

        if b_size_x >= b_size_y:
            b_size_x //= 2
        else:
            b_size_y //= 2
        count += 1