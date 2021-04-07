def darts(n):
    shot = [(1, '1'), (2, 'D1'), (3, 'T1'), (2, '2'), (4, 'D2'), (6, 'T2'), (3, '3'), (6, 'D3'), (9, 'T3'), (4, '4'), (8, 'D4'), (12, 'T4'), (5, '5'), (10, 'D5'), (15, 'T5'), (6, '6'), (12, 'D6'), (18, 'T6'), (7, '7'), (14, 'D7'), (21, 'T7'), (8, '8'), (16, 'D8'), (24, 'T8'), (9, '9'), (18, 'D9'), (27, 'T9'), (10, '10'), (20, 'D10'), (30, 'T10'), (11, '11'), (22, 'D11'), (33, 'T11'), (12, '12'), (24, 'D12'), (36, 'T12'), (13, '13'), (26, 'D13'), (39, 'T13'), (14, '14'), (28, 'D14'), (42, 'T14'), (15, '15'), (30, 'D15'), (45, 'T15'), (16, '16'), (32, 'D16'), (48, 'T16'), (17, '17'), (34, 'D17'), (51, 'T17'), (18, '18'), (36, 'D18'), (54, 'T18'), (19, '19'), (38, 'D19'), (57, 'T19'), (20, '20'), (40, 'D20'), (60, 'T20'), (25, '25'), (50, 'D25')]
    master = []

    def calc_poss(n, partial, partial_sum, i):
        if partial_sum == n and 'D' in partial[-1] and partial not in master:
            master.append(partial)
            return None
        if len(partial)<3 and partial_sum < n:
            new_partial = list(partial)
            new_partial_sum = partial_sum + shot[i][0]
            new_partial.append(str(shot[i][1])) ## use curr i
            calc_poss(n, new_partial, new_partial_sum, 0)      
            if i<len(shot)-1:
                calc_poss(n, partial, partial_sum, i+1) 

    calc_poss(n,[],0,0)
    master.sort()
    return master

    
print(darts(169))