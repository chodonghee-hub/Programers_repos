# Quiz from : https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    bFlag = True
    cnt = 0

    while bFlag:
        div = 3**cnt
        if n//div != 0:
            cnt += 1
        else :
            bFlag = False

    ls = [0] * cnt
    for idx in range(cnt-1, -1, -1):
        div = 3**idx
        tmp = n//div
        ls[len(ls)-1-idx] = tmp
        n -= div*tmp

    ls = [(3**idx)*ls[idx] for idx in range(len(ls))]
    return sum(ls)

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

    tc_n = [45, 125]
    tc_rs = [7, 229]
    compare([solution(tc_n[idx]) for idx in range(2)], tc_rs)












