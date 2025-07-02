# 1. 모든 경우의 수로 숫자 3개를 뽑고 더한다. ???? ok
# 2. 2이상의 숫자에서 자기 절반의 숫자까지 나눠지는 숫자가 없을때 true 있을때 False ok 
# 재귀함수네!
def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        one = nums[i]
        for j in range(i+1,len(nums)-1):
            two = nums[j]
            for k in range(j+1,len(nums)):
                three = nums[k]
                sum = one+two+three
                print(sum,end=':')
                
                num_divided = 0
                for z in range(2,sum//2 +1):
                    if sum % z ==0 :
                        num_divided += 1
                if num_divided == 0:
                    answer += 1
                print(num_divided)    
    return answer