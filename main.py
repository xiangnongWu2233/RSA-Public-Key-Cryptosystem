import math
n=155196355420821961
for i in range(2,int(math.sqrt(n))-1):
    if(n%i==0):
        print("False")
print("True")
