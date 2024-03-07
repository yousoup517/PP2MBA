def solve(numhead, numlegs):
    chick = 0
    rabbit = 0
    
    for chick in range(numhead+1):
        rabbit = numhead - chick
        if (2*chick + 4*rabbit == numlegs):
            return chick, rabbit
        
    return 0, 0


def ounces(g):
    return 28.3495231 * g
