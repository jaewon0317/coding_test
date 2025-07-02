def solution(array):
    for index,value in enumerate(array):
        if value == max(array):
            result = [value,index]
            return result