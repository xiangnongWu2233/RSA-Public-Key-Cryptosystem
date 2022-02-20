import random

def fast_power(a,k,m):
    ans=1
    while(k):
        if(k%2==1):
            ans*=a%m
        a*=a%m
        k=int(k/2)
    return ans%m

def primality_test(n):
    #Miller-Rabin primality test
    if n==2:
        return True
    q=n-1
    k=0
    while q%2==0:
        k+=1
        q/=2
    q=int(q)
    for a in range(1,n):
        if n%a==0:
            continue
        b=False
        for i in range(k):
            print(fast_power(a,fast_power(2,i,n)*q,n))
            if fast_power(a,fast_power(2,i,n)*q,n)==n-1:
                b=True
                break
        if (b==False) and fast_power(a,q,n)!=1:
            return False
    return True

def generate_key():
    p=random.randint(10**200,10**201)
    q=random.randint(10**200,10**201)
    m=p*q
    euler_m=(p-1)*(q-1)
    k=random.randint(10**10,10**11)
    while(euler_m%k==0):
        k=random.randint(10**10,10**11)
    save=open("rule.txt","w")
    save.write(str(m)+"\n"+str(k))

def encoding(message,k,m):
    information=message.upper()
    number=''
    for i in information:
        number+=str(ord(i))
    code=[]
    for i in range(0,len(number),8):
        if (i+8)<=len(number):
            code.append(number[i:(i+8)])
        else:
            code.append(number[i:len(number)])
    for i in range(len(code)):
        j=int(code[i])
        code[i]=fast_power(j,k,m)
    return code

'''generate_key()
infile=open("rule.txt","r")
sm=infile.readline()
sk=infile.readline()
m=int(sm)
k=int(sk)
'''
print(primality_test(155196355420821961))
