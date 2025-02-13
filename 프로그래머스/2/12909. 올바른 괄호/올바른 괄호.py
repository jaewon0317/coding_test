#효율성 통과 못한 코드..
# def solution(s):
#     s = s.replace('(','0')
#     s = s.replace(')','1')
#     s = list(s)
#     for i in range(len(s)):
#         s[i] = int(s[i])
#     while len(s) != 0: # 배열의 길이가 0이 아니면 반복
#         if s[0] == 1: #닫는 괄호로 시작할때 false 반환
#             return False
#         else:# 열리는 괄호로 시작할때 
#             if 1 in s:
#                 for i in range(len(s)):
#                     if s[i] == 1:
#                         del(s[i])
#                         del(s[0])
#                         break
#             else: return False 
#     return True
# 
def solution(s):
    temp = 0
    for i in range(len(s)):
        if temp > 0 : return False
        if s[i] == '(':
            temp += -1
        else:
            temp += 1
    if temp == 0 :return True
    else: return False