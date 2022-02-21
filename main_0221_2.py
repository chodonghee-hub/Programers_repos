# Quiz from : https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    return sum([idx if flag == True else idx*-1 for idx, flag in zip(absolutes, signs)])

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

    tc_absolutes = [[4,7,12], [1,2,3]]
    tc_signs = [[True, False, True], [False, False, True]]
    testCaseArr_result = [9, 0]

    compare([solution(tc_absolutes[idx], tc_signs[idx]) for idx in range(2)], testCaseArr_result)










