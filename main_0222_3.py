# Quiz from : https://programmers.co.kr/learn/courses/30/lessons/77884

import math

def solution(left, right):
    ls = [idx for idx in range(left , right+1)]
    rs = [CheckDivisor(idx) for idx in ls]
    return sum(rs)

def CheckDivisor(n):
    rs = []
    for idx in range(1, int(math.sqrt(n))+1):
        if n%idx == 0 :
            rs.append(idx)
            rs.append(n//idx)
    rs = set(rs)
    return n if len(rs)%2 == 0 else n*-1

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

    tc_left = [13, 24]
    tc_right = [17, 27]

    testCaseArr_result = [43, 52]

    compare([solution(tc_left[idx], tc_right[idx]) for idx in range(2)], testCaseArr_result)












