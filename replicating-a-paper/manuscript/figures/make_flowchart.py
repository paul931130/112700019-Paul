"""Draws the experimental-design flow chart used in main.tex.

Run:  python make_flowchart.py   ->  flowchart.pdf (used by LaTeX) and flowchart.png (preview)
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["pdf.fonttype"] = 42

fig, ax = plt.subplots(figsize=(6.5, 6.7))
ax.set_xlim(0, 10)
ax.set_ylim(1.3, 11.9)
ax.axis("off")

GRAY, BLUE, GREEN, EDGE = "#f2f2f2", "#dbe7f3", "#e3f0dc", "#333333"


def box(cx, cy, w, h, text, fc=GRAY, size=7.6):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                                boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=EDGE, lw=0.9))
    lines = text.split("\n")
    n = len(lines)
    step = size * 0.0205 * 1.55
    y0 = cy + step * (n - 1) / 2
    for i, ln in enumerate(lines):
        ax.text(cx, y0 - i * step, ln, ha="center", va="center", fontsize=size,
                fontweight="bold" if i == 0 else "normal")


def arrow(p, q):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=9, lw=0.9,
                                 color=EDGE, shrinkA=0, shrinkB=0))


box(5, 11.2, 8.6, 1.15,
    "1. Raw data (Feng et al., 2019, NASDAQ)\n"
    "1,026 tickers × 1,246 trading days;\n"
    "industry relation tensor (1,026 × 1,026 × 97)")
box(5, 9.55, 8.6, 1.15,
    "2. Preprocessing\n"
    "Treat the −1234 sentinel as missing\n"
    "Features: normalized close + 5-, 10-, 20-, 30-day moving averages\n"
    "Target: next-day return ratio")
box(5, 7.95, 8.6, 0.95,
    "3. Split by date (same for both models)\n"
    "train: days 0–755  |  validation: 756–1007  |  test: 1008–")

box(2.9, 5.95, 4.4, 1.55,
    "4a. Baseline: Rank_LSTM\nLSTM over each stock's own\nhistory; no relation graph", fc=GREEN, size=7.2)
box(7.5, 5.95, 3.8, 1.55,
    "4b. RSR (implicit, RSR_I)\nbaseline's exported embedding\n+ attention over the\nstatic industry graph",
    fc=GREEN, size=7.0)

box(5, 3.8, 8.6, 1.15,
    "5. Training (identical settings, two independent runs)\n"
    "Adam, seq = 4, unit = 32; loss = MSE + α × pairwise ranking penalty\n"
    "50 epochs; test metrics taken at the best-validation epoch")
box(5, 2.1, 8.6, 1.15,
    "6. Evaluation on the test split\n"
    "MSE  |  MRR (reciprocal true rank of top pick)  |  IRR (return of top pick)\n"
    "compared with Table 6 (NASDAQ) of the original paper")

arrow((5, 10.62), (5, 10.12))
arrow((5, 8.97), (5, 8.43))
arrow((2.9, 7.47), (2.9, 6.73))
arrow((7.5, 7.47), (7.5, 6.73))
arrow((5.1, 5.95), (5.6, 5.95))
arrow((2.9, 5.17), (2.9, 4.38))
arrow((7.5, 5.17), (7.5, 4.38))
arrow((5, 3.22), (5, 2.68))

fig.savefig("flowchart.pdf", bbox_inches="tight", pad_inches=0.05)
fig.savefig("flowchart.png", dpi=170, bbox_inches="tight", pad_inches=0.05)
print("saved flowchart.pdf, flowchart.png")
