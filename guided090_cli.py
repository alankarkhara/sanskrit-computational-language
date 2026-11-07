import argparse,json
from pathlib import Path
from guided090.interface import draft,confirm,ClarificationRequired
p=argparse.ArgumentParser(description='Narrow fail-closed SCL request preview')
p.add_argument('request');p.add_argument('--document',required=True);p.add_argument('--id',default='document42');p.add_argument('--approve',action='store_true')
a=p.parse_args()
try:
    d=draft(a.request,{a.id:Path(a.document).read_bytes()})
    print(json.dumps({'preview':d['preview'],'scl_source':d['scl_source'],'state':d['status']},indent=2,ensure_ascii=False))
    if a.approve:print(json.dumps({'state':confirm(d,True)['status']}))
except ClarificationRequired as e:
    print(json.dumps({'state':'needs_clarification','reason':str(e)}));raise SystemExit(2)
