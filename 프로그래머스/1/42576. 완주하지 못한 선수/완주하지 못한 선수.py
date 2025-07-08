def solution(participant,completion):
    # for name in completion:
    #     participant.remove(name)
    # return participant[0]
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if i == len(participant)-1:
            return participant[i]
        elif participant[i] != completion[i]: 
            return participant[i]
 