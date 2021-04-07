
    
    


def darts(n):
    target = n
    a1 = list(range(1,21))
    a1.append(25)
    a2 = list(range(2,41,2))
    a2.append(50)
    a3 = list(range(3,61,3))
    a1.extend(a2)
    a1.extend(a3)
    array = list(set(a1)) 

    if n > 170:
        return []
    possibilities = []

    def calc_possibilities(i, j, pos):
        print(pos)
        s = sum(pos)

        if s == n:
            if pos[-1]%2 == 0:
                possibilities.append(pos)
            pos = []
        if s >= target or j == 3:
            pos = []
        if i == len(array):
            return
        pos.append(array[i])
        calc_possibilities(i+1, j+1, pos) 
    
    calc_possibilities(0, 0, [])
        

darts(5)