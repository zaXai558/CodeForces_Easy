s=input().split()
k=int(s[0])
n=int(s[1])
w=int(s[2])

pay=0
for i in range(w):
    pay=pay+(i+1)*k

print(pay-n if(pay-n)>0 else 0)
    
