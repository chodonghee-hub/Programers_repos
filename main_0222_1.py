# Quiz from : https://programmers.co.kr/learn/courses/30/lessons/70128?language=python3

def solution(a, b):
    return sum([x*y for x, y in zip(a, b)])

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

    tc_a = [[1,2,3,4],[-1,0,1]]
    tc_b = [[-3,-1,0,2], [1,0,-1]]
    testCaseArr_result = [3, -2]

    compare([solution(tc_a[idx], tc_b[idx]) for idx in range(2)], testCaseArr_result)












