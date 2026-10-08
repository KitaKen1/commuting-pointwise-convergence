# Complete Lean proof

Lean **v4.33.1**, Mathlib `0df444a360eaa60ab8c11dca51a86af692955474`.

[CommutingConvergence.lean](CommutingConvergence.lean) contains the complete proof
in one file, retaining all 334 original module bodies and their author notices.
[FCTargetProofs.lean](verification/FCTargetProofs.lean) proves the two FC-style
propositions without importing the statement placeholders.

```bash
lake update
lake exe cache get
python3 scripts/build_audit.py
```

The script builds the proof and freshly checks all 2,095 declarations listed in
[Axioms.lean](verification/Axioms.lean), followed by the two target proofs.
Reproduction logs go under `.lake/verification/`.
The [checked verification record](verification/build-results.json) records the
current source hashes and standard axiom checks.
