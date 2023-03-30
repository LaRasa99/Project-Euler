import time
start = time.time()
n=1000
m=[]
x=[]
for i in range(n,1,-1):
    for j in range(n,1,-1):
        a = i*j
        if(str(a)==str(a)[::-1]):
            m.append(a)
            x.append(i)
            x.append(j)
print(max(m))
print(str(m[0])+' = ' + str(x[0])+ '*'+ str(x[1]))
end = time.time()
print(end-start)

