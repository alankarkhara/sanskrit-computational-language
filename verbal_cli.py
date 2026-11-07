import argparse,json,sys
from pathlib import Path
from grammar.verbal import derive,verify,DerivationError
p=argparse.ArgumentParser(description='Restricted source-referenced laṭ derivations')
p.add_argument('root',nargs='?',default='paṭh');p.add_argument('--verify')
a=p.parse_args()
if a.verify:
    try:ok=verify(json.loads(Path(a.verify).read_text(encoding='utf-8')))
    except (ValueError,OSError):ok=False
    print('VALID' if ok else 'INVALID');sys.exit(0 if ok else 1)
try:print(json.dumps(derive(a.root),ensure_ascii=False,indent=2))
except DerivationError as e:print(e,file=sys.stderr);sys.exit(2)
