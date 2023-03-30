import time
start = time.time()
n = 600851475143
b=[]
for i in range(2, int(n**0.5+1)):
    a = n%i
    if(a==0):
        c=[1]
        for j in range(2, i+1):
            if i%j==0:
                c.append(j)
        if(len(c)==2):
            b.append(i)
print(b[-1])
print(b)
end = time.time()
print(end-start)       
