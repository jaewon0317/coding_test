def solution(fees, records):
    answer = []
    car_dict = {}
    for i in range(len(records)):
        time = records[i][0:5]
        min = int(time[:2])*60 + int(time[3:])
        car_num = records[i][6:10]

        # car_state = records[i][10:13]

        if car_num not in car_dict:
            car_dict[car_num]=[min]
        else:
            car_dict[car_num].append(min)

    def fee_calculator(fees,min_stayed):
        basic_min = fees[0] #기본 시간
        basic_fee = fees[1] #기본 요금
        chunck_time = fees[2] #단위 시간
        chunck_fee = fees[3] #단위 요금
        x = min_stayed - basic_min


        if min_stayed <= basic_min:
            return basic_fee
        else:
            if x % chunck_time == 0:
                return basic_fee + (x // chunck_time)*chunck_fee
            else:
                return basic_fee + ((x // chunck_time)+1)*chunck_fee

    answer = []

    for key, value in sorted(car_dict.items()):
        print(key, value)

        min_stayed=0
        # 전체 시간 계산
        if len(value)%2 == 1:
            min_stayed += 23*60+59-value[-1] # 23:59 분 까지 계산

        for i in range((len(value)//2)):
             min_stayed += value[2*i+1]-value[2*i]
        total_fee = fee_calculator(fees,min_stayed)
        answer.append(total_fee)
    return answer