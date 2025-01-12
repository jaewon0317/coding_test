def solution(bandage, health, attacks):
    
    skill_time = bandage[0]
    health_per_sec = bandage[1]
    skill_bonus = bandage[2]
    
    max_health = health
    
    max_time = attacks[-1][0]
    
    #공격 받는 시간 리스트
    attack_time= [] 
    for attack in attacks:
        attack_time.append(attack[0])
   
    attack_num = 0
    skill_time_count = 0 
    for time in range(1,max_time+1):
        if time in attack_time: # 공격 받을때
            health -= attacks[attack_num][1]
            attack_num += 1
            skill_time_count = 0
            if health <= 0:
                return -1
        else: # 공격 받지 않을때
            health += health_per_sec
            skill_time_count += 1
            if health >= max_health:
                health = max_health
            # 스킬 추가 효과 발생시
            if skill_time_count == skill_time:
                health += skill_bonus
                skill_time_count = 0
                if health >= max_health:
                    health = max_health
    
    answer = health
    return answer
