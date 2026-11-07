import argparse,json
from pathlib import Path
from grammar.evidence066 import certificate,verify,audit_interactions
p=argparse.ArgumentParser()
p.add_argument('source',nargs='?');p.add_argument('--requests');p.add_argument('--verify');p.add_argument('--audit',action='store_true')
a=p.parse_args()
if a.audit:print(json.dumps(audit_interactions(),ensure_ascii=False,indent=2));raise SystemExit
if not a.source or not a.requests:p.error('source and --requests required')
s=Path(a.source).read_text(encoding='utf8');requests=json.loads(Path(a.requests).read_text(encoding='utf8'))
if a.verify:
 print('VALID' if verify(s,requests,json.loads(Path(a.verify).read_text(encoding='utf8'))) else 'INVALID')
else:print(json.dumps(certificate(s,requests),ensure_ascii=False,indent=2))
