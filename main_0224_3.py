# Quiz from : https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sz):
    for n, idx in enumerate(sz) :
        x, y = idx
        sz[n] = [y, x] if y > x else [x, y]
    return max([idx[0] for idx in sz]) * max([idx[1] for idx in sz])

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

    tc_sz = [[[60, 50], [30, 70], [60, 30], [80, 40]],
             [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]],
             [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]],
             [[2, 1], [1, 1], [1, 1], [1, 3]],
             [[3, 2], [2, 2], [2, 1]],
             [[3, 1], [1, 1], [1, 1], [1, 3]],
             [[1, 1], [1, 1], [1, 1], [1, 1]],
             [[100, 1], [80, 90], [1, 1], [1000, 1], [1, 1]]]
    tc_rs = [4000, 120, 133, 3, 6, 3, 1, 80000]


    compare([solution(tc_sz[idx]) for idx in range(len(tc_rs))], tc_rs)
