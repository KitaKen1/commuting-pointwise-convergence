# Pointwise Convergence for Two Commuting Transformations

The pointwise convergence conjecture for two commuting transformations states the following.

> [!NOTE]
> **Conjecture (Pointwise convergence for two commuting transformations).**
>
> Let $(X,\mathcal B,\mu)$ be a probability space, and let $T,S:X\to X$ be commuting invertible measure-preserving transformations. For every $f,g\in L^\infty(\mu)$, the averages
>
> $$A_N(f,g)(x)=\frac1N\sum_{n=0}^{N-1}f(T^n x)g(S^n x)$$
>
> converge as $N\to\infty$ for $\mu$-almost every $x$.

This repository presents a proposed proof of this conjecture for submission to **Formal Conjectures**. A proof sketch follows; the [PDF manuscript](PDF/commuting-convergence.pdf) contains the detailed proof.

## Proof sketch

### 1. Obtain a finite maximal estimate for kernel averages

Define the standard Gaussian density and two kernels by

$$
\varphi(t)=\frac{e^{-t^2/2}}{\sqrt{2\pi}},\qquad
E(t)=(3-t^2)\varphi(t),\qquad O(t)=(3t-t^3)\varphi(t),
$$

and write $D_rK(t)=r^{-1}K(t/r)$ for $r>0$. On the plane, set

$$
\mathcal A_N^K(F,G)(u,v)
=\int_{\mathbb R}K(t)F(u+Nt,v)G(u,v+Nt)\,dt.
$$

An increasing chain is a tuple $\mathbf n=(n_0<\cdots<n_m)$ of positive integers.

**Planar finite maximal estimate.** For each $K=D_rE,D_rO$ and bounds $C_f,C_g\ge0$, there are finite constants $C_m\ge0$ with $C_m/m\to0$ such that

$$
\int_{\mathbb R^2}\max_{\mathbf n\in\mathcal F}
\sum_{j=1}^{m}
\left|\mathcal A_{n_j}^K(F,G)-\mathcal A_{n_{j-1}}^K(F,G)\right|
\le |Q_L|\,C_m
$$

for every $L>0$, every bounded measurable pair $F,G$ supported in $Q_L=[-L,L]^2$ with $|F|\le C_f$ and $|G|\le C_g$, and every finite nonempty family $\mathcal F$ of increasing chains of length $m$.

The constants are independent of $L,F,G,\mathcal F$. **The maximum must remain inside the integral.** Separate integral estimates for individual chains do not supply this estimate.

The manuscript gives the following derivation. Higher Gaussian derivatives are represented by probability averages of first-order score insertions with a narrower row variance. Joint convexity of the matrix cost controls these insertions. Single-edge energy dissipation controls the additional column costs arising from averaging the heat flow over the centers. Counting switches of scale intervals entry by entry, with choices allowed to depend on the output point, gives the bound

$$
C\left[\sum_{v=0}^2 n_v^3+m\{n_0^3+n_0^2(n_1+n_2)\}\right],
$$

where $n_v$ are the three input $L^3$ norms. Normalizing these norms to $(m^{-1/2},1,1)$ and then restoring them by trilinearity yields $C\sqrt m\prod_v n_v$. The identities

$$
\partial_{\log L}D_LE=-D_L\varphi^{(4)},\qquad
\partial_{\log L}D_LO=D_L(\varphi^{(5)}+3\varphi^{(3)})
$$

then give an $L^{3/2}$ bound for the pointwise supremum of increment sums for the E/O kernels. When both inputs are supported in $Q_L$, the output also vanishes outside $Q_L$. Hölder's inequality therefore gives the planar estimate with $C_m=C C_fC_g\sqrt m$. **The higher-derivative and switching argument is the analytic part that still requires verification.**

### 2. Transfer the estimate to a suspension and obtain E/O convergence

On $Y=X\times[0,1)^2$, define

$$
U_t(x,u,v)=(T^{\lfloor u+t\rfloor}x,\{u+t\},v),\qquad
V_t(x,u,v)=(S^{\lfloor v+t\rfloor}x,u,\{v+t\}).
$$

These are commuting measure-preserving flows. Lift $f,g$ to $Y$ and apply the planar estimate to their orbit functions.

Fix a finite family of chains, let $B$ be its largest scale, and choose a kernel tail radius $R$. Cutting off the orbit functions on $Q_{L+BR}$ changes each average on $Q_L$ by an error controlled uniformly by the kernel's $L^1$ tail. If each average changes by at most $\varepsilon$, every increment sum and its finite maximum change by at most $2m\varepsilon$. Letting $L\to\infty$ makes the ratio of square areas tend to $1$; then letting the tail error vanish transfers the planar estimate to the suspension with the same $C_m$.

Monotone convergence from finite maxima to the supremum $J_m$ over all increasing chains gives $\int_YJ_m\le C_m$. At every point where the averages are not Cauchy, some $\varepsilon>0$ satisfies $J_m\ge m\varepsilon$ for all $m$. Markov's inequality and $C_m/m\to0$ show that these points form a null set. Thus each E/O kernel average converges almost everywhere.

### 3. Pass from E/O kernels to the interval kernel

For $0<\delta<1$, differentiation and integration give

$$
\int_\delta^1s^2E(st)\,ds=\varphi(t)-\delta^3\varphi(\delta t),
\qquad
\int_\delta^1sO(st)\,ds=t\varphi(t)-t\delta^3\varphi(\delta t).
$$

The $L^1$ norms of the remainder terms are constant multiples of $\delta^2$ and $\delta$, respectively. Approximating the scale integrals in $L^1$ yields convergence for the even and odd Gaussian kernels at every positive rate.

For $a>0$, $k\in\{0,1\}$, and integers $j\ge0$, we also have

$$
t^ke^{-at^2}\left(\frac{1-e^{-ht^2}}h\right)^j
\longrightarrow t^{k+2j}e^{-at^2}
\quad\text{in }L^1(\mathbb R)
\quad\text{as }h\downarrow0.
$$

The left side is a finite linear combination of Gaussian kernels. This extends convergence to polynomial Gaussian kernels. Density of polynomials in Gaussian $L^2$ then gives an $L^1$ approximation of $\chi=\mathbf1_{(0,1)}$ by such kernels.

For bounded inputs, replacing $K$ by $K'$ changes every average by at most $C_fC_g\|K-K'\|_1$, uniformly in the scale. Hence the time averages associated with $\chi$ also converge almost everywhere.

### 4. Recover the discrete averages by phase integration

Set

$$
B_N(x,u,v)=\frac1N\int_0^N
f(T^{\lfloor t+u\rfloor}x)g(S^{\lfloor t+v\rfloor}x)\,dt,
\qquad w(u,v)=3-6|u-v|.
$$

Splitting each unit time interval into its phase cells and integrating gives the exact identity

$$
\int_0^1\!\int_0^1 w(u,v)B_N(x,u,v)\,dv\,du
=A_N(f,g)(x)+\frac{f(T^Nx)g(S^Nx)-f(x)g(x)}{2N}.
$$

Fubini's theorem and dominated convergence pass almost-everywhere convergence on the product space to the phase integral. The endpoint term tends to zero, so the discrete averages converge. This completes the manuscript's argument for the conjecture using the planar estimate established in Step 1. No restriction of a product null set to the phase diagonal is needed.

### 5. Extend from bounded inputs to $L^2\times L^2$

Let $f_M=f\mathbf1_{\{|f|\le M\}}$ and $g_M=g\mathbf1_{\{|g|\le M\}}$. Cauchy–Schwarz for finite sums bounds the difference between the original and truncated averages by ordinary Birkhoff averages of $|f-f_M|^2$, $|g-g_M|^2$, $|f|^2$, and $|g|^2$.

Birkhoff's theorem and the vanishing $L^1$ norms of the squared tails yield a common subsequence along which both tail conditional expectations tend to zero almost everywhere. Combining this with convergence for bounded inputs proves that the original averages are Cauchy almost everywhere. Thus convergence extends to $L^2\times L^2$, and in particular for $L^3\times L^3$. □

## Detailed proof

- [Proof manuscript (PDF)](PDF/commuting-convergence.pdf)
