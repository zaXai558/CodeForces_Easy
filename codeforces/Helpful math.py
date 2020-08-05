s=input()
count1=count2=count3=0
for i in range(0,len(s),2):
    if s[i]== '1':
        count1+=1
    elif s[i]== '2':
        count2+=1
    else:
        count3+=1
sub= "1+" * count1 + "2+" * count2 + "3+" * count3
print(sub[:-1])
