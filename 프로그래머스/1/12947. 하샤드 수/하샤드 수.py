# 1.숫자를 문자열로 변환
# 2.각 요소를 더함
# 3.숫자를 나눠서 0 인지 확인
def solution(x):
    x_str = str(x)
    x_str
    sum = 0
    for i in range(len(x_str)):
        sum += int(x_str[i])
    if x % sum ==0:
        return True
    else: 
        return False