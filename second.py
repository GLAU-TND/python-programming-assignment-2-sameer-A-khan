string=eval(input())
string=[str(i) for i in string]
string.sort()
b=''
for i in range(len(t)-1):
    if string[i][0]==string[i+1][0] and len(string[i])<len(string[i+1]):
        a=string[i]
        string[i]=string[i+1]
        string[i+1]=a
for i in range(len(string)-1,-1,-1):
    b=b+string[i]
print(int(b))

