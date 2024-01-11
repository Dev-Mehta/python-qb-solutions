def getPatients(m,d):
    return ((6-m)**2 + abs(d-15))

def countTv(n, r1, r2, target):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for tvs in range(n+1):
        ctarget = 0
        # For each month
        for m in range(1,13):
            # For each day set target according to formula
            for d in range(1,days[m]+1):
                np = getPatients(m,d)
                np = min(np, n)
                if np <= n - tvs:
                    ctarget += np * r2
                else:
                    ctarget += ((n - tvs) * r2 + ((np - (n - tvs)) * r1))
        if ctarget >= target:
            break
    return min(tvs, n)
    
print(countTv(20,1500,1000,7000000))
print(countTv(10,1000,1500,10000000))
