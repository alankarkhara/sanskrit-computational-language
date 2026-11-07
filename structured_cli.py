import argparse,json,sys
from grammar.structured_rules import certificate,verify,DerivationError
p=argparse.ArgumentParser();p.add_argument('left',nargs='?');p.add_argument('right',nargs='?');p.add_argument('--verify')
a=p.parse_args()
try:
 if a.verify:
  with open(a.verify,encoding='utf-8') as f:c=json.load(f)
  print('VALID' if verify(c) else 'INVALID');sys.exit(0 if verify(c) else 1)
 if not a.left or not a.right:p.error('two words required')
 print(json.dumps(certificate(a.left,a.right),ensure_ascii=False,indent=2))
except DerivationError as e: print(str(e),file=sys.stderr);sys.exit(2)
