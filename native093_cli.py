import argparse,json
from pathlib import Path
from core080.native093 import compile_dialogue,verify_dialogue
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('--verify');a=p.parse_args()
s=Path(a.source).read_text(encoding='utf-8')
if a.verify:
    assert verify_dialogue(s,json.loads(Path(a.verify).read_text(encoding='utf-8'))),'INVALID';print('VALID')
else:print(json.dumps(compile_dialogue(s),ensure_ascii=False,sort_keys=True,indent=2))
