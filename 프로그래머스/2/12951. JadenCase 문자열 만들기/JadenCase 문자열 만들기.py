def solution(s):
    s_splitted = s.split(' ')
    ans = ''
    for i in range(len(s_splitted)):
        if s_splitted[i] == '':
            ans += ' '
        elif i == len(s_splitted) - 1:
            ans += s_splitted[i].capitalize()
        else:
            ans += s_splitted[i].capitalize() + ' '
    if s_splitted[-1] == '':
        ans = ans[:-1]
    return ans