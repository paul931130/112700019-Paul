"""Draws the experimental-design flow chart used in main.tex.

Run:  python make_flowchart.py   ->  flowchart.pdf (used by LaTeX) and flowchart.png (preview)
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["pdf.fonttype"] = 42

fig, ax = plt.subplots(figsize=(6.5, 8.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 13)
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


# 1-3: data, preprocessing, split
box(5, 12.2, 8.6, 1.15,
    "1. Raw data (Feng et al., 2019, NASDAQ)\n"
    "1,026 tickers × 1,246 trading days;\n"
    "industry relation file (97 industries)")
box(5, 10.5, 8.6, 1.15,
    "2. Preprocessing\n"
    "Treat the −1234 sentinel as missing\n"
    "Features: 5-, 10-, 20-, 30-day moving averages + close ratio,\n"
    "each normalized by the stock's maximum price")
box(5, 8.85, 8.6, 0.95,
    "3. Split by date (same for all models)\n"
    "train: days 0–755  |  validation: 756–1007  |  test: 1008–")

# 4: relation graphs
box(5.0, 7.0, 2.9, 1.35,
    "4a. Static graph\nIndustry one-hot,\n1,026 × 1,026;\nconstant during training",
    fc=BLUE, size=7.2)
box(8.3, 7.0, 2.9, 1.35,
    "4b. Dynamic graph\nRolling 60-day\ncorrelation, |corr| > 0.5;\nwindows built\nwithin each split",
    fc=BLUE, size=7.0)

# 5: models
box(1.7, 4.75, 2.9, 1.55, "5a. Baseline\nRank_LSTM\nno relation graph", fc=GREEN, size=7.2)
box(5.0, 4.75, 2.9, 1.55,
    "5b. RSR\nbaseline's exported LSTM\nembedding + attention\nover the static graph",
    fc=GREEN, size=7.0)
box(8.3, 4.75, 2.9, 1.55,
    "5c. Dynamic relation\n(extension): same as RSR,\ngraph fed per\n60-day window",
    fc=GREEN, size=7.0)

# 6-7: training, evaluation
box(5, 2.6, 8.6, 1.15,
    "6. Training (identical for all three models)\n"
    "Adam, seq = 4, unit = 32; loss = MSE + α × pairwise ranking penalty\n"
    "10-epoch pilot, then matched 50-epoch runs")
box(5, 1.0, 8.6, 1.0,
    "7. Evaluation on the test split\n"
    "MSE  |  mrrt (top-pick reciprocal rank)  |  btl (long-only backtest return)")

# arrows
arrow((5, 11.62), (5, 11.08))
arrow((5, 9.92), (5, 9.33))
arrow((1.7, 8.37), (1.7, 5.55))
arrow((5.0, 8.37), (5.0, 7.68))
arrow((8.3, 8.37), (8.3, 7.68))
arrow((5.0, 6.32), (5.0, 5.55))
arrow((8.3, 6.32), (8.3, 5.55))
for x in (1.7, 5.0, 8.3):
    arrow((x, 3.97), (x, 3.18))
arrow((5, 2.02), (5, 1.5))

fig.savefig("flowchart.pdf", bbox_inches="tight", pad_inches=0.05)
fig.savefig("flowchart.png", dpi=170, bbox_inches="tight", pad_inches=0.05)
print("saved flowchart.pdf, flowchart.png")
