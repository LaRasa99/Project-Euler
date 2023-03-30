a = 1
b = 2
n = 4000000
m =0
while(a<n):
    if(a%2==0):
        m+=a
    a, b = b, b+a
print(m)
