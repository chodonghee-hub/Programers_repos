def solution(new_id):

    # length : 3 ~ 15
    # special index : - , _ , .
    # index (. ) can't repeated
    # index (. ) can't use at head and tail
    # if index (. ) used at head and tail -> delete
    # all the index is lower case ( check alpha , check upper case index )
    # after satisfied all the requirements
    # if length of id <= 2, repeat last word until length 3

    ls = [idx for idx in new_id if idx in ['.', '-', '_'] or idx.isalpha() or idx.isdigit()]
    tmp = []

    # upper -> lower
    for idx in range(len(ls)):
        if ls[idx].isalpha() and ls[idx].isupper() :
            ls[idx] = ls[idx].lower()

    # remove repeated '.' idx
    if len(ls) >= 2:
        for idx1, idx2 in zip(ls[:-1], ls[1:]):
            if idx1 == '.' and idx1 == idx2 :
                pass
            else :
                tmp.append(idx1)
        tmp.append(ls[-1])
    else :
        tmp = ls

    # delete '.' from head and tail
    try :
        tmp = RemoveIdxFrom(tmp)
    except:
        pass

    # check empty spaces , return
    if not tmp :
        return 'aaa'
    elif tmp :
        if len(tmp) < 3 :
            idx = tmp[-1]
            return ''.join(tmp+[(3-len(tmp))*tmp[-1]])
        else :
            tmp = tmp if len(tmp) <= 15 else tmp[:15]
            tmp = RemoveIdxFrom(tmp)
            return ''.join(tmp)

def RemoveIdxFrom(tmp):
    while (tmp[0] == '.' or tmp[-1] == '.'):
        if tmp and tmp[0] == '.':
            del tmp[0]
        elif tmp and tmp[-1] == '.':
            del tmp[-1]
    return tmp

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
    testCase = "...!@BaT#*..y.abcdefghijklm"
    testCaseArr_sample = ["...!@BaT#*..y.abcdefghijklm","z-+.^.","=.=","123_.def","abcdefghijklmn.p", "b"]
    testCaseArr_result = ["bat.y.abcdefghi","z--","aaa","123_.def","abcdefghijklmn", "bbb"]

    rs = [solution(idx) for idx in testCaseArr_sample]

    compare(rs, testCaseArr_result)





