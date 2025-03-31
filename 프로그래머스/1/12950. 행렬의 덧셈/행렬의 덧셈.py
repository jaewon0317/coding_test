def solution(arr1, arr2):
    rows = len(arr1)
    cols = len(arr1[0])
    answer = []
    for row in range(rows):
        answer.append([])
        for col in range(cols):
            answer[row].append(arr1[row][col] + arr2[row][col])
    return answer