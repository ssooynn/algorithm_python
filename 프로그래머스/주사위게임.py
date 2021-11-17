def solution(monster, S1, S2, S3):
    total_cases = 0
    no_monster_cases = 0
    
    for i in range(1, S1+1):
        for j in range(1, S2+1):
            for k in range(1, S3+1):
                total_cases += 1
                if not i+j+k+1 in monster:
                    no_monster_cases += 1
            
    return int(no_monster_cases/total_cases * 1000)
