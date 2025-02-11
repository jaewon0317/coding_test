def solution(msg):
    import string
    letter = string.ascii_uppercase
    letters = []
    for i in letter:
        letters.append(i)
    ans = []
    
    while len(msg) > 0:
        for i in range(len(letters),0,-1): 
            if msg[:len(letters[i-1])] == letters[i-1]:
                ans.append(i)
                letters.append(msg[:len(letters[i-1])+1])
                msg = msg[len(letters[i-1]):]
                break
    return ans