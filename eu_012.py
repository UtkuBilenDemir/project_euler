# https://projecteuler.net/problem=12

def primeFactor(p, n = 2, l = []):
    if p == 1:
        return l


    elif p % n == 0:
        p = p//n
        l.append(n)
            
        
    else:
        n+=1
    
    primeFactor(p=p, n=n, l=l)
        
print(primeFactor(57))