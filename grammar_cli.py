import argparse,json
from grammar.panini import analyse_sentence,verify_certificate,REGISTRY
p=argparse.ArgumentParser();p.add_argument('predicate',nargs='?');p.add_argument('tokens',nargs='*');p.add_argument('--registry',action='store_true');p.add_argument('--verify',metavar='JSONFILE')
a=p.parse_args()
if a.registry:print(json.dumps(REGISTRY,ensure_ascii=False,indent=2))
elif a.verify:
 with open(a.verify,encoding='utf-8') as f: c=json.load(f)
 print('VALID' if verify_certificate(c) else 'INVALID');raise SystemExit(0 if verify_certificate(c) else 1)
else:
 if not a.predicate or not a.tokens:p.error('predicate and nominal tokens required')
 print(json.dumps(analyse_sentence(a.tokens,a.predicate),ensure_ascii=False,indent=2))
