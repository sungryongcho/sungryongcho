import math
def solution(arr):
    answer = arr[0]
    for n in arr:
        answer = (n*answer) // math.gcd(n,answer)
        print(answer)
    return answer
