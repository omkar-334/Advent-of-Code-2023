import re

input=open('input2.txt','r').readlines()
dict={"red":12,"green":13,"blue":14}

sum=0
for line in input:
    flag=True

    games=re.split(";",line[8:].replace("\n",""))
    games=[[i.replace(":","").split() for i in j.split(",")] for j in games]

    for game in games:
        for set in game:
            print(set)
            if dict[set[1]]<int(set[0]):
                flag=False

    if flag==True:
        sum+=int(line[5:8].replace(":",""))

print(sum)
