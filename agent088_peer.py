"""Independently running SCL agents over TCP loopback, newline-framed JSON transport.
Not cryptographic authentication; use only on trusted loopback. No external effects.
"""
import argparse,json,socket,sys
from pathlib import Path
from core080.grounded088 import execute,verify,digest,ContractError

def send(sock, obj): sock.sendall(json.dumps(obj,ensure_ascii=False,sort_keys=True).encode()+b'\n')
def receive(sock):
    buf=b''
    while not buf.endswith(b'\n'):
        v=sock.recv(4096)
        if not v: raise ConnectionError('EOF before frame')
        buf+=v
        if len(buf)>65536:raise ValueError('frame too large')
    return json.loads(buf)

def run_server(host,port):
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((host,port));s.listen(1); print('READY',flush=True)
        c,_=s.accept()
        with c:
            c.settimeout(8)
            try:
                req=receive(c)
                if set(req)!= {'source','fuel','contract_sha256'}:raise ValueError('invalid request keys')
                result=execute(req['source'],req['fuel'])
                if digest(result['contract'])!=req['contract_sha256']:raise ValueError('contract mismatch')
                if result['contract']['task']['pratigrahītṛ']!='AgentB':raise ValueError('wrong recipient')
                send(c,{'certificate':result['certificate']})
            except (ValueError,KeyError,TypeError,ConnectionError) as e:
                send(c,{'error':str(e)})

def run_client(host,port,src):
    source=Path(src).read_text(encoding='utf-8'); x=execute(source)
    with socket.create_connection((host,port),timeout=8) as c:
        c.settimeout(8)
        send(c,{'source':source,'fuel':1,'contract_sha256':digest(x['contract'])})
        answer=receive(c)
    if 'error' in answer:raise RuntimeError(answer['error'])
    cert=answer['certificate']
    if not verify(source,cert):raise RuntimeError('certificate verification failed')
    print(json.dumps({'verified':True,'peer_process':'AgentB','result':cert['result'],'contract_sha256':cert['contract_sha256']},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=('server','client'));p.add_argument('--host',default='127.0.0.1');p.add_argument('--port',type=int,required=True);p.add_argument('--source');a=p.parse_args()
    if a.mode=='server':run_server(a.host,a.port)
    else:run_client(a.host,a.port,a.source)
