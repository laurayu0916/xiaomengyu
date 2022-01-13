def solution(a):
    res = 0
    for i in range(len(a)):
        for j in range(len(a)):
            str1 = str(a[i])
            str2 = str(a[j])
            total = str1 + str2
            num = int(total)
            res += num
    return res

solution(8)
