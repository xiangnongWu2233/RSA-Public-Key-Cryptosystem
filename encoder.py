import random
map={}
for i in range(26):
    map.update({chr(i+65):str(i+11)})
    map.update({str(i+11):chr(i+65)})
for i in range(26):
    map.update({chr(i+97):str(i+37)})
    map.update({str(i+37):chr(i+97)})
map.update({' ':'70'})
map.update({'70':' '})


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
    k=random.randint(10**6,10**7)
    while(euler_m%k==0):
        k=random.randint(10**6,10**7)
    save=open("rule.txt","w")
    save.write(str(m)+"\n"+str(k))
    return (p,q)

def encoding(message,k,m):
    number=''
    for i in message:
        number+=map[i]
    code=[]
    for i in range(0,len(number),4):
        if (i+4)<=len(number):
            code.append(number[i:(i+4)])
        else:
            code.append(number[i:len(number)])
    for i in range(len(code)):
        j=int(code[i])
        code[i]=fast_power(j,k,m)
    return code
