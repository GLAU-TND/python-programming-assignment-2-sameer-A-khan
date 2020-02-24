string=eval(input())
baw=[min(string)]
an=min(string)[-1]
string.remove(min(string))
for i in string:
    for j in string:
        if an==j[0] and j[-1]!=baw[0][0]:
            baw.append(j)
            an=j[-1]
            string.remove(j)
            break
baw=baw+string
print(baw)
