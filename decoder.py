from encoder import fast_power
from Text_Code import map
from encoder import exgcd

solution=[(0,0)]

def solve(u,v,depth):
    if(u%v==0):
        return solution[depth-1]
    if depth==1:
        solution.append((1,-(u//v)))
    elif depth==2:
        solution.append((-(u//v),1-solution[1][1]*(u//v)))
    else:
        q=u//v
        r=u%v
        solution.append((solution[depth-2][0]-q*solution[depth-1][0],solution[depth-2][1]-q*solution[depth-1][1]))
    return solve(v,u%v,depth+1)

def decoding(k, p, q, code):
    euler_m=(p-1)*(q-1)
    solution.clear()
    solution.append((0,0))
    s=solve(k,euler_m,1)
    m=p*q
    u,v=s[0],s[1]
    while u<0 :
        u+=euler_m
        v-=k
    number=''
    for i in range(len(code)):
        number+=str(fast_power(code[i],u,m))
    message=''
    for i in range(0,len(number),2):
        message+=map[number[i:(i+2)]]
    return message
