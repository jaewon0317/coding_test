def solution(s):
    splited = s.split(' ')
    for i in range(len(splited)):
        splited[i] = int(splited[i])
    return str(min(splited))+str(' ') +str(max(splited))