def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        temp_lst = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr2)):
                temp += arr1[i][k] * arr2[k][j]
            temp_lst.append(temp)
        answer.append(temp_lst)

    return answer