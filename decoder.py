from encoder import fast_power
map={}
for i in range(26):
    map.update({chr(i+65):str(i+11)})
    map.update({str(i+11):chr(i+65)})
for i in range(26):
    map.update({chr(i+97):str(i+37)})
    map.update({str(i+37):chr(i+97)})
map.update({' ':'70'})
map.update({'70':' '})
solution=[(0,0)]

def exgcd(m,n):
    if n==0 :
        return m
    return exgcd(n,m%n)

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
    s=solve(k,-euler_m,1)
    m=p*q
    u,v=s[0],s[1]
    while u<=0 :
        u+=euler_m
        v-=k
    number=''
    test=[]
    for i in range(len(code)):
        number+=str(fast_power(code[i],u,m))
        test.append(fast_power(code[i],u,m))
    print(test)
    #print(number)
    message=''
    for i in range(0,len(number),2):
        message+=map[number[i:(i+2)]]
    return message
