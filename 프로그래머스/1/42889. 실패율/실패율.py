# 1. 자기 자신보다 낮은 숫자 제외
# 2. 자기 자신과 같은 수의 갯수/자기 자신과 같거나 높은 숫자들의 갯수
# 3. key 기준으로 내림차순 정렬
def solution(N, stages):
    error_rate={}
    for i in range(1,N+1):
        i_num=0
        i_bigger_num=0
        for j in stages:
            if j == i:
                i_num +=1
            elif j > i:
                i_bigger_num +=1
        if i_bigger_num+i_num == 0:
            error_rate[i]= 0
        else:
            error_rate[i]=i_num/(i_bigger_num+i_num)
    print(error_rate)
    sorted_keys_get = sorted(error_rate, key=error_rate.get, reverse=True)
    return sorted_keys_get