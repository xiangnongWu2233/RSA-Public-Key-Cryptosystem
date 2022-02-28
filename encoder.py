import random
import os
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

def generate_key(range):
    p=random.randint(10**range,10**(range+1))
    while primality_test(p)==False:
        p = random.randint(10 ** range, 10 ** (range+1))
    q=random.randint(10**range,10**(range+1))
    while primality_test(q)==False:
        q = random.randint(10 ** range, 10 ** (range+1))
    m=p*q
    euler_m=(p-1)*(q-1)
    k=random.randint(10**range,10**(range+1))
    while(exgcd(k,euler_m)!=1):
        k = random.randint(10 ** range, 10 ** (range+1))


    if os.path.exists('Table')==False:
        os.mkdir('Table')
    path_rule=os.path.join('Table','rule.txt');
    path_key=os.path.join('Table','key.txt');
    rule=open(path_rule,"w")
    key=open(path_key,"w")
    rule.write(str(m)+"\n"+str(k))
    key.write(str(p)+"\n"+str(q))
    rule.close()
    key.close()

def encoding(message,m,k):
    message=toCode(message)
    code=[]
    for i in range(0,len(message),8):
        if (i+8)<=len(message):
            code.append(message[i:(i+8)])
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
