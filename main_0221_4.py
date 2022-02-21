# Quiz from : https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    return sum([price * idx for idx in range(1, count+1)]) - money if sum([price * idx for idx in range(1, count+1)]) >= money else 0

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

    tc_price = 3
    tc_money = 20
    tc_count = 4
    testCaseArr_result = 10

    compare([solution(tc_price, tc_money, tc_count)], [testCaseArr_result])











