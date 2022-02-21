# Quiz from : https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3

def solution(id_list, report, k):
    dic_count = {}
    dic_id = {}
    for idx in id_list:
        dic_count[idx] = []
        dic_id[idx] = 0

    for idx in report :
        idx = idx.split(' ')
        reported = idx[1]
        if idx not in dic_count[reported]:
            dic_count[reported].append(idx)

    for key, val in dic_count.items():
        if len(val) >= k:
            for info in val :
                dic_id[info[0]] += 1

    return [idx for idx in dic_id.values()]

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

    tc_id_list = [["muzi", "frodo", "apeach", "neo"],["con", "ryan"]]
    tc_report = [["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],["ryan con", "ryan con", "ryan con", "ryan con"]]
    tc_k = [2, 3]
    testCaseArr_result = [[2,1,1,0], [0,0]]

    compare([solution(tc_id_list[idx], tc_report[idx], tc_k[idx]) for idx in range(2)], testCaseArr_result)









