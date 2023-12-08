import re
input=open('input1.txt','r').readlines()

pattern='(?=(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))'

dict={"one":'1',"two":'2',"three":'3',"four":'4',"five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9',
      "1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}

sum=0

for i in input:
    temp=re.findall(pattern,i)
    out=[dict[x] for x in temp]

    calvalue=str(out[0])+str(out[-1])
    sum+=int(calvalue)

print(sum)