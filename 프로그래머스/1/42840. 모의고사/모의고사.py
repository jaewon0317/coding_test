def solution(answers):

    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    a_count = 0
    b_count = 0
    c_count = 0
    
    for i in range(len(answers)):
        if a[i % len(a)] == answers[i]:
            a_count += 1
        if b[i % len(b)] == answers[i]:
            b_count += 1
        if c[i % len(c)] == answers[i]:
            c_count += 1
      
    if a_count > b_count and a_count > c_count:
        answer = [1]
    elif b_count > a_count and b_count > c_count:
        answer = [2]
    elif c_count > a_count and c_count > b_count:
        answer = [3]
    elif a_count == b_count and a_count > c_count:
        answer = [1,2]
    elif a_count == c_count and a_count > b_count:
        answer = [1,3]
    elif b_count == c_count and b_count > a_count:
        answer = [2,3]
    else:
        answer = [1,2,3]
    return answer