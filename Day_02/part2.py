import math
import re

input=open('input2.txt','r').readlines()

out=0
for line in input:
    dict={"red":0,"green":0,"blue":0}
    flag=True

    games=re.split(";",line[8:].replace("\n",""))
    games=[[i.replace(":","").split() for i in j.split(",")] for j in games]

    for game in games:
        for set in game:
            if dict[set[1]]<(var:=int(set[0])):
                dict[set[1]]=var

    out+=math.prod(list(dict.values()))

print(out)
