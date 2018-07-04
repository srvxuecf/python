list1 = []
import json

with open('2.txt','r') as f:
    for i in f:
        ret = eval(i.replace('\n',''))
        
        #print type(ret)
        list1.append(ret)
        #print i

dict1={}
dict1['name'] = "xuecf"

dict1['2fd'] = list1
print dict1
print type(dict1)


print json.dumps(dict1)



print dict1.get('2fd')

dict1.get('2fd').append(eval('{"type": "int(111)", "name": "age111"}'))

print dict1