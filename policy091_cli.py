import argparse,json
from pathlib import Path
from core080.policy091 import compile_policy,verify_policy
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('--verify');a=p.parse_args();s=Path(a.source).read_text(encoding='utf-8');c=compile_policy(s)
if a.verify: print('VALID' if verify_policy(s,json.loads(Path(a.verify).read_text())) else 'INVALID')
else: print(json.dumps(c,ensure_ascii=False,indent=2))
