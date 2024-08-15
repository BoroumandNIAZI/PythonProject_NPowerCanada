import json
d = {'Artin': {'Age' : 13, 'class' : 'secondaire' },
     'Sourena': {'Age' : 8, 'class' : '2e année' }
     }
# print(json.dumps(d, ensure_ascii=False),'\n')
# print(json.dumps(d, indent = 4),'\n') 
# print(json.dumps(d, indent = 4, separators = (';', '-> ')),'\n')

jsn = 'C:/Users/borou/OneDrive/Documents/VSCode/mysons.json'

with open(jsn, 'w') as f:
    json.dump(d, f)

# with open(jsn) as f:
#     print(json.load(f))


import glob
print(glob.glob('C:/Users/borou/OneDrive/Documents/VSCode/*.*'))