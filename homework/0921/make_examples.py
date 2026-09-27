"""Illustrative examples only — toy numbers, NOT the textbook's Q2/Q3 data.
Shows the expected style: labeled fusion heights, and a K-means iteration grid.
Run: python make_examples.py -> example_dendrogram.png, example_kmeans.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------------
# Example 1: dendrogram sketch style (toy dissimilarities, 4 points)
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5, 4))
# hand-sketch-style joins: (x_left, x_right, height, label)
# leaves at x = 1,2,3,4 named A,B,C,D
leaf_x = {"A": 1, "B": 2, "C": 3, "D": 4}
for name, x in leaf_x.items():
    ax.text(x, -0.15, name, ha="center", va="top", fontsize=12, fontweight="bold")
    ax.plot([x, x], [0, 0.4], color="black", lw=1.5)

# fusion 1: B+C at height 0.4
ax.plot([2, 3], [0.4, 0.4], color="black", lw=1.5)
ax.plot([2.5, 2.5], [0.4, 1.1], color="black", lw=1.5)
ax.text(2.6, 0.75, "0.4", fontsize=10, color="crimson")

# fusion 2: A + (BC) at height 1.1
ax.plot([1, 1], [0, 1.1], color="black", lw=1.5)
ax.plot([1, 2.5], [1.1, 1.1], color="black", lw=1.5)
ax.plot([1.75, 1.75], [1.1, 1.9], color="black", lw=1.5)
ax.text(1.85, 1.45, "1.1", fontsize=10, color="crimson")

# fusion 3: (ABC) + D at height 1.9
ax.plot([4, 4], [0, 1.9], color="black", lw=1.5)
ax.plot([1.75, 4], [1.9, 1.9], color="black", lw=1.5)
ax.text(3.0, 1.95, "1.9", fontsize=10, color="crimson")

ax.set_ylim(-0.3, 2.3)
ax.set_xlim(0.5, 4.5)
ax.set_ylabel("fusion height (dissimilarity)")
ax.set_title("Example only — not the assignment's data\nlabel every fusion height as you draw it by hand", fontsize=10)
ax.spines[["top", "right", "bottom"]].set_visible(False)
ax.set_xticks([])
fig.tight_layout()
fig.savefig("example_dendrogram.png", dpi=170)
print("saved example_dendrogram.png")

# ---------------------------------------------------------------
# Example 2: K-means iteration grid (toy points, K=2)
# ---------------------------------------------------------------
rng = np.random.default_rng(0)
pts = np.array([[1, 1], [1.5, 2], [3, 4], [5, 7], [3.5, 5], [4.5, 5]])
labels_by_iter = [
    np.array([0, 1, 0, 1, 0, 1]),   # iter 0: random start
    np.array([0, 0, 1, 1, 1, 1]),   # iter 1
    np.array([0, 0, 0, 1, 1, 1]),   # iter 2: converged
]
fig, axes = plt.subplots(1, 3, figsize=(9.5, 3.2), sharex=True, sharey=True)
colors = ["#4472c4", "#ed7d31"]
for ax, labels, title in zip(axes, labels_by_iter, ["iteration 0\n(random assignment)", "iteration 1\n(reassign to nearest centroid)", "iteration 2\n(converged)"]):
    for k in (0, 1):
        m = labels == k
        ax.scatter(pts[m, 0], pts[m, 1], c=colors[k], s=90, edgecolor="black", zorder=3)
        if m.sum():
            cx, cy = pts[m].mean(axis=0)
            ax.scatter([cx], [cy], marker="x", s=140, c=colors[k], linewidths=3, zorder=4)
    for i, (x, y) in enumerate(pts):
        ax.annotate(str(i + 1), (x, y), textcoords="offset points", xytext=(6, 6), fontsize=9)
    ax.set_title(title, fontsize=9)
    ax.set_xlim(0, 6.5)
    ax.set_ylim(0, 8)
fig.suptitle("Example only — not the assignment's data. × marks each cluster's centroid.", fontsize=10)
fig.tight_layout(rect=[0, 0, 1, 0.92])
fig.savefig("example_kmeans.png", dpi=170)
print("saved example_kmeans.png")
