def solve(numhead, numlegs):
    chick = 0
    rabbit = 0
    
    for chick in range(numhead+1):
        rabbit = numhead - chick
        if (2*chick + 4*rabbit == numlegs):
            return chick, rabbit
        
    return 0, 0

sanzh = int(input())
legs = int(input())
c , r = solve(sanzh, legs)

if (c != 0) and (legs != 0):
    print(c, r)
else:
    print("No solve")
