# 1. array 의 첫번째 원소를 answer 리스트에 넣는다
# 2. array 의 두번째 원소부터 하나씩 answer 리스트의 마지막 원소랑 비교후 값이 다르면 answer 리스트에 추가한다.
def solution(array):
    answer = [array[0]]
    for i in range(1,len(array)):
        if array[i] != answer[-1]:
            answer.append(array[i])
    return answer