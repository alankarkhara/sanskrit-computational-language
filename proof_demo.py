from proof_kernel.numeric import Num,Binary,check_derivation
from proof_kernel.rewrites import Var,Fun,Rule,certify
x=Var('x')
f=lambda a:Fun('f',(a,))
g=lambda a:Fun('g',(a,))
print('F0', check_derivation(Binary('+',Num(2),Binary('*',Num(3),Num(4)))))
for name,rules in [
    ('joinable',[Rule('outer',f(g(x)),g(x)),Rule('collapse',g(g(x)),g(x))]),
    ('nonconfluent',[Rule('A',f(g(x)),Fun('a')),Rule('B',f(g(x)),Fun('b'))])]:
    c=certify(rules)
    print(name, 'termination:',c['termination_certified'],'confluence:',c['confluence_certified'],'critical pairs:',len(c['critical_pairs']))
    for rec in c['critical_pairs']:
        print(' ',rec['rules'], 'at',rec['position'], 'joinable', rec['joinable'])
