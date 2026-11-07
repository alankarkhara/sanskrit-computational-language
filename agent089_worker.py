"""Separate worker process for signed SCL document task; stdin/out JSON IPC."""
import sys,json,base64
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from core080.grounded089 import execute_request
payload=json.loads(sys.stdin.readline())
key=Ed25519PrivateKey.from_private_bytes(base64.b64decode(payload['worker_secret']))
result=execute_request(payload['request'],key,payload['root_public'],payload['now'],set())
print(json.dumps(result,ensure_ascii=False,sort_keys=True),flush=True)
