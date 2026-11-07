"""Run two independent OpenAI-compatible LOCAL inference servers for protocol smoke tests.

The model responses are untrusted and NOT execution authorization.
Supply e.g. --a-url http://127.0.0.1:11434/v1/chat/completions, --a-model ...
No network calls occur unless this script is explicitly invoked.
"""
import argparse,json,urllib.request,urllib.parse
from core080.wire100 import VERSION,encode,decode,ReceiveSequence

def localhost_only(url):
    p=urllib.parse.urlparse(url)
    if p.scheme!='http' or p.hostname not in ('localhost','127.0.0.1','::1') or p.username or p.password:raise ValueError('local http endpoint only')
    if p.path not in ('/v1/chat/completions','/api/chat'):raise ValueError('unsupported endpoint path')
    return url

def infer(url,model,prompt):
    localhost_only(url)
    if url.endswith('/api/chat'):
        data={'model':model,'stream':False,'messages':[{'role':'user','content':prompt}]}
    else:data={'model':model,'stream':False,'messages':[{'role':'user','content':prompt}]}
    req=urllib.request.Request(url,json.dumps(data).encode(),{'Content-Type':'application/json'},method='POST')
    with urllib.request.urlopen(req,timeout=45) as res:
        if int(res.headers.get('Content-Length','0'))>65536:raise ValueError('oversized model response')
        raw=res.read(65537)
    if len(raw)>65536:raise ValueError('oversized model response')
    obj=json.loads(raw)
    value=obj['message']['content'] if url.endswith('/api/chat') else obj['choices'][0]['message']['content']
    if type(value)!=str or not value.strip():raise ValueError('empty model response')
    return value

def run(a_url,a_model,b_url,b_model):
    recv=ReceiveSequence(); session='local-llm-integration'; transcript=[]
    for index,(sender,url,model,prompt,kind) in enumerate([
        ('AgentA',a_url,a_model,'Propose a short task request for another AI agent that counts tokens in a document; state what must be clarified.','request'),
        ('AgentB',b_url,b_model,'Respond to this request with clarification questions, no execution or approval: {previous}','clarify'),
        ('AgentA',a_url,a_model,'Answer only clarifications which are known; explicitly mark any unknowns, do not fabricate authorization: {previous}','answer')]):
        response=infer(url,model,prompt.replace('{previous}',transcript[-1]['payload']['text'] if transcript else ''))
        frame={'version':VERSION,'session':session,'sequence':sum(f['sender']==sender for f in transcript),'sender':sender,'kind':kind,'payload':{'text':response}}
        frame=decode(encode(frame));recv.accept(frame);transcript.append(frame)
    return {'status':'transport-only','model_calls':len(transcript),'independent_endpoints':a_url!=b_url,'transcript':transcript,'limitations':'Not yet native-SCL semantic translation, signed authorization, or execution'}

if __name__=='__main__':
    p=argparse.ArgumentParser();
    for a in ('a','b'):
        p.add_argument('--'+a+'-url',required=True);p.add_argument('--'+a+'-model',required=True)
    args=p.parse_args();print(json.dumps(run(args.a_url,args.a_model,args.b_url,args.b_model),ensure_ascii=False,indent=2))
