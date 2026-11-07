"""Verify a v0.8.1 certificate with the separately authored v0.8.2 checker."""
import argparse,json,sys
from core080.independent082 import check
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('certificate')
a=p.parse_args()
try:
    with open(a.source,encoding='utf-8') as f:s=f.read()
    with open(a.certificate,encoding='utf-8') as f:cert=json.load(f)
    valid=check(s,cert)
except (OSError,ValueError):valid=False
print('VALID' if valid else 'INVALID')
sys.exit(0 if valid else 1)
