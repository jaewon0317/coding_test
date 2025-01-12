def time_to_sec(time):
    minute = time[0:2]
    second = time[3:]
    sec = int(minute) * 60 + int(second)
    return sec

def solution(video_len, pos, op_start, op_end, commands):
    
    video_len = time_to_sec(video_len)
    pos = time_to_sec(pos)
    op_start = time_to_sec(op_start)
    op_end = time_to_sec(op_end)
    
    if op_start <= pos <= op_end:
        pos = op_end
    
    result = pos
    for i in range(len(commands)):

        if commands[i] == "next":
            result += 10
            if op_start <= result < op_end:
                result = op_end
            elif result > video_len:
                result = video_len
        elif commands[i] == "prev":
            result -= 10
            if op_start <= result < op_end:
                result = op_end
            elif result < 0:
                result = 0
        if op_start <= result <=op_end:
            result = op_end
    min = result//60
    sec = result%60
    answer = str(min).zfill(2) + ":" + str(sec).zfill(2)
    return answer