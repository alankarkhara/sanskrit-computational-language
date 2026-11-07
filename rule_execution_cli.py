import argparse, json
from grammar.rule_execution import demonstration, verify_certificate
p=argparse.ArgumentParser(description='SCL 0.6 bounded rule-execution certificate demo')
p.add_argument('--case',choices=['joinable','divergent','exception'],default='joinable')
p.add_argument('--verify')
a=p.parse_args()
if a.verify:
 with open(a.verify,encoding='utf-8') as f: c=json.load(f)
 print('VALID' if verify_certificate(c) else 'INVALID')
 raise SystemExit(0 if verify_certificate(c) else 1)
print(json.dumps(demonstration()[a.case],ensure_ascii=False,indent=2))
