"""Illustrative example only — toy dissimilarities, NOT the textbook's Q2 matrix.
Shows single vs. complete linkage disagreeing on the 2-cluster cut, which is the
point of Q2(c)/(d): "the two can disagree."

Toy dissimilarity matrix (made up for this illustration):
        A     B     C     D
  A     -    0.3   0.9   0.5
  B    0.3    -    0.4   0.5
  C    0.9   0.4    -    1.0
  D    0.5   0.5   1.0    -

Both methods merge A,B first (smallest distance, 0.3). After that they disagree:
  single  (uses the MIN distance to a merged group) attaches C next -> ((A,B)C)D
  complete (uses the MAX distance to a merged group) attaches D next -> ((A,B)D)C

Run: python make_linkage_comparison.py -> linkage_comparison.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def draw_tree(ax, order, heights, title):
    # order: list of 4 leaf labels in left-to-right x position
    # heights: (h1, h2, h3) = height of 1st, 2nd, 3rd fusion, in merge sequence
    # sequence is always: order[0]+order[1] first, then order[2] joins, then order[3] joins
    x = {name: i + 1 for i, name in enumerate(order)}
    h1, h2, h3 = heights

    for name in order:
        ax.plot([x[name], x[name]], [0, h1 if name in order[:2] else 0], color="black", lw=1.5)

    # fusion 1: leaves 0,1
    a, b = order[0], order[1]
    ax.plot([x[a], x[a]], [0, h1], color="black", lw=1.5)
    ax.plot([x[b], x[b]], [0, h1], color="black", lw=1.5)
    ax.plot([x[a], x[b]], [h1, h1], color="black", lw=1.5)
    mid1 = (x[a] + x[b]) / 2
    ax.text(mid1 + 0.08, (h1) / 2, f"{h1:.2f}", fontsize=9, color="crimson")

    # fusion 2: {a,b} + leaf 2
    c = order[2]
    ax.plot([mid1, mid1], [h1, h2], color="black", lw=1.5)
    ax.plot([x[c], x[c]], [0, h2], color="black", lw=1.5)
    ax.plot([mid1, x[c]], [h2, h2], color="black", lw=1.5)
    mid2 = (mid1 + x[c]) / 2
    ax.text(mid2 + 0.08, (h1 + h2) / 2, f"{h2:.2f}", fontsize=9, color="crimson")

    # fusion 3: {a,b,c} + leaf 3
    d = order[3]
    ax.plot([mid2, mid2], [h2, h3], color="black", lw=1.5)
    ax.plot([x[d], x[d]], [0, h3], color="black", lw=1.5)
    ax.plot([mid2, x[d]], [h3, h3], color="black", lw=1.5)
    ax.text((mid2 + x[d]) / 2 + 0.08, (h2 + h3) / 2, f"{h3:.2f}", fontsize=9, color="crimson")

    for name in order:
        ax.text(x[name], -0.05 * h3, name, ha="center", va="top", fontsize=12, fontweight="bold")

    ax.set_title(title, fontsize=11)
    ax.set_xlim(0.5, 4.5)
    ax.set_ylim(-0.12 * h3, h3 * 1.25)
    ax.set_xticks([])
    ax.spines[["top", "right", "bottom"]].set_visible(False)


fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.3))

# single linkage: A,B merge first, then C joins {A,B}, then D joins last
draw_tree(axes[0], ["A", "B", "C", "D"], heights=(0.30, 0.40, 0.50), title="Single linkage\ncut for 2 clusters: {A, B, C} vs {D}")

# complete linkage: A,B merge first, then D joins {A,B}, then C joins last
draw_tree(axes[1], ["A", "B", "D", "C"], heights=(0.30, 0.50, 1.00), title="Complete linkage\ncut for 2 clusters: {A, B, D} vs {C}")

axes[0].set_ylabel("fusion height (dissimilarity)")
fig.suptitle(
    "Example only — toy dissimilarities, not the assignment's matrix.\n"
    "Both start by merging A, B (their distance is smallest). After that the methods disagree:\n"
    "single linkage (uses the closest pair between groups) attaches C next; "
    "complete linkage (uses the farthest pair) attaches D next.\n"
    "That is why cutting each tree for 2 clusters gives a different grouping — this is what Q2(c)/(d) ask you to notice.",
    fontsize=9,
)
fig.tight_layout(rect=[0, 0, 1, 0.80])
fig.savefig("linkage_comparison.png", dpi=170)
print("saved linkage_comparison.png")
