/-
Copyright 2026 Kenta Kitamura (KitaKen1).
-/
import CommutingConvergence

/-!
# Complete proofs of the Formal Conjectures targets

These are the propositions stated with `answer(True)` in
`FClikelean/CommutingPointwiseConvergence.lean`. Here the affirmative answer
is written as `True`, without importing the FC statement placeholders.
The complete proof terms and their axiom reports are retained for verification
and for generation of the Mathlib-only Lean4Web edition.
-/

open MeasureTheory Filter
open scoped BigOperators Topology ENNReal

namespace CommutingConvergence

/-- The original bounded-input commuting-transformation question has a positive
answer. Invertibility includes measurability of the inverse. -/
theorem commutingPointwiseConvergence :
    True ↔
      ∀ (X : Type*) [MeasurableSpace X] (μ : Measure X) [IsProbabilityMeasure μ]
        (T S : X ≃ᵐ X),
        MeasurePreserving T μ μ → MeasurePreserving S μ μ →
        Function.Commute (T : X → X) (S : X → X) →
        ∀ (f g : X → ℂ), MemLp f ∞ μ → MemLp g ∞ μ →
          ∀ᵐ x ∂μ, ∃ L : ℂ,
            Tendsto (fun N : ℕ ↦ (N : ℂ)⁻¹ *
              ∑ n ∈ Finset.range N, f (T^[n] x) * g (S^[n] x)) atTop (𝓝 L) := by
  constructor
  · intro _ X _ μ _ T S hT hS hTS f g hf hg
    exact commuting_pointwise_bounded μ T S hT hS hTS f g hf hg
  · intro _
    trivial

/-- The same averages converge almost everywhere for square-integrable inputs. -/
theorem commutingPointwiseConvergenceL2 :
    True ↔
      ∀ (X : Type*) [MeasurableSpace X] (μ : Measure X) [IsProbabilityMeasure μ]
        (T S : X ≃ᵐ X),
        MeasurePreserving T μ μ → MeasurePreserving S μ μ →
        Function.Commute (T : X → X) (S : X → X) →
        ∀ (f g : X → ℂ), MemLp f 2 μ → MemLp g 2 μ →
          ∀ᵐ x ∂μ, ∃ L : ℂ,
            Tendsto (fun N : ℕ ↦ (N : ℂ)⁻¹ *
              ∑ n ∈ Finset.range N, f (T^[n] x) * g (S^[n] x)) atTop (𝓝 L) := by
  constructor
  · intro _ X _ μ _ T S hT hS hTS f g hf hg
    exact commuting_pointwise_l2 μ T S hT hS hTS f g hf hg
  · intro _
    trivial

end CommutingConvergence

#print axioms CommutingConvergence.commutingPointwiseConvergence
#print axioms CommutingConvergence.commutingPointwiseConvergenceL2
