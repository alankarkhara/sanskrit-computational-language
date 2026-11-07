"""Build SCL native source from actual requests/responses across two processes.
Deterministic dialogue agents are NOT generative AI models.
"""
import json,subprocess,sys
from pathlib import Path
from core080.native093 import compile_dialogue,verify_dialogue
from core080.clarify092 import Session
ROOT=Path(__file__).parent
agent=subprocess.Popen([sys.executable,str(ROOT/'agent093_process.py'),'AgentB'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1)
user=subprocess.Popen([sys.executable,str(ROOT/'agent093_process.py'),'User'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1)
try:
    agent.stdin.write(json.dumps({'kind':'request','task':'task42'})+'\n');agent.stdin.flush()
    ask=json.loads(agent.stdout.readline())
    assert ask=={'kind':'ask','actor':'AgentB'}
    session=Session({'User':'manuṣya','AgentB':'abhikartṛ'},{'doc42':'UTF8Document'},'task42',owner='User',contract={'requester':'User','executor':'AgentB','operation':'gaṇaya_śabdān','object_id':'doc42'})
    issues=session.ask('AgentB')
    user.stdin.write(json.dumps({'kind':'issues','issues':issues},ensure_ascii=False)+'\n');user.stdin.flush()
    answers=[]
    while True:
        msg=json.loads(user.stdout.readline());answers.append(msg)
        if msg['kind']=='propose_and_approve':break
    assert len(answers)==len(issues)+1
    fragments=['(spaṣṭa_saṃvāda',' (bhāgī User manuṣya)',' (bhāgī AgentB abhikartṛ)',' (vastu (id doc42) (prakāra UTF8Document))',' (ādeśa (id task42) (owner User) (requester User) (executor AgentB) (operation gaṇaya_śabdān) (object_id doc42))',' (spaṣṭīkaraṇa (kartṛ AgentB))']
    for msg in answers[:-1]:
        assert msg['kind']=='answer'
        f,v=msg['field'],msg['value'];assert f.isidentifier() and v.replace(',','').isidentifier()
        session.answer('User',{f: v.split(',') if f=='constraints' else v})
        fragments.append(f' (uttara (kartṛ User) (kṣetra {f}) (mūlya {v}))')
    assert session.requirements()==[]
    fragments+=[' (prastāva)',' (anumodana (kartṛ User))',')']
    source='\n'.join(fragments)+'\n';certificate=compile_dialogue(source)
    assert verify_dialogue(source,certificate)
    assert certificate['clarification']['state']=='approved'
    (ROOT/'LIVE093_TRANSCRIPT.scl').write_text(source,encoding='utf-8')
    (ROOT/'LIVE093_CERTIFICATE.json').write_text(json.dumps(certificate,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'agents':'two independent OS processes, deterministic rule-driven, not LLMs','questions':len(issues),'responses':len(answers)-1,'status':certificate['clarification']['state'],'verification':True},ensure_ascii=False))
finally:
    agent.terminate();user.terminate();agent.wait(timeout=5);user.wait(timeout=5)
    for p in (agent,user):p.stdin.close();p.stdout.close()
