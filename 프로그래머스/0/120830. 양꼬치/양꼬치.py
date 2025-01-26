def solution(n, k):
    num = n//10
    drink = k - num
    
    price = n * 12000 + drink * 2000
    return price