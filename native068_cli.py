import argparse,json
from pathlib import Path
from grammar.native068 import certificate,verify
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('--verify');a=p.parse_args();s=Path(a.source).read_text()
if a.verify:
 print('VALID' if verify(s,json.loads(Path(a.verify).read_text())) else 'INVALID')
 raise SystemExit(0 if verify(s,json.loads(Path(a.verify).read_text())) else 1)
print(json.dumps(certificate(s),ensure_ascii=False,indent=2))
