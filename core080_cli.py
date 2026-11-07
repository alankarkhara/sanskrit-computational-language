import argparse, json, pathlib, sys
from core080 import compile_program, execute, certify, verify, SclError
p=argparse.ArgumentParser(description='Strict SCL v0.8.0 language core')
p.add_argument('source'); p.add_argument('--certify',action='store_true'); p.add_argument('--verify')
a=p.parse_args()
s=pathlib.Path(a.source).read_text(encoding='utf-8')
try:
    if a.verify:
        print('VALID' if verify(s,json.loads(pathlib.Path(a.verify).read_text())) else 'INVALID')
        sys.exit(0 if verify(s,json.loads(pathlib.Path(a.verify).read_text())) else 1)
    if a.certify:print(json.dumps(certify(s),ensure_ascii=False,indent=2))
    else:
        for value in execute(s): print(str(value).lower() if isinstance(value,bool) else value)
except SclError as e:
    print('SCL REJECTED:',e,file=sys.stderr);sys.exit(2)
