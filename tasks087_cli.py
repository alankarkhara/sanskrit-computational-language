"""Native SCL task negotiation: python tasks087_cli.py program.scl [--verify file.json]"""
import argparse,json,sys
from core080.tasks087 import compile_tasks,verify_tasks
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('--verify');a=p.parse_args()
s=open(a.source,encoding='utf8').read()
if a.verify:
    cert=json.load(open(a.verify,encoding='utf8'))
    ok=verify_tasks(s,cert);print('VALID' if ok else 'INVALID');sys.exit(0 if ok else 1)
else:print(json.dumps(compile_tasks(s),ensure_ascii=False,indent=2))
