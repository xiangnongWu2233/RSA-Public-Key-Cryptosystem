from encoder import fast_power
solution=[(0,0)]
def exgcd(m,n):
    if n==0 :
        return m
    return exgcd(n,m%n)


def solve(u,v,depth):
    if(v==0):
        return
    if depth==1:
        solution.append((1,-u//v))
    if depth==2:
        solution.append((-u//v,1-solution[1][1]*(u//v)))
    else:
        q=u//v
        r=u%v
        solution.append((solution[depth-2][0]-q*solution[depth-1][0],solution[depth-2][1]-q*solution[depth-1][1]))
    print(solution[depth])
    solve(v,u%v,depth+1)


#solve(12453,2347,1)
