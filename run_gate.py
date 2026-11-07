from pathlib import Path
import json
from gate.compatibility import run
root=Path(__file__).resolve().parent.parent
latest=Path(__file__).resolve().parent
names=['scl_v0_1','scl_v0_2','scl_v0_3','scl_v0_4','scl_v0_4_audited','scl_v0_4_1_integrity','scl_v0_4_2_formal','scl_v0_4_3_proof','scl_v0_4_4_certified','scl_v0_4_5_symbolic','scl_v0_5_alpha','scl_v0_5_beta','scl_v0_5_stable_candidate','scl_v0_5_integrity_candidate','scl_v0_5_sentence_checked']
result=run([root/n for n in names if (root/n/'scl.py').exists()],latest,limit=40)
(latest/'COMPATIBILITY_GATE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(f"{result['matched']}/{result['total']} matches; {len(result['failures'])} differences")
