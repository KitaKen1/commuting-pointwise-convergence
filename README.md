# Pointwise convergence for two commuting transformations in Lean 4

The pointwise convergence conjecture for two commuting transformations is the following
([Frantzikinakis, Section 5.2.5, Problem 19](https://arxiv.org/html/1103.3808v3#S5.SS2.SSS5)):

> **Conjecture.**
>
> Let $`(X,\mathcal B,\mu)`$ be a probability space, and let $`T,S:X\to X`$
> be commuting, invertible, measure-preserving transformations with measurable
> inverses. For every $`f,g\in L^\infty(\mu)`$, the averages
>
> ```math
> A_N(f,g)(x)=\frac1N\sum_{n=0}^{N-1}f(T^n x)g(S^n x)
> ```
>
> converge as $`N\to\infty`$ for $`\mu`$-almost every $`x`$.

This repository presents a **Lean 4 proof** of this conjecture.
Ergodicity is not required. Convergence is asserted for each fixed pair of inputs.

Contributions:

1. **FC-style formalization** of the commuting-transformation conjecture.
2. **Lean 4 proof** of almost-everywhere convergence for bounded inputs.

SubContribution:

1. **A stronger theorem** for $`L^2(\mu)\times L^2(\mu)`$ inputs,
   with an FC-style statement and proof ([appendix](#appendix-square-integrable-inputs-and-formal-scope)).

<!-- PUBLICATION_LINKS_START -->
**Try it in Lean4Web:** [open the complete proof in one file](https://live.lean-lang.org/#url=https%3A%2F%2Fraw.githubusercontent.com%2FKitaKen1%2Fcommuting-pointwise-convergence%2Fmain%2Flean4web%2FCommutingConvergenceLean4Web.lean) (Lean **v4.35.0-rc4**).
<!-- PUBLICATION_LINKS_END -->

## Formal Conjectures targets

[CommutingPointwiseConvergence.lean](FClikelean/CommutingPointwiseConvergence.lean)
states the **bounded-input conjecture** in the namespace `CommutingConvergence`:

```lean
@[category research solved, AMS 37,
    formal_proof using lean4 at "https://github.com/KitaKen1/commuting-pointwise-convergence/blob/main/lean/verification/FCTargetProofs.lean"]
theorem commutingPointwiseConvergence :
    answer(True) ↔
      ∀ (X : Type*) [MeasurableSpace X] (μ : Measure X) [IsProbabilityMeasure μ]
        (T S : X ≃ᵐ X),
        MeasurePreserving T μ μ → MeasurePreserving S μ μ →
        Function.Commute (T : X → X) (S : X → X) →
        ∀ (f g : X → ℂ), MemLp f ∞ μ → MemLp g ∞ μ →
          ∀ᵐ x ∂μ, ∃ L : ℂ,
            Tendsto (fun N : ℕ ↦ (N : ℂ)⁻¹ *
              ∑ n ∈ Finset.range N, f (T^[n] x) * g (S^[n] x)) atTop (𝓝 L) := by
  sorry
```

The same file states the **square-integrable-input theorem**:

```lean
@[category research solved, AMS 37,
    formal_proof using lean4 at "https://github.com/KitaKen1/commuting-pointwise-convergence/blob/main/lean/verification/FCTargetProofs.lean"]
theorem commutingPointwiseConvergenceL2 :
    answer(True) ↔
      ∀ (X : Type*) [MeasurableSpace X] (μ : Measure X) [IsProbabilityMeasure μ]
        (T S : X ≃ᵐ X),
        MeasurePreserving T μ μ → MeasurePreserving S μ μ →
        Function.Commute (T : X → X) (S : X → X) →
        ∀ (f g : X → ℂ), MemLp f 2 μ → MemLp g 2 μ →
          ∀ᵐ x ∂μ, ∃ L : ℂ,
            Tendsto (fun N : ℕ ↦ (N : ℂ)⁻¹ *
              ∑ n ∈ Finset.range N, f (T^[n] x) * g (S^[n] x)) atTop (𝓝 L) := by
  sorry
```

Both targets use the official Formal Conjectures annotations and place
`answer(True)` outside all quantifiers. Their `by sorry` bodies are FC
problem-statement placeholders. The `formal_proof` annotations link to
[FCTargetProofs.lean](lean/verification/FCTargetProofs.lean), which proves the
same propositions and prints their axioms using the complete results in
[CommutingConvergence.lean](lean/CommutingConvergence.lean).
The FC statement placeholders are not proof dependencies.
These are local FC-style contributions; the [FC-style statement file](FClikelean/CommutingPointwiseConvergence.lean)
records the proposed upstream scope.

## Mathematical explanation (AI generated)

The proof first controls finite maxima of oscillations for two Gaussian-based
kernels on the plane. It transfers this estimate to commuting flows, recovers
the interval kernel by approximation, and reconstructs the discrete averages.

**1. A planar estimate with the maximum inside the integral.** Put

```math
\varphi(t)=(2\pi)^{-1/2}e^{-t^2/2},\qquad
E(t)=(3-t^2)\varphi(t),\qquad O(t)=(3t-t^3)\varphi(t),
```

and write $`D_rK(t)=r^{-1}K(t/r)`$. For bounded measurable functions on
$`\mathbb R^2`$, define

```math
\mathcal A_N^K(F,G)(u,v)
=\int_{\mathbb R}K(t)F(u+Nt,v)G(u,v+Nt)\,dt.
```

For $`m\ge1`$ and a finite nonempty family $`\mathcal F`$ of increasing positive-integer chains
$`\boldsymbol n=(n_0,\ldots,n_m)`$, set

```math
M_{\mathcal F}(a)
=\max_{\boldsymbol n\in\mathcal F}
  \sum_{j=1}^m|a_{n_j}-a_{n_{j-1}}|.
```

The key estimate **(1)**, for $`r,L>0`$, $`K=D_rE`$ or $`D_rO`$, and inputs supported in
$`Q_L=[-L,L]^2`$, is

```math
\int_{\mathbb R^2}M_{\mathcal F}(\mathcal A^K(F,G))(p)\,dp
\le |Q_L|\,C_K\|F\|_\infty\|G\|_\infty\sqrt{m}.
```

The bound is uniform over the finite family. Keeping the maximum inside the
integral allows the maximizing chain to depend on the spatial point.

**2. Matrix energy and Gaussian derivatives supply (1).** On a finite grid,
the proof represents three inputs by Gaussian-weighted matrices and uses the
energy $`\Phi(P)=\mathrm{tr}(P^{3/2})`$. A mixed trace inequality
controls cyclic products by quadratic insertion costs. Gaussian heat
identities turn these costs into dissipation of the matrix energy.

The selected intervals are encoded by changing entries on one edge of the
cyclic product. Each entry switches at most $`2m`$ times. The rank-change
formula and one-dimensional maximal estimates control the total cost of
these switches. After normalizing the three input norms to
$`(m^{-1/2},1,1)`$ and restoring them by trilinearity, the resulting bound
has the form $`C\sqrt m\prod_{v=0}^2\|G_v\|_3`$.

The derivative orders needed for the two kernels are exactly $`3,4,5`$:

```math
\partial_{\log L}D_LE=-D_L\varphi^{(4)},\qquad
\partial_{\log L}D_LO=D_L(\varphi^{(5)}+3\varphi^{(3)}).
```

Fix the finite interval menu first. Its positive lower endpoints have a
common positive minimum, so the masked scale kernel vanishes below it.
The proof then passes through grid limits, approximation of measurable
finite choices, and $`L^3`$ input density. Four phases $`1,-1,i,-i`$ suffice
to control the complex increments. A box indicator as the third input
supplies the volume factor in (1). This qualitative route uses
positive-integer chains throughout.

**3. Spatial transference turns sublinear oscillation into convergence.**
Let $`U_t,V_t`$ be commuting, jointly measurable, measure-preserving real actions on a probability
space $`(Y,\nu)`$. Apply (1) to orbit functions
$`F_y(u,v)=f(U_uV_vy)`$ and $`G_y(u,v)=g(U_uV_vy)`$, cut off in large boxes.
Measure preservation, followed by removal of the box and kernel-tail
cutoffs, gives

```math
\int_Y M_{\mathcal F}(a^K(y))\,d\nu(y)\le C_m,\qquad
 a_N^K(y)=\int_{\mathbb R}K(t)f(U_{Nt}y)g(V_{Nt}y)\,dt,
\qquad \frac{C_m}{m}\longrightarrow0.
```

There are countably many integer chains. Monotone convergence therefore
extends the estimate to their supremum $`J_m`$. If a sequence is not Cauchy,
some $`\eta>0`$ permits chains of every length with successive increments
at least $`\eta`$. At that point $`J_m\ge m\eta`$ for every $`m`$.
Markov's inequality bounds the measure of this event by
$`\inf_m C_m/(m\eta)=0`$. Taking a countable union over rational
$`\eta>0`$ proves almost-everywhere convergence for the Euler kernels.

**4. Passing from Gaussian kernels to the interval kernel.** For bounded
inputs, the real kernels for which $`a_N^K`$ converges almost everywhere form
a closed linear subspace of $`L^1(\mathbb R)`$, because

```math
\sup_N|a_N^K(y)-a_N^H(y)|
\le\|f\|_\infty\|g\|_\infty\|K-H\|_1.
```

Integrating the dilation identities for $`E`$ and $`O`$, then taking finite
differences in the Gaussian parameter, puts all polynomial Gaussian kernels
in this subspace. Gaussian moment determinacy gives polynomial density in
Gaussian $`L^2`$. Consequently, $`\mathbf1_{(0,1)}`$ is an $`L^1`$ limit
of polynomial Gaussian kernels, and

```math
\frac1N\int_0^N f(U_ty)g(V_ty)\,dt
```

converges almost everywhere.

**5. Exact phase reconstruction recovers the discrete averages.** Suspend
the two integer actions on $`Y=X\times[0,1)^2`$:

```math
U_t(x,u,v)=(T^{\lfloor u+t\rfloor}x,\{u+t\},v),\qquad
V_t(x,u,v)=(S^{\lfloor v+t\rfloor}x,u,\{v+t\}).
```

These are commuting measurable measure-preserving real actions. For the
lifted functions, write

```math
B_N(x,u,v)=\frac1N\int_0^N
f(T^{\lfloor t+u\rfloor}x)g(S^{\lfloor t+v\rfloor}x)\,dt.
```

With $`w(u,v)=3-6|u-v|`$, integration over the phase square gives the exact
identity

```math
\int_0^1\!\int_0^1w(u,v)B_N(x,u,v)\,dv\,du
=A_N(f,g)(x)+\frac{f(T^Nx)g(S^Nx)-f(x)g(x)}{2N}.
```

The two off-diagonal coefficients cancel and the diagonal coefficients each
integrate to $`1/2`$. Fubini and dominated convergence give convergence of
the left side for almost every $`x`$. The boundary term tends to zero for
bounded inputs, proving the conjecture. The square-integrable extension
follows by the truncation argument in the appendix.

## Files

| Directory | Contents |
|---|---|
| [paper/](paper/) | Revised proof manuscript, full PDF and TeX source |
| [lean/](lean/) | Complete single-file proof, Lean 4.33.1 |
| [lean4web/](lean4web/) | Complete single-file edition, verified locally on Lean 4.35.0-rc4 |
| [FClikelean/](FClikelean/) | FC-style bounded and square-integrable statements with proof references |

The complete proofs are in
[CommutingConvergence.lean](lean/CommutingConvergence.lean).
The same file
provides real-valued forms, both index conventions, representative invariance,
and explicit measurable inverse maps.

## Build and verification

```bash
cd lean
lake update
lake exe cache get
python3 scripts/build_audit.py
```

Dependencies are pinned. The complete proofs use only
`[propext, Classical.choice, Quot.sound]`.
See the [verification record](lean/verification/build-results.json) for build and axiom-audit results.
The original modular edition passed an isolated rebuild of all **4,110 dependency/project source modules** and a
fresh **2,095-declaration axiom audit**. Its compact single-file edition was then
compiled and all 2,095 declarations audited again. The complete single-file edition
also passed local compilation on **v4.35.0-rc4** with the same standard axiom set
for its two final targets. Hosted browser execution is not claimed.

## References

- Nikos Frantzikinakis, [*Some open problems on multiple ergodic averages*, Section 5.2.5, Problem 19](https://arxiv.org/html/1103.3808v3#S5.SS2.SSS5): the commuting-transformation pointwise convergence question.
- **OpenAI**, *Annular variation of the triangular Hilbert transform at the symmetric point*, fixed revision `adc7f1241b42e322a6451854ab7e4b4c146bf78a`: the [matrix inequalities](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/build/sections/matrix.tex), [Gaussian heat identities](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/build/sections/heat.tex), and [maximal estimates](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/build/sections/preliminaries.tex) used in the written proof. Exact lemma labels appear in the manuscript appendix.
- **TauCeti contributors**, [TauCeti](https://github.com/TauCetiProject/TauCeti/tree/b4b6003311d14474661f1d2763df2e767180fd64): adopted Gaussian moment, Hermite derivative, moment determinacy, and maximal-estimate results.
- **LeanPool contributors**, [LeanPool](https://github.com/Vilin97/lean-pool/tree/01db1d7049cf9668bda1e9e106875ee1278b43e6): the adopted pointwise Birkhoff theorem.
- **The Formal Conjectures Authors**, [`google-deepmind/formal-conjectures`](https://github.com/google-deepmind/formal-conjectures/tree/89294ea02bd7cd678d59984add52cb4baef3dbf4): the official `answer` elaborator and problem attributes used by the FC targets.
- [Lean 4](https://github.com/leanprover/lean4) and the [Lean community's Mathlib](https://github.com/leanprover-community/mathlib4): the proof assistant and mathematical library used for the formalization.

The project uses the [Apache-2.0 license](LICENSE). Adopted files retain their
author notices and the [TauCeti license](lean/LICENSE-TauCeti)
and [LeanPool license](lean/LICENSE-LeanPool).
Copies of these licenses also accompany the single-file edition.

## AI usage disclosure

This formalization, mathematical exploration, proof development, and documentation were produced by Kenta Kitamura with assistance from ChatGPT and OpenAI Codex using GPT-6 Astra and GPT-6.1 sol.

## Appendix: square-integrable inputs and formal scope

The stronger theorem is:

> **Theorem.** Under the same hypotheses on $`(X,\mathcal B,\mu,T,S)`$,
> the averages $`A_N(f,g)(x)`$ converge to a finite limit almost everywhere
> for every $`f,g\in L^2(\mu)`$.

Let $`f_M=f\mathbf1_{\{|f|\le M\}}`$ and
$`g_M=g\mathbf1_{\{|g|\le M\}}`$, and denote ordinary ergodic averages
by $`P_N^Th=N^{-1}\sum_{n=0}^{N-1}h\circ T^n`$. Cauchy–Schwarz gives

```math
\begin{aligned}
|A_N(f,g)-A_N(f_M,g_M)|
&\le (P_N^T|f-f_M|^2)^{1/2}(P_N^S|g|^2)^{1/2}\\
&\quad +(P_N^T|f|^2)^{1/2}(P_N^S|g-g_M|^2)^{1/2}.
\end{aligned}
```

The pointwise Birkhoff theorem supplies finite limits for these ordinary
averages. The tail limits have integrals tending to zero; along a summable
subsequence of truncation levels, both vanish almost everywhere. Since each
bounded truncation already converges, the displayed estimate forces the
original averages to be Cauchy almost everywhere.

On a probability space, $`L^\infty`$ and $`L^3`$ are contained in $`L^2`$.
The formal library also proves real-valued versions with real limits and
shows that sums over $`0,\ldots,N-1`$ and $`1,\ldots,N`$ have the same limit.
Changing representatives leaves every discrete average unchanged on one
common set of full measure for the chosen representatives.

The formalized planar estimate concerns finite maxima over positive-integer
chains, sufficient for this qualitative convergence theorem. Stronger
quantitative variation assertions at arbitrary real scales are outside the
formal scope stated here.

## Appendix: timeline

| Year | Who | Stage | Problem or result |
|---|---|---|---|
| 2016 | [Nikos Frantzikinakis](https://arxiv.org/html/1103.3808v3#S5.SS2.SSS5) | Survey formulation | Pointwise convergence for two commuting transformations (Problem 19). |
| 2026 | **This repository (Kenta Kitamura)** | **Lean 4 proof** | Proves the conjecture and its $`L^2\times L^2`$ extension. |

## Appendix: manuscript

- [Revised proof manuscript](paper/commuting-convergence-revised.pdf)
- [Original manuscript](https://github.com/KitaKen1/commuting-pointwise-convergence/blob/db68ff5e411e71a580073c942666286b9f6df743/PDF/commuting-convergence.pdf)
