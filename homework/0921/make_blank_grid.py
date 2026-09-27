"""Blank grid template for hand-drawing the Q2 dendrograms — no dendrogram content,
just axis scaffolding (leaf positions + height gridlines) to draw on top of, by hand.
Run: python make_blank_grid.py -> blank_dendrogram_grid.png (print or trace on screen)
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(9, 4.5))
for ax, title in zip(axes, ["Blank grid — for (a)", "Blank grid — for (b)"]):
    for x in (1, 2, 3, 4):
        ax.axvline(x, color="#dddddd", lw=1, zorder=0)
        ax.text(x, -0.04, str(x), ha="center", va="top", fontsize=12, fontweight="bold")
    for h in [round(i * 0.1, 1) for i in range(0, 11)]:
        ax.axhline(h, color="#eeeeee", lw=0.8, zorder=0)
    ax.set_yticks([round(i * 0.1, 1) for i in range(0, 11)])
    ax.set_xlim(0.5, 4.5)
    ax.set_ylim(-0.05, 1.0)
    ax.set_xticks([])
    ax.set_ylabel("fusion height")
    ax.set_title(title, fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)

fig.suptitle("Blank template only — no answer drawn. Add your own fusion lines by hand.", fontsize=10)
fig.tight_layout(rect=[0, 0, 1, 0.93])
fig.savefig("blank_dendrogram_grid.png", dpi=170)
print("saved blank_dendrogram_grid.png")
