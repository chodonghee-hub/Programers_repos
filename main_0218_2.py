# Quiz from : https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    ArrAlpha_dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    ArrAlpha = [idx for idx in ArrAlpha_dic.keys()]
    tmp = []
    now_read = 0
    while (now_read+1 <= len(s)):
        if s[now_read].isdigit() :
            tmp.append(s[now_read])
            now_read += 1
        else :
            rs = recallsive_func(s[now_read:], ArrAlpha, 0)
            tmp.append(ArrAlpha_dic[rs])
            now_read += len(rs)
    return int(''.join(tmp))

def recallsive_func(message, ls, n):
    if len(ls) == 1 :
        return ls[0]
    tmp = []
    for idx in ls :
        if idx[n] == message[0] :
            tmp.append(idx)
    return recallsive_func(message[1:], tmp, n+1)

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
    testCaseArr_sample = ["one4seveneight", "23four5six7", "2three45sixseven", "123"]
    testCaseArr_result = [1478, 234567, 234567, 123]

    rs = [solution(idx) for idx in testCaseArr_sample]

    print(rs)







