#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
from gate.certify import make,verify,GateError
p=argparse.ArgumentParser(description='Fail-closed SCL certification gate')
p.add_argument('source',type=Path);p.add_argument('--requests',type=Path);p.add_argument('--verify',type=Path)
a=p.parse_args()
try:
    src=a.source.read_text(encoding='utf-8')
    if a.verify:
        ok=verify(src,json.loads(a.verify.read_text(encoding='utf-8')))
        print('VALID' if ok else 'INVALID');sys.exit(0 if ok else 1)
    requests=json.loads(a.requests.read_text(encoding='utf-8')) if a.requests else []
    print(json.dumps(make(src,requests=requests),indent=2,ensure_ascii=False))
except (OSError,ValueError,TypeError,KeyError,GateError) as exc:
    print('GATE REJECTED:',exc,file=sys.stderr);sys.exit(2)
