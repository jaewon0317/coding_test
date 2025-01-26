def solution(phone_number):
    phone_number = list(phone_number)
    phone_back = phone_number[-4:]
    temp = ''
    for i in phone_back:
        temp += str(i)
    answer = (len(phone_number) - 4)*'*' + temp
    return answer