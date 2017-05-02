import math
def prime(max):
    for i in range(2,max):
        if _isPrime(i):
            yield i

def _isPrime(x):
    if x == 2:
        return True
    for i in range(2,math.ceil(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True