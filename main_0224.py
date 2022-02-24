# Quiz from : https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    return min([idx for idx in range(1, n) if n%idx == 1])

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

    tc_n = [10, 12]
    tc_rs = [3, 11]
    compare([solution(tc_n[idx]) for idx in range(2)], tc_rs)












