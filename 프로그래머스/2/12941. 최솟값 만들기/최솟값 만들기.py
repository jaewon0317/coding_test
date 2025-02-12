# 내가 짠 코드 논리는 맞지만 효율성에 문제가 있다.
# from itertools import permutations
# def solutions(A,B):
#     arr = [i+1 for i in range(len(A))]
#     r = len(A)
#     permu = list(permutations(arr, r))
#     print(permu)
#     muls = []
#     for i in A:
#         temp = []
#         for j in B:
#             temp.append(i*j)
#         muls.append(temp)
#     ans_list = []
#     print(muls)
#     for i in permu:
#         temp = 0
#         print(i)
#         for j in range(len(A)):
#             temp += muls[j][i[j]-1]
#         ans_list.append(temp)
#     return max(ans_list)
# solutions([1,2,3],[4,5,6]) 
def solution(A, B):
    A.sort()  
    B.sort(reverse=True)  
    return sum(a * b for a, b in zip(A, B))