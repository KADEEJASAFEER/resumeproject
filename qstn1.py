string = input("enter the string")
txt=list(string)
dict={}
for i in txt:
    if(i not in dict):
        dict[i]=1
    else:
        dict[i]+=1
print(dict)

