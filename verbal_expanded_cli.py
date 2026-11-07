import sys,json,argparse
from grammar.verbal_expanded import derive,verify,DerivationError
p=argparse.ArgumentParser();p.add_argument('root',nargs='?',default='bhū');p.add_argument('--person',type=int,choices=(1,2,3),default=3);p.add_argument('--verify');a=p.parse_args()
try:
 if a.verify:
  with open(a.verify,encoding='utf-8') as f: c=json.load(f)
  ok=verify(c);print('VALID' if ok else 'INVALID');sys.exit(0 if ok else 1)
 print(json.dumps(derive(a.root,a.person),ensure_ascii=False,indent=2))
except (ValueError,OSError) as exc: print(str(exc),file=sys.stderr);sys.exit(2)
