def solution(s):
    s_splitted = s.split(' ')# 공백 기준으로 쪼갬
    ans = ''
    for i in range(len(s_splitted)):
        if s_splitted[i] == '': #공백이 연속될때의 처리
            ans += ' '
        elif i == len(s_splitted) - 1: # 마지막 문자열 처리
            ans += s_splitted[i].capitalize()
        else:
            ans += s_splitted[i].capitalize() + ' ' #문자열 처리
    if s_splitted[-1] == '':
        ans = ans[:-1]
    return ans
