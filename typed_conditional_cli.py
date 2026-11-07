"""Run the bounded finite-domain conditional critical-pair demonstration."""
import argparse,json
from grammar.typed_conditional import demo_system
p=argparse.ArgumentParser()
p.add_argument('--conflict',action='store_true',help='include a synthetic overlapping incompatible grammatical rule')
p.add_argument('--max-assignments',type=int,default=4096)
a=p.parse_args()
r=demo_system(a.conflict).conditional_pairs(max_assignments=a.max_assignments)
print(json.dumps({'status':r['status'],'pairs':[{**x,'start':repr(x['start']),'left':repr(x['left']),'right':repr(x['right'])} for x in r['pairs']]},ensure_ascii=False,indent=2))
