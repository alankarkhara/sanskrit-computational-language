import argparse,json,sys
from pathlib import Path
from grammar.assurance067 import certificate,verify
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('--requests',required=True);p.add_argument('--verify')
a=p.parse_args();source=Path(a.source).read_text();requests=json.loads(Path(a.requests).read_text())
if a.verify:
    valid=verify(source,requests,json.loads(Path(a.verify).read_text()));print('VALID' if valid else 'INVALID');sys.exit(0 if valid else 1)
print(json.dumps(certificate(source,requests),ensure_ascii=False,indent=2))
