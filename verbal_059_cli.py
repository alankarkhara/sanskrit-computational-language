import argparse,json
from grammar.verbal_059 import derive,verify
p=argparse.ArgumentParser()
p.add_argument('root',nargs='?',default='bhū');p.add_argument('--person',type=int,default=3);p.add_argument('--number',choices=['sg','du','pl'],default='sg');p.add_argument('--verify')
a=p.parse_args()
if a.verify:
 with open(a.verify,encoding='utf-8') as f:c=json.load(f)
 print('VALID' if verify(c) else 'INVALID')
else:print(json.dumps(derive(a.root,a.person,a.number),ensure_ascii=False,indent=2))
