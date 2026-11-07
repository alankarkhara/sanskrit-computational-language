# SCL 0.4.2 Formal Safety Addendum

Use this release as a **compatibility-preserving** successor to 0.4.1. Run `python scl.py examples/niyama.scl --rewrite-policy formal` or inspect `python scl.py examples/niyama.scl --rewrite-policy formal --emit-ir`. Run all regression tests with `python -m unittest discover -s tests -v`.

- Legacy mode is still the default for backward compatibility.
- `formal` mode accepts only checked **ground integer** rewrites; symbolic and effectful rewrites are skipped.
- New effect and type judgment helpers are available in the `scl` module.
- IR includes formal effect and cautious confluence reports, while preserving 0.4.1 AST schema.
- Case evidence is explicitly separated from semantically assigned kāraka roles.

Read `FORMAL_SEMANTICS.md` for operational rules, restricted preservation argument, nonconfluence limitations, and open proof obligations.
