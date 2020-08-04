n,k= [int(x) for x in input().split()]
numList=list()
numList = [int(x)for x in input().split()]
result= 0
for i in numList:
    if(i>0 and i>=numList[k-1]):
        result+=1
print(result)
        
