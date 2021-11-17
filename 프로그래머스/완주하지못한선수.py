def solution(participant, completion):
    participant.sort()
    completion.sort()
    for par, com in zip(participant[:-1], completion):
        if par != com:
            return par
        
    return participant[-1]
