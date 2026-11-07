"""Reproducible, task-focused SCL/Python/Node comparison; no performance equivalence claim."""
import json, subprocess, sys, time, shutil
from core080.language import execute, SclError
from core080.rules081 import certify_081, execute_081
from core080.independent082 import check

CASES=[
 ('role_order','(krama (kārya f ((kartṛ Int) (karma Int)) Int (vyavakalana kartṛ karma)) (darśaya (āhvāna f (karma 4) (kartṛ 9))))',True,[5]),
 ('duplicate_role','(krama (kārya f ((kartṛ Int)) Int kartṛ) (darśaya (āhvāna f (kartṛ 5) (kartṛ 7))))',False,None),
 ('missing_role','(krama (kārya f ((kartṛ Int) (karma Int)) Int (yoga kartṛ karma)) (darśaya (āhvāna f (kartṛ 5))))',False,None),
 ('role_type_error','(krama (kārya f ((kartṛ Int)) Int kartṛ) (darśaya (āhvāna f (kartṛ satya))))',False,None),
 ('lazy_branch','(krama (darśaya (yadi satya (yoga 4 0) (bhāga 1 0))))',True,[4]),
 ('neutral_multiplication','(krama (darśaya (guṇana 1 (yoga 8 0))))',True,[8]),
 ('integer_overflow','(krama (darśaya (yoga 9223372036854775807 1)))',False,None),
 ('unknown_function','(krama (darśaya (āhvāna missing (kartṛ 3))))',False,None),
]
PYTHON_BASELINE='''def role_function(*, kartṛ:int, karma:int)->int:\n    if type(kartṛ) is not int or type(karma) is not int: raise TypeError\n    return kartṛ-karma\nprint(role_function(karma=4,kartṛ=9))'''
NODE_BASELINE='''function roleFunction({kartṛ,karma}) { if(!Number.isInteger(kartṛ)||!Number.isInteger(karma))throw new TypeError(); return kartṛ-karma; } console.log(roleFunction({karma:4,kartṛ:9}));'''

def benchmark():
 results=[]
 for name,src,accept,expected in CASES:
  started=time.perf_counter_ns()
  try:
   value=execute_081(src)
   permitted=True
   certificate=certify_081(src)
   verified=check(src,certificate)
  except (ValueError,OverflowError,TypeError) as e:
   permitted=False;value=None;verified=False
  elapsed=(time.perf_counter_ns()-started)/1e6
  results.append({'case':name,'expected_accept':accept,'accepted':permitted,'value':value,'independent_certificate_verified':verified,'pass':permitted==accept and (not accept or (value==expected and verified)),'elapsed_ms':round(elapsed,3)})
 language=[]
 for name,runner,script in [('Python',sys.executable,PYTHON_BASELINE),('Node',shutil.which('node'),NODE_BASELINE)]:
  if not runner:language.append({'language':name,'available':False});continue
  command=[runner,'-c',script] if name=='Python' else [runner,'-e',script]
  t=time.perf_counter_ns();p=subprocess.run(command,capture_output=True,text=True,timeout=5)
  language.append({'language':name,'available':True,'returncode':p.returncode,'output':p.stdout.strip(),'elapsed_process_ms':round((time.perf_counter_ns()-t)/1e6,3)})
 return {'scl_cases':results,'passed':sum(x['pass'] for x in results),'total':len(results),'reference_runtimes':language,'caution':'Python and Node programs exercise an equivalent role-order task only, not full comparable static semantics or compiler speed.'}
if __name__=='__main__':print(json.dumps(benchmark(),indent=2,ensure_ascii=False))
