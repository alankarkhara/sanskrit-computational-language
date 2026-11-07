"""Usage: python sentence_cli.py 'rāmaḥ phalam paṭhati'"""
import argparse,json
from grammar.sentence import parse_sentence
p=argparse.ArgumentParser()
p.add_argument('sentence')
args=p.parse_args()
print(json.dumps(parse_sentence(args.sentence),ensure_ascii=False,indent=2))
