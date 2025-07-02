# # 1. 자기 자신보다 낮은 숫자 제외
# # 2. 자기 자신과 같은 수의 갯수/자기 자신과 같거나 높은 숫자들의 갯수
# # 3. key 기준으로 내림차순 정렬
# def solution(N, stages):
#     error_rate={}
#     stage_list = []
#     people = len(stages)
#     for i in range(1,N+1):
#         count = stages.count(i)
#         stage_list.append(count)
#     for i in range(N):
#         if people == 0:
#             error_rate[i+1] = 0
#         else :
#             error_rate[i+1] = stage_list[i]/people
#             people -= stage_list[i]
#     sorted_keys_get = sorted(error_rate, key=error_rate.get, reverse=True)
#     return sorted_keys_get

def solution(N, stages):
    error_rate={}
    stage_list = [0] * (N+2)
    people = len(stages)

    for stage in stages:
        stage_list[stage] += 1
    
    for i in range(1,N+1):
        if people == 0:
            error_rate[i] = 0
        else :
            error_rate[i] = stage_list[i]/people
            people -= stage_list[i]
    sorted_keys_get = sorted(error_rate, key=error_rate.get, reverse=True)
    return sorted_keys_get
