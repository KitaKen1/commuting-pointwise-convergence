# Complete Lean4Web proof

[CommutingConvergenceLean4Web.lean](CommutingConvergenceLean4Web.lean) contains the
complete proof, importing only Mathlib. Select **Lean v4.35.0-rc4** in Lean4Web.
Mathlib is pinned to `021ce68bf125a049beee22b3fc7664d78728e21d`.

```bash
lake update
lake exe cache get
lake build
```

The [verification record](build-results.json) certifies successful local
compilation and the two final target reports using only `propext`,
`Classical.choice`, and `Quot.sound`. Hosted browser execution is a separate check.
