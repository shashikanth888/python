def ispowerten(num):
    while num > 1:
        if num%10 != 0:
            return False
        num /= 10
    if num==1:
        return True
    return False
        
def last_digit(n):
    q = [0,2,3,4,5,6,7,8,9]
    num = n
    if ispowerten(num):
        return None
    else:
        while len(q)!=1 :
            # print(q)
            digits = str(num)
            for i in digits:
                temp = int(i)
                # print(temp)
                if q.count(temp) > 0 and len(q)!=1:
                    q.remove(temp)
            num = num * n
        return q[0]

# print("op: ", last_digit(100000000))