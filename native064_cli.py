import argparse,json,pathlib,sys
from grammar.native064 import certificate,verify
p=argparse.ArgumentParser();p.add_argument('source',type=pathlib.Path);p.add_argument('--verify',type=pathlib.Path);a=p.parse_args()
s=a.source.read_text(encoding='utf8')
if a.verify:
    print('VALID' if verify(s,json.loads(a.verify.read_text(encoding='utf8'))) else 'INVALID')
    sys.exit(0 if verify(s,json.loads(a.verify.read_text(encoding='utf8'))) else 1)
print(json.dumps(certificate(s),ensure_ascii=False,indent=2))
