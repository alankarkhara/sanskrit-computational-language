# SCL 0.8.9: scope, inference rules, and assurance boundary

## The computation is not a natural-language semantics

The SCL form `kārya_pramāṇa` has exactly one document declaration and one task declaration. Every accepted task operates on one immutable `UTF8Document` identified by the SHA-256 digest of exact bytes. The sole supported action `gaṇaya_śabdān` returns the number of tokens produced by Python `str.split()` on the strict UTF-8 decoding (Unicode whitespace splitting). This is a **particular declared token-counting algorithm**, not a natural-language theory of words. Exact Unicode and Python runtime versions can affect future interoperability; pin them for repeatable archival verification.

## Deterministic semantic judgment

Given source `s`, document bytes `d`, authority grant `g`, signed request `r`, fixed time `t`, and one-use nonce set `N`, the evaluator is a partial function:

`⟨s,d,g,r,t,N⟩ ⇓ (count(d), N∪{nonce(r)})`

**Only if** source fields are unique, object digest matches `SHA256(d)`, requester signature verifies, root-signed grant binds contract digest / requester / executor public key / operation / effect, expiration admits `t`, and nonce has not been used. Other cases deterministically reject. `count(d) = len(d.decode('utf-8', 'strict').split())`, for admitted inputs up to 65536 bytes. This interpreter produces one result or a specified rejection at this abstraction level, excluding operating-system failures.

### Paper proof sketch (not proof-assistant checked)

* Lemma 1: The restricted S-expression parser produces at most one tuple (deterministic recursive-descent algorithm). The unique-field checker rejects duplicates and unknown fields, so accepted syntactic contracts have a unique normalized mapping.
* Lemma 2: For fixed byte string `d`, decoding with strict UTF-8 and Unicode whitespace splitting is a deterministic computation in a pinned runtime. The output count is unique.
* Lemma 3: For fixed contract and signed envelope, validation functions select exactly success or rejection; successful execution has exactly one result value under the stated counting algorithm.
* Theorem (restricted determinism): Under a fixed implementation environment and supplied state, accepted tasks have one result. By Lemmas 1–3.

These statements are **informal proof sketches**, not universal mathematical soundness theorems and not machine-checked. They do not prove cryptographic security; Ed25519 authentication relies on standard cryptographic assumptions, correct library use, private-key secrecy, trusted root distribution and replay-state durability.

## Certificates

Request and grant signatures bind their canonical JSON contents. The signed result binds request, contract, bytes digest, executor key, output type, value, status and observation list. Requester checks the signatures and recomputes the result from local bytes. Hash functions and signatures do not independently certify that a remote agent used a specific execution trace, nor can they prevent an authorized malicious agent from lying without requester recomputation.

## Remaining production blockers

- Key generation, provisioning, revocation, durable replay counters, clock synchronization and trust anchors need deployment infrastructure.
- No cryptographically authenticated live network transport. The demonstration uses separate OS processes through local pipes; the signed payload is transport independent.
- No broad task ontology, effects beyond `pure`, or verifiable semantics for summarizing real documents, financial transfers, web research or file mutation.
- Formal proofs are not encoded/checked in Lean, Coq or Agda; no claim of complete general-language unambiguity.
- The existing 0.8.7 clarification machine is not unified with 0.8.9 signed requests; this is an additive language fragment.
