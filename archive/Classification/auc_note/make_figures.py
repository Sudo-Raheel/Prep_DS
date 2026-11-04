"""Generate all figures (and print the numbers quoted in main.tex).

Run:  python3 make_figures.py      ->  figs/*.pdf
"""
import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import norm

try:
    from scipy.integrate import trapezoid
except ImportError:  # older scipy
    from numpy import trapz as trapezoid

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figs")
os.makedirs(OUT, exist_ok=True)

# --- palette (validated categorical slots 1-3 + one blue ramp for prevalence) ---
INK, MUTED, GRID = "#222222", "#6b6a66", "#e3e2de"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
BLUES = ["#a9c9f2", "#6aa5e8", "#2a78d6", "#12457f"]  # light -> dark

plt.rcParams.update(
    {
        "font.family": "serif",
        "mathtext.fontset": "cm",
        "font.size": 9,
        "text.color": INK,
        "axes.edgecolor": MUTED,
        "axes.labelcolor": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "axes.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.6,
        "legend.frameon": False,
        "savefig.bbox": "tight",
        "pdf.fonttype": 42,
    }
)
LW = 1.8


def save(fig, name):
    fig.savefig(os.path.join(OUT, name))
    plt.close(fig)


# ----------------------------------------------------------------------------
# Binormal score model: S|neg ~ N(0,1), S|pos ~ N(mu,1)
# ----------------------------------------------------------------------------
MU = 2.0


def binormal_roc(mu=MU, n=60001):
    t = np.linspace(-12, 16, n)
    fpr, tpr = norm.sf(t), norm.sf(t - mu)
    return fpr[::-1], tpr[::-1]  # ascending


def precision(tpr, fpr, k):
    den = tpr + k * fpr
    return np.divide(tpr, den, out=np.ones_like(tpr), where=den > 0)


def ap_integral(tpr, fpr, k):
    return trapezoid(precision(tpr, fpr, k), tpr)


fpr, tpr = binormal_roc()
auc_roc = trapezoid(tpr, fpr)
print(f"binormal mu={MU}: ROC-AUC = {auc_roc:.4f}  (closed form {norm.cdf(MU/np.sqrt(2)):.4f})")

PIS = [0.5, 0.1, 0.01, 0.001]
print("\nprevalence | k | AP | AP/pi | ROC-AUC")
for pi in PIS:
    k = (1 - pi) / pi
    ap = ap_integral(tpr, fpr, k)
    print(f"{pi:>8} | {k:8.1f} | {ap:.4f} | {ap/pi:7.1f} | {auc_roc:.4f}")

# operating point used later: TPR = 0.8
t80 = MU + norm.isf(0.8)  # sf(t-mu)=0.8
f80 = norm.sf(t80)
print(f"\nTPR=0.8 operating point: FPR = {f80:.4f}")
for pi in PIS:
    k = (1 - pi) / pi
    p = 0.8 / (0.8 + k * f80)
    print(f"  pi={pi}: precision={p:.4f}, FDR={1-p:.4f}")

# Empirical sanity check with sklearn (sampled data)
try:
    from sklearn.metrics import average_precision_score, roc_auc_score

    rng = np.random.default_rng(0)
    for pi in [0.1, 0.001]:
        n_neg = 1_000_000
        n_pos = int(round(n_neg * pi / (1 - pi)))
        s = np.r_[rng.normal(0, 1, n_neg), rng.normal(MU, 1, n_pos)]
        y = np.r_[np.zeros(n_neg), np.ones(n_pos)]
        print(
            f"sklearn check pi={pi}: n_pos={n_pos}, ROC-AUC={roc_auc_score(y, s):.4f}, "
            f"AP={average_precision_score(y, s):.4f}"
        )
except Exception as e:  # pragma: no cover
    print("sklearn check skipped:", e)

# ----------------------------------------------------------------------------
# Figure 1: ROC curve and PR curves for the same model at four prevalences
# ----------------------------------------------------------------------------
fig, (a, b) = plt.subplots(1, 2, figsize=(6.6, 2.9))
a.plot(fpr, tpr, color=BLUE, lw=LW)
a.plot([0, 1], [0, 1], color=MUTED, lw=1.0, ls="--")
a.fill_between(fpr, 0, tpr, color=BLUE, alpha=0.10, lw=0)
a.text(0.55, 0.38, f"ROC-AUC = {auc_roc:.3f}", color=INK)
a.text(0.52, 0.12, "random: 0.5", color=MUTED)
a.set(xlim=(0, 1), ylim=(0, 1.02), xlabel="False positive rate (FPR)", ylabel="True positive rate (TPR)")
a.set_title("(a) ROC curve", loc="left", fontsize=9.5)
a.set_aspect("equal", adjustable="box")

for pi, c in zip(PIS, BLUES[::-1]):  # darkest = most balanced
    k = (1 - pi) / pi
    p = precision(tpr, fpr, k)
    ap = trapezoid(p, tpr)
    b.plot(tpr, p, color=c, lw=LW, label=rf"$\pi={pi:g}$:  AP = {ap:.3f}")
    b.axhline(pi, color=c, lw=0.9, ls=":")
b.set(xlim=(0, 1), ylim=(0, 1.02), xlabel="Recall (TPR)", ylabel="Precision")
b.set_title("(b) PR curves, same classifier", loc="left", fontsize=9.5)
b.legend(loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=2, fontsize=7.8, handlelength=1.6, columnspacing=1.2)
fig.tight_layout(w_pad=2.0)
save(fig, "fig_curves.pdf")

# ----------------------------------------------------------------------------
# Figure 2: sweep prevalence for the fixed classifier
# ----------------------------------------------------------------------------
pis = np.logspace(np.log10(0.5), -5, 70)
aps = np.array([ap_integral(tpr, fpr, (1 - p) / p) for p in pis])
fdr80 = np.array([1 - 0.8 / (0.8 + ((1 - p) / p) * f80) for p in pis])

fig, (a, b) = plt.subplots(1, 2, figsize=(6.6, 2.8))
a.axhline(auc_roc, color=BLUE, lw=LW)
a.plot(pis, aps, color=ORANGE, lw=LW)
a.plot(pis, pis, color=MUTED, lw=1.0, ls="--")
a.set_xscale("log")
a.invert_xaxis()
a.set(ylim=(0, 1.02), xlabel=r"Prevalence $\pi$ (more imbalanced $\rightarrow$)", ylabel="Metric value")
a.text(2e-2, auc_roc + 0.03, "ROC-AUC (flat)", color=INK)
a.text(4e-3, 0.28, "AUC-PR (AP)", color=INK)
a.text(2e-4, 0.07, r"baseline = $\pi$", color=MUTED)
a.set_title("(a) Same classifier, varying $\\pi$", loc="left", fontsize=9.5)

b.plot(pis, fdr80, color=ORANGE, lw=LW)
b.set_xscale("log")
b.invert_xaxis()
b.set(
    ylim=(0, 1.02),
    xlabel=r"Prevalence $\pi$ (more imbalanced $\rightarrow$)",
    ylabel="Share of alerts that are false",
)
b.text(3e-3, 0.30, "fixed ROC point:\nTPR = 0.80, FPR = 0.123", color=INK, fontsize=8)
b.set_title("(b) False-alert share at that point", loc="left", fontsize=9.5)
fig.tight_layout(w_pad=2.0)
save(fig, "fig_sweep.pdf")

# ----------------------------------------------------------------------------
# Figure 3: toy example (10 transactions, 3 frauds)
# ----------------------------------------------------------------------------
labels = np.array([1, 0, 1, 0, 0, 1, 0, 0, 0, 0])
P, N = labels.sum(), (1 - labels).sum()
tp = np.cumsum(labels)
fp = np.cumsum(1 - labels)
roc_x = np.r_[0, fp / N]
roc_y = np.r_[0, tp / P]
prec_k = tp / np.arange(1, len(labels) + 1)
rec_k = tp / P
auc_toy = trapezoid(roc_y, roc_x)
ap_toy = np.sum(prec_k[labels == 1]) / P
print(f"\ntoy: ROC-AUC = {auc_toy:.4f} (17/21 = {17/21:.4f}),  AP = {ap_toy:.4f}")

fig, (a, b) = plt.subplots(1, 2, figsize=(6.6, 2.9))
a.step(roc_x, roc_y, where="post", color=BLUE, lw=LW)
a.fill_between(roc_x, 0, roc_y, step="post", color=BLUE, alpha=0.10, lw=0)
a.plot([0, 1], [0, 1], color=MUTED, lw=1.0, ls="--")
a.scatter(roc_x, roc_y, s=14, color=BLUE, zorder=3)
a.text(0.50, 0.30, r"area = $17/21\approx0.81$", color=INK)
a.set(xlim=(-0.02, 1.02), ylim=(-0.02, 1.04), xlabel="FPR", ylabel="TPR")
a.set_title("(a) ROC: pairwise view", loc="left", fontsize=9.5)
a.set_aspect("equal", adjustable="box")

# AP as a step-wise sum
xs = np.r_[0, rec_k[labels == 1]]
for i in range(P):
    h = prec_k[labels == 1][i]
    b.fill_between([xs[i], xs[i + 1]], 0, h, color=ORANGE, alpha=0.18, lw=0)
    b.plot([xs[i], xs[i + 1]], [h, h], color=ORANGE, lw=LW)
b.plot(rec_k, prec_k, "o:", color=MUTED, lw=1.0, ms=3.5, zorder=3)
b.axhline(P / (P + N), color=MUTED, lw=0.9, ls="--")
b.text(0.02, 0.32, r"baseline $\pi=0.30$", color=MUTED, fontsize=8)
b.text(0.40, 0.88, r"AP = $(1+\frac{2}{3}+\frac{1}{2})/3\approx0.72$", color=INK, fontsize=8.5)
b.set(xlim=(0, 1.02), ylim=(0, 1.05), xlabel="Recall", ylabel="Precision")
b.set_title("(b) PR: precision at each fraud", loc="left", fontsize=9.5)
fig.tight_layout(w_pad=2.0)
save(fig, "fig_toy.pdf")

# ----------------------------------------------------------------------------
# Figure 4: Model A vs Model B  (piecewise-linear ROC curves, k = 999)
# ----------------------------------------------------------------------------
K = 999.0
PI = 1 / (1 + K)
models = {
    "A": (np.array([0, 0.6, 1.0]), np.array([0, 0.001, 1.0]), BLUE),
    "B": (np.array([0, 0.8, 1.0]), np.array([0, 0.2, 1.0]), ORANGE),
}
r = np.linspace(1e-9, 1, 400001)
fig, (a, b) = plt.subplots(1, 2, figsize=(6.6, 2.9))
res = {}
for name, (vt, vf, c) in models.items():
    g = np.interp(r, vt, vf)
    p = precision(r, g, K)
    ap = trapezoid(p, r)
    auc = trapezoid(vt, vf)
    p_vertex = vt[1] / (vt[1] + K * vf[1])
    res[name] = (auc, ap, p_vertex)
    a.plot(vf, vt, color=c, lw=LW)
    a.scatter([vf[1]], [vt[1]], s=22, color=c, zorder=3)
    b.plot(r, p, color=c, lw=LW)
    b.scatter([vt[1]], [p_vertex], s=22, color=c, zorder=3)
a.plot([0, 1], [0, 1], color=MUTED, lw=1.0, ls="--")
a.text(0.55, 0.70, "A", color=INK, fontweight="bold")
a.text(0.40, 0.92, "B", color=INK, fontweight="bold")
a.text(0.40, 0.12, "ROC-AUC: A 0.7995,  B 0.8000", color=INK, fontsize=8)
a.set(xlim=(0, 1), ylim=(0, 1.02), xlabel="FPR", ylabel="TPR")
a.set_title("(a) ROC: almost identical", loc="left", fontsize=9.5)
a.set_aspect("equal", adjustable="box")

b.axhline(PI, color=MUTED, lw=0.9, ls="--")
b.text(0.12, 0.03, r"baseline $\pi=0.001$", color=MUTED, fontsize=8)
b.text(0.12, 0.42, f"A  (AP = {res['A'][1]:.3f})", color=INK, fontsize=8.5)
b.annotate(f"B  (AP = {res['B'][1]:.4f})", xy=(0.45, 0.004), xytext=(0.55, 0.12), fontsize=8.5, color=INK,
           arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.set(xlim=(0, 1), ylim=(0, 0.5), xlabel="Recall (TPR)", ylabel="Precision")
b.set_title(r"(b) PR at $\pi=0.001$: very different", loc="left", fontsize=9.5)
fig.tight_layout(w_pad=2.0)
save(fig, "fig_models.pdf")

print("\nModels A/B (k=999):")
for n, (auc, ap, pv) in res.items():
    print(f"  {n}: ROC-AUC={auc:.4f}  AP={ap:.5f}  precision@vertex={pv:.5f}  AP/baseline={ap/PI:.1f}")
print(f"  AP_A / AP_B = {res['A'][1]/res['B'][1]:.1f}")
