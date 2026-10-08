# FC-compatible statements with linked complete proofs

[CommutingPointwiseConvergence.lean](CommutingPointwiseConvergence.lean) contains
the bounded and square-integrable targets, with `answer(True)` outside all
quantifiers, `category research solved`, `AMS 37` and `formal_proof` links.
Following the Formal Conjectures statement format, this file has two `by sorry`
statement placeholders. They are excluded from proof certification.

The actual complete proofs, containing no proof placeholders, are in
[../lean/verification/FCTargetProofs.lean](../lean/verification/FCTargetProofs.lean).
They apply the adjoining proved convergence theorems and print their axiom sets.
The Lean4Web edition contains these complete proof terms.

This statement project uses Lean `v4.33.1` and Formal Conjectures utilities at
commit `89294ea02bd7cd678d59984add52cb4baef3dbf4`.

```bash
lake update
lake build
```

An upstream contribution and its acceptance are separate from local certification.
