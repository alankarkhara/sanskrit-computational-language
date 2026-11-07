# SCL 0.6.1: Structured rule execution and bounded Pāṇinian examples

## Scope

This is an additive research module. It does not modify `scl.py`, historical rule modules, or the prior 0.6 tests. The new `grammar/structured_rules.py` implements immutable `Term` trees and `Var` patterns, first-order matching and unification with occurs check, nested rewrite positions, generation of syntactic critical pairs, and finite bounded reachability of normal forms.

## Critical pair procedure

For each ordered pair of rules `l1 → r1`, `l2 → r2`, rename their variables apart and consider every **non-variable** position `p` in `l1`. If the subterm `l1|p` unifies with `l2` under most general substitution σ, produce a peak `(σ(r1), σ(l1[r2]_p))`. For each peak, bounded breadth-first rewriting computes reachable normal forms; shared normal forms establish joinability of that peak *within the supported rule set and search budget*. Disjoint terminal normal-form sets are reported as non-joinable for that finite exploration. If the state bound is exceeded, the checker raises an error rather than concluding confluence.

**Do not infer global confluence** merely from finite examples. The textbook critical-pair lemma applies to all critical pairs of a specified left-linear first-order rewrite system under suitable assumptions; termination plus local confluence implies confluence (Newman's lemma). Here, neither global termination nor all semantic Pāṇinian conditions are certified. The report is bounded evidence, not a Lean-checked theorem.

## Soundness boundaries

The sandhi demonstrator is a *separate* typed boundary operation over IAST words with explicit `saṃhitā` context. It supports selected vowel boundaries associated with 6.1.77, 6.1.87, 6.1.88, and 6.1.101. The 6.1.101 subcase explicitly suppresses the general 6.1.77 transformation for homogeneous vowels. It refuses unknown boundaries. The source URI recorded in a certificate documents the sūtra; it does not imply that all inherited restrictions, phonological environments, precedence rules, or commentarial interpretations have been modeled.

References:
- https://www.sanskritlibrary.org/grammatical/data/A.6.1.77.html
- https://sanskritdictionary.com/panini/6-1-101
- https://www.learnsanskrit.org/vyakarana/sounds/ac-sandhi/

Each certificate replays the derivation and recomputes its digest. This detects edits but is not independent proof-assistant verification. The abstract critical-pair rules are general term-rewrite examples, not sourced Pāṇinian rules.

## Commands

```
python structured_cli.py dadhi indraḥ
python structured_cli.py dadhi indraḥ > cert.json
python structured_cli.py --verify cert.json
python -m unittest discover -s tests -q
```

## Open obligations

1. Refine the representation from generic term trees to explicitly typed grammatical state transitions and well-formedness checking.
2. Translate sourced sūtras into parameterized patterns with auditable anuvṛtti/adhikāra and phonological context, rather than relying on the specialized boundary evaluator.
3. Integrate true rule guards and exception relations into the critical-pair checker. The abstract checker currently has no classical Sanskrit precedence semantics.
4. Obtain scholarly assessment of the corpus and grammatical interpretation; integrate independent machine-checked proofs and source-to-IR certification.
5. Prove termination or implement stronger abstract interpretation for classes of potentially infinite term-rewrite systems.
