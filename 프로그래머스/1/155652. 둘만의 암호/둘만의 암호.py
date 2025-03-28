


def solution(s, skip, index):
    answer = ''
    #1. alphabet 에서 skip 원소들 삭제
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    alphabet = [ch for ch in alphabet if ch not in skip]
    
    #2. 알파벳이 z를 넘어갈 경우를 위해
    alphabet_list = alphabet*2
    index = index % len(alphabet)
    
    #3. 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줌
    s_index = [alphabet.index(letter) for letter in s]
    for i in s_index:
        answer += alphabet_list[i+index]
    return answer