# Quiz from : https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    return 45 - sum(numbers)

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

    tc_numbers = [[1,2,3,4,6,7,8,0], [5,8,4,0,6,7,9]]
    testCaseArr_result = [14, 6]

    compare([solution(tc_numbers[idx]) for idx in range(2)], testCaseArr_result)









