from encoder import generate_key,encoding,fast_power
from decoder import decoding,solve

key=generate_key()
p=key[0]
q=key[1]
print(p)
print(q)
infile=open("rule.txt","r")
sm=infile.readline()
sk=infile.readline()
m=int(sm)
k=int(sk)
code=encoding("Good Morning",k,m)
print(decoding(k,p,q,code))
