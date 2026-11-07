"""Independent deterministic dialogue participants. No LLM inference or remote API."""
import json,sys
role=sys.argv[1]
for line in sys.stdin:
    msg=json.loads(line)
    if role=='AgentB' and msg['kind']=='request':
        print(json.dumps({'kind':'ask','actor':'AgentB'},ensure_ascii=False),flush=True)
    elif role=='User' and msg['kind']=='issues':
        known={'object_type':'UTF8Document','result_type':'Int64','effect':'śuddha','constraints':'source_only,no_modify','permission':'internal'}
        for issue in msg['issues']:
            field=issue['field']
            if field not in known:print(json.dumps({'kind':'decline','field':field}),flush=True)
            else:print(json.dumps({'kind':'answer','actor':'User','field':field,'value':known[field]},ensure_ascii=False),flush=True)
        print(json.dumps({'kind':'propose_and_approve','actor':'User'}),flush=True)
