#!/usr/bin/env python3
"""Source/IR/grammar replay certificates for the stable candidate."""
import argparse,json,pathlib,sys
from scl import compile_source
from grammar.assurance import grammar_bundle,verify_bundle

p=argparse.ArgumentParser()
p.add_argument('source',type=pathlib.Path)
p.add_argument('--policy',default='certified',choices=['certified','symbolic','symbolic-confluent','formal','checked','legacy'])
p.add_argument('--requests',type=pathlib.Path,help='JSON array of {predicate,tokens}')
p.add_argument('--verify',type=pathlib.Path,help='Recheck existing bundle')
a=p.parse_args()
source=a.source.read_text(encoding='utf8')
compiler=lambda s:compile_source(s,rewrite_policy=a.policy)
if a.verify:
    bundle=json.loads(a.verify.read_text(encoding='utf8'))
    valid=verify_bundle(source,bundle,compiler)
    print('VALID' if valid else 'INVALID');sys.exit(0 if valid else 1)
requests=json.loads(a.requests.read_text(encoding='utf8')) if a.requests else []
print(json.dumps(grammar_bundle(source,compiler(source),requests),ensure_ascii=False,indent=2))
