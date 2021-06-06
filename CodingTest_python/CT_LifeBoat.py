def solution(people, limit):
    answer = 0
    people.sort()

    while len(people) >= 1:
        if len(people) == 1:
            people.remove(people[0])
            answer += 1
        else:
            if people[0] + people[1] > limit:
                people.remove(people[0])
                answer += 1
            elif people[0] + people[1] == limit:
                people.remove(people[0])
                people.remove(people[1])
                answer += 1
            else:
                for i in range(2, len(people)):
                    if people[0] + people[i] > limit:
                        people.remove(people[0])
                        people.remove(people[i - 1])
                        answer += 1
                        break
                    elif people[0] + people[i] == limit:
                        people.remove(people[0])
                        people.remove(people[i])
                        answer += 1
                        break
                    else:
                        pass
    return answer

# 최대 2명, 무게 100 제한, 
# 구명보트 최대한 적게 사용하여 모든 사람 구출
# 효율성 개선해야 함