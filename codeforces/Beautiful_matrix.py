matrix=list()
for i in range(0,5):
    matrix.append(input().split())
def find(matrix):
    i=r=c=0
    OneFind=False
    while(i<5 and not OneFind):
        j=0
        while(j<5 and not OneFind):
            if matrix[i][j]=='1':
                r=i
                c=j
                OneFind= True
            j+=1
        i+=1
    return (abs(r-2)+abs(c-2))

print(find(matrix))
                
