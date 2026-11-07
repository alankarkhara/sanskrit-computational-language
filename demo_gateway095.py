"""Executable, offline demonstration. Not a live LLM experiment."""
import json
from core080.unified094 import Kernel
from core080.gateway095 import Gateway, verify_transcript
k=Kernel('task42','User',{'User':'manuṣya','AgentB':'abhikartṛ'}, {'doc42':'UTF8Document'},
         {'requester':'User','executor':'AgentB','operation':'gaṇaya_śabdān','object_id':'doc42'})
g=Gateway(k)
questions=g.request_clarification()
assert len(questions)==5
g.answer_by_owner({'object_type':'UTF8Document','result_type':'Int64','effect':'śuddha',
                   'constraints':['source_only','no_modify'],'permission':'internal'})
result=g.owner_review_and_approve(True)
assert result['state']=='approved' and verify_transcript(g.transcript())
print(json.dumps({'questions':questions,'state':result['state'],'contract':k.session.contract,
                  'integrity_valid':verify_transcript(g.transcript()),'executed':False},ensure_ascii=False,indent=2))
