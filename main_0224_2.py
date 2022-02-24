# Quiz from : https://programmers.co.kr/learn/courses/30/lessons/12921

import math

def solution(n):
    return len([target for target in [idx for idx in range(2, n+1)] if checkNum(target) == True])

def checkNum(target):
    for div in range(1, int(math.sqrt(target)) + 1):
        if div != 1 and target % div == 0:
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

    tc_n = [10, 5]
    tc_rs = [4, 3]
    compare([solution(tc_n[idx]) for idx in range(2)], tc_rs)












