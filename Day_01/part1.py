import re
input=open('input1.txt','r').readlines()

sum=0
for i in input:
    out="".join(re.findall("[0-9]*",i))
    calvalue=str(out[0])+str(out[-1])
    sum+=int(calvalue)

print(sum)
