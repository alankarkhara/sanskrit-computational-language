import argparse,json,sys
from core080.rules081 import compile_081,execute_081,certify_081,verify_081
from core080 import SclError
p=argparse.ArgumentParser(description='SCL certified restricted rewrite compiler v0.8.1')
p.add_argument('source');p.add_argument('--config');p.add_argument('--certify',action='store_true');p.add_argument('--verify');p.add_argument('--ir',action='store_true')
a=p.parse_args()
s=open(a.source,encoding='utf8').read()
try:
    if a.verify:
        result=verify_081(s,json.load(open(a.verify,encoding='utf8')))
        print('VALID' if result else 'INVALID');sys.exit(0 if result else 1)
    config=json.load(open(a.config,encoding='utf8')) if a.config else None
    if a.certify:print(json.dumps(certify_081(s,config),ensure_ascii=False,indent=2))
    elif a.ir: print(json.dumps(compile_081(s,config),ensure_ascii=False,indent=2))
    else:print(*execute_081(s,config),sep='\n')
except (SclError,ValueError) as ex:print('ERROR:',ex,file=sys.stderr);sys.exit(2)
