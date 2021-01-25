try:
    def SieveOfEratosthenes(n): 
        global prime

        p = 2
        while (p * p <= n): 
            if (prime[p] == True):
                #pn.append(p)
                for i in range(p * p, n+1, p): 
                    prime[i] = False
            p += 1
    
    def isPossible(n):
        global pn
        
        c = 0
        #maxi = n
        for i in range(5, n+1):
            if prime[i]:
                if(prime[i-2]):
                    pn[i]=pn[i-1]+1
                else:
                    pn[i]=pn[i-1]
            else:
                pn[i]=pn[i-1]
            
        
    nn = 1000000
    prime = [True for i in range(nn+1)]
    pn = []
    for j in range(nn+1):
        pn.append(0)
    SieveOfEratosthenes(nn)
    prime[0] = False
    prime[1] = False
    isPossible(nn)
    t = int(input())
    for _ in range(t):
        n = int(input())
        #print(pn)
        #print(prime)
        print(pn[n])
except:
    exit(0)