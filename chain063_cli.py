import argparse,json,pathlib,sys
from scl import compile_source
from grammar.chain063 import produce,verify
p=argparse.ArgumentParser()
p.add_argument('source',type=pathlib.Path)
p.add_argument('--verify',type=pathlib.Path)
p.add_argument('--boundary',nargs=2,default=['i','i'])
a=p.parse_args();source=a.source.read_text(encoding='utf8')
compile_fn=lambda text:compile_source(text,rewrite_policy='certified')
if a.verify:
    result=verify(source,compile_fn,json.loads(a.verify.read_text(encoding='utf8')))
    print('VALID' if result else 'INVALID');sys.exit(0 if result else 1)
print(json.dumps(produce(source,compile_fn,tuple(a.boundary)),ensure_ascii=False,indent=2))
