def compare(str1, str2):
    for i in range(0,len(str1)):
        if(str1.lower()[i]<str2.lower()[i]):
            return -1
        elif(str1.lower()[i]>str2.lower()[i]):
            return 1
    return 0
str1=input()
str2=input()
print(compare(str1,str2))
        
        
