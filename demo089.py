"""Demonstrate OS-isolated requester & executor (IPC subprocess); test only."""
import base64,hashlib,json,subprocess,sys
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey as Key
from cryptography.hazmat.primitives import serialization
from core080.grounded089 import *
from pathlib import Path
document='A verified document has five tokens'.encode()
source=f'''(kārya_pramāṇa
  (vastu (id doc42) (prakāra UTF8Document) (sha256 {hashlib.sha256(document).hexdigest()}))
  (ādeśa (id task42) (kartṛ AgentA) (pratigrahītṛ AgentB)
    (kriyā gaṇaya_śabdān) (lakṣya doc42) (pariṇāma Int64)
    (prabhāva śuddha) (anumati antarika)))'''
root,a,b=Key.generate(),Key.generate(),Key.generate()
grant=issue_grant(root,pubkey(b),compile_source(source),expires_at=100)
request=authenticated_request(source,document,a,grant,'nonce-example-00001')
private=base64.b64encode(b.private_bytes(serialization.Encoding.Raw,serialization.PrivateFormat.Raw,serialization.NoEncryption())).decode()
proc=subprocess.run([sys.executable,'agent089_worker.py'],input=json.dumps({'request':request,'worker_secret':private,'root_public':pubkey(root),'now':50})+'\n',text=True,capture_output=True,check=True,cwd=Path(__file__).resolve().parent)
response=json.loads(proc.stdout)
verified=verify_result(source,document,request,response,pubkey(root),50)
report={'version':'0.8.9','separate_worker_pid':True,'verified':verified,'value':response['body']['result']['value'],'document_digest':hashlib.sha256(document).hexdigest(),'transport':'local standard-input/output subprocess','signed_request':True,'signed_grant':True,'signed_result':True}
Path('DEMO_089_RESULT.json').write_text(json.dumps(report,indent=2)+'\n')
Path('core080/examples/grounded_document_089.scl').write_text(source+'\n')
print(json.dumps(report,indent=2))
assert verified and report['value']==6
