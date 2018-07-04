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

##打印结果：


{'name': 'xuecf', '2fd': [{'type': 'int(11)', 'name': 'id'}, {'type': 'varchar(20)', 'name': 'name'}, {'type': 'int(11)', 'name': 'age'}]}
<type 'dict'>
{"name": "xuecf", "2fd": [{"type": "int(11)", "name": "id"}, {"type": "varchar(20)", "name": "name"}, {"type": "int(11)", "name": "age"}]}
[{'type': 'int(11)', 'name': 'id'}, {'type': 'varchar(20)', 'name': 'name'}, {'type': 'int(11)', 'name': 'age'}]
{'name': 'xuecf', '2fd': [{'type': 'int(11)', 'name': 'id'}, {'type': 'varchar(20)', 'name': 'name'}, {'type': 'int(11)', 'name': 'age'}, {'type': 'int(111)', 'name': 'age111'}]}
