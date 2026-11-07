import argparse,json
from pathlib import Path
from core080.grounded088 import execute,verify
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('--fuel',type=int,default=1);p.add_argument('--verify');a=p.parse_args()
s=Path(a.source).read_text(encoding='utf-8')
if a.verify:
    cert=json.loads(Path(a.verify).read_text());print('VALID' if verify(s,cert) else 'INVALID')
else: print(json.dumps(execute(s,a.fuel)['certificate'],ensure_ascii=False,indent=2))
