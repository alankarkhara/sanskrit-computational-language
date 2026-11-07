import argparse, json
from grammar.coverage065 import coverage, recognize
a=argparse.ArgumentParser()
a.add_argument('sutra',nargs='?')
a.add_argument('--field')
a.add_argument('--value')
x=a.parse_args()
if not x.sutra: print(json.dumps(coverage(),ensure_ascii=False,indent=2))
else: print(json.dumps(recognize(x.sutra,{x.field:x.value}),ensure_ascii=False,indent=2))
