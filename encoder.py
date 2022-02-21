import random
from Text_Code import map

def exgcd(m,n):
    if n==0 :
        return m
    return exgcd(n,m%n)

def fast_power(a,k,m):
    ans=1
    while k :
        if k%2==1 :
            ans*=a%m
        a*=a%m
        k=k//2
    return ans%m

def primality_test(n):
    'Miller-Rabin primality test'
    if n==2:
        return True
    q=n-1
    k=0
    while q%2==0:
        k+=1
        q=q//2
    for a in range(1,100):
        if n%a==0:
            continue
        b=False
        for i in range(k):
            if fast_power(a,fast_power(2,i,n)*q,n)==n-1:
                b=True
                break
        if (b==False) and fast_power(a,q,n)!=1:
            return False
    return True

def generate_key():
    p=random.randint(10**6,10**7)
    while primality_test(p)==False:
        p = random.randint(10 ** 6, 10 ** 7)
    q=random.randint(10**6,10**7)
    while primality_test(q)==False:
        q = random.randint(10 ** 6, 10 ** 7)
    m=p*q
    euler_m=(p-1)*(q-1)
    k=random.randint(10**4,10**5)
    while(exgcd(k,euler_m)!=1):
        k = random.randint(10 ** 4, 10 ** 5)
    rule=open("rule.txt","w")
    key=open("key.txt","w")
    rule.write(str(m)+"\n"+str(k))
    key.write(str(p)+"\n"+str(q))

def encoding(message,k,m):
    code=[]
    for i in range(0,len(message),4):
        if (i+4)<=len(message):
            code.append(message[i:(i+4)])
        else:
            code.append(message[i:len(message)])
    for i in range(len(code)):
        j=int(code[i])
        code[i]=fast_power(j,k,m)
    return code

def toCode(message):
    code = ''
    for i in message:
        code += map[i]
    return code
