# SCL v0.6.4 — native grammatical evidence and scope controls

The SCL built-in `sandhi_pramāṇa(left,right)` computes a **restricted** vowel sandhi result. The AST-to-IR evidence sidecar records each literal invocation with its original AST path, AST digest, input/output, sūtra ID, inherited context, suppression decision, source URL, IR digest and review flag. Verification reparses and recompiles the source; alteration is rejected. Dynamic (nonliteral) calls may run but **are not eligible for native grammatical certificates**. No arbitrary rule is claimed authentic.

## Modelled classical features
* **Anuvṛtti:** explicit `saṃhitāyām` and (for 6.1.101) `aci` dependencies, limited to these sūtras.
* **Adhikāra:** 6.1.84 recorded for the two-vowel replacement in 6.1.101.
* **Apavāda / niyama:** homogeneous vowels select 6.1.101 rather than a simultaneous 6.1.77 transformation.
* **Asiddhatva:** no authentic general visibility semantics are implemented. Reject expansion as complete.

The proof chain is executable replay and hash integrity, **not** machine-checked source semantics. Lean is not installed, so no independent Lean compilation occurred. Substitution preservation is only the documented many-sorted induction argument in previous releases. Corpus is source-cross-checked against the links below but lacks third-party scholar sign-off.

## Source references
- 6.1.77: https://www.sanskritlibrary.org/grammatical/data/A.6.1.77.html
- 6.1.101: https://sanskritdictionary.com/panini/6-1-101

## Acceptance blockers
Independent Lean/Coq proof run, verified mapping to real interpreter small-step semantics, general classical visibility/inheritance, scholar-signed linguistic corpus, and sound proof of source-to-IR semantic preservation.
