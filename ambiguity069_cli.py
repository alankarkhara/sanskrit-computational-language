import argparse,json,pathlib
from grammar.ambiguity069 import record,verify
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('--requests',required=True);p.add_argument('--verify');a=p.parse_args()
s=pathlib.Path(a.source).read_text(encoding='utf-8');req=json.loads(pathlib.Path(a.requests).read_text(encoding='utf-8'))
if a.verify:
    valid=verify(s,req,json.loads(pathlib.Path(a.verify).read_text(encoding='utf-8')))
    print('VALID' if valid else 'INVALID');raise SystemExit(0 if valid else 1)
print(json.dumps(record(s,req),ensure_ascii=False,indent=2))
