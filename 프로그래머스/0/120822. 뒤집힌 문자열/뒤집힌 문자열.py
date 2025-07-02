def solution(my_string):
    new_string = ''
    for i in range(len(my_string)):
        new_string += my_string[-(i+1)]
    return new_string