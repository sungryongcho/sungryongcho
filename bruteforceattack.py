def brute_force_attack(T, P):
    num = 0
    for password in P:
        if password == T:
            print(T, "==", P[num])
            print(num+1, "attempt")
            return True
        else:
            print(T, "!=", P[num])
            num +=1
    return False



word = "attack"
P = ["python", "TSOM", "cybersecurity", "success", "brute", "force", "attack"]

a = brute_force_attack(word, P)

if a :
    print("success")
else :
    print("fail")

