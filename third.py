text=bin(int(input()))
bt=1
ct=0
for i in range(len(text)-3):
    if text[i+2]==text[i+3]:
        bt+=1
    else:
        ct=max(c,bt)
        bt=1
        continue
print(ct)
