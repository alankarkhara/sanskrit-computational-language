import argparse,json,sys
from pathlib import Path
from grammar.typed_state import derive,verify,StateError

def main():
    parser=argparse.ArgumentParser(description='Bounded typed Sanskrit derivation')
    parser.add_argument('dhatu',nargs='?',default='paṭh')
    parser.add_argument('pratyaya',nargs='?',default='tip')
    parser.add_argument('--verify',metavar='FILE')
    args=parser.parse_args()
    if args.verify:
        ok=verify(json.loads(Path(args.verify).read_text(encoding='utf8')))
        print('VALID' if ok else 'INVALID');return 0 if ok else 1
    try:print(json.dumps(derive(args.dhatu,args.pratyaya),ensure_ascii=False,indent=2));return 0
    except StateError as ex:print(str(ex),file=sys.stderr);return 2
if __name__=='__main__':sys.exit(main())
