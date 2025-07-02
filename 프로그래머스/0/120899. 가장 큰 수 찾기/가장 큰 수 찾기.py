# def solution(array):
#     for index,value in enumerate(array):
#         if value == max(array):
#             result = [value,index]
#             return result

def solution(array):
    max_value = max(array)
    index = array.index(max_value)
    return [max_value, index]
