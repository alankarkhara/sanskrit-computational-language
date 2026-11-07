"""Execute native SCL agent dialogue: python native085_cli.py script.scl [--verify cert.json]."""
import argparse,json,sys
from core080.native_agents085 import compile_dialogue, verify_dialogue
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('--verify');a=p.parse_args()
source=open(a.source,encoding='utf8').read()
if a.verify:
    cert=json.load(open(a.verify,encoding='utf8'))
    valid=verify_dialogue(source,cert)
    print('VALID' if valid else 'INVALID');sys.exit(0 if valid else 1)
else: print(json.dumps(compile_dialogue(source),ensure_ascii=False,indent=2))
