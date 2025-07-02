def solution(a, b, n):
    answer = 0
    while n // a !=0:
        new_bottles = n // a * b
        left_bottles = n % a
        answer += new_bottles
        n = new_bottles + left_bottles
    return answer