def DivHalving(x,y):
    if x == 0:
        return (0,0)
    (qp,rp) = DivHalving(x//2,y)
    if x > 0 and x % 2 == 0 and 2*rp<y:
        return (2*qp,2*rp)
    elif x > 0 and x % 2 == 0 and 2 * rp >= y:
        return (2 * qp+1, (2 * rp)-y)
    elif x > 0 and x % 2 == 1 and (2 * rp) +1 < y:
        return (2 * qp, (2 * rp)+1)
    else:
        return (2 * qp+1, (2 * rp)-y+1)

print(DivHalving(61,3))