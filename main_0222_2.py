# Quiz from : https://programmers.co.kr/learn/courses/30/lessons/12977

import math

def solution(nums):
    set(nums)
    rs = []
    recallsive_func(sorted(nums), [], rs)
    return len([idx for idx in rs if checkNum(sum(idx)) == True])
    return len(rs)

def recallsive_func(nums, tmp, rs):
    tmp.sort()
    if len(tmp) == 3 :
        if tmp not in rs and checkNum(sum(tmp)) == True:
            rs.append(tmp)
        return

    for idx in range(len(nums)) :
        recallsive_func(nums[:idx] + nums[idx+1:], tmp + [nums[idx]], rs)

def checkNum(n):
    for idx in range(2, int(math.sqrt(n))+1):
        if n%idx == 0 :
            return False
    return True

def compare(myResultArr, _result_Arr):
    score = 0
    for _idx1, _idx2 in zip(myResultArr, _result_Arr):
        if _idx1 == _idx2:
            score += 1
        else :
            print("=====================================")
            print("** error \nmy idx    : {}\ntCase     : {}".format(_idx1, _idx2))
    print("** score : {}".format(score))

if __name__ == '__main__':

    tc_nums = [[1,2,3,4],[1,2,7,6,4]]

    testCaseArr_result = [1, 4]

    compare([solution(tc_nums[idx]) for idx in range(2)], testCaseArr_result)
    # solution(tc_nums[0])












