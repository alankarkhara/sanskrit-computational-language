import argparse,json,sys
from grammar.derivation import derive,verify,DerivationError,registry
p=argparse.ArgumentParser(description='SCL bounded Paninian sandhi derivations')
p.add_argument('left',nargs='?');p.add_argument('right',nargs='?');p.add_argument('--verify');p.add_argument('--coverage',action='store_true')
a=p.parse_args()
try:
    if a.coverage:out=registry()
    elif a.verify:
        with open(a.verify,encoding='utf8') as f:cert=json.load(f)
        out={'valid':verify(cert)}
        if not out['valid']:sys.exit('Certificate rejected')
    else:
        if not a.left or not a.right:p.error('two operands required')
        out=derive(a.left,a.right)
    print(json.dumps(out,ensure_ascii=False,indent=2))
except (ValueError,FileNotFoundError) as e:sys.exit(str(e))
