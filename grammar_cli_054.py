"""Experimental bounded Paninian foundations CLI."""
import argparse,json
from grammar.foundations import pratyahara,it_marker,sandhi_extended,GrammarScopeError

def main():
    ap=argparse.ArgumentParser(description='Bounded Pāṇinian phonology and metalanguage')
    sub=ap.add_subparsers(dest='command',required=True)
    p=sub.add_parser('pratyahara');p.add_argument('name')
    q=sub.add_parser('it');q.add_argument('upadesha');q.add_argument('--category',default='affix')
    r=sub.add_parser('sandhi');r.add_argument('left');r.add_argument('right')
    a=ap.parse_args()
    try:
        if a.command=='pratyahara':result={'class':a.name,'members':pratyahara(a.name)}
        elif a.command=='it':result=it_marker(a.upadesha,a.category)
        else:result=sandhi_extended(a.left,a.right)
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except GrammarScopeError as exc:ap.error(str(exc))
if __name__=='__main__':main()
