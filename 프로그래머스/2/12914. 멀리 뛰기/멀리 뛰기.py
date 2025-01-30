def mul(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

def same_permutation(one,two):
    return mul(one+two)//(mul(one)*mul(two))

def solution(n):
    one = n 
    two = 0
    ans = 0
    for i in range(n//2 + 1):
        ans += int(same_permutation(one,two))
        one -= 2
        two += 1
    return ans%1234567