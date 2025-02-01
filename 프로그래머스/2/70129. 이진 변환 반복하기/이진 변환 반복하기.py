def solution(s):
    repeat = 0
    zeros = 0
    while '1' in s:
        if s == '1':
            return [repeat,zeros]
        else:
            before = len(s)
            s = s.replace('0','')
            after = len(s)
            zeros += before - after
            s = bin(len(s))[2:]
            repeat +=1