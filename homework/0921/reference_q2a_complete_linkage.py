"""REFERENCE IMAGE ONLY — copy this by hand onto paper and photograph YOUR OWN drawing
for submission. The instructor's rule: "A figure produced by scipy earns no marks for
this question." Do not submit this file or a screenshot of it.

Uses the actual computed merge sequence for Q2(a), complete linkage:
  {1,2} at 0.3, {3,4} at 0.45, {1,2}+{3,4} at 0.8
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 4.2))

x = {1: 1, 2: 2, 3: 3, 4: 4}

# fusion 1: {1,2} at 0.3
ax.plot([x[1], x[1]], [0, 0.3], color="black", lw=1.8)
ax.plot([x[2], x[2]], [0, 0.3], color="black", lw=1.8)
ax.plot([x[1], x[2]], [0.3, 0.3], color="black", lw=1.8)
ax.text(1.5, 0.32, "0.3", ha="center", fontsize=10, color="crimson")
mid12 = (x[1] + x[2]) / 2

# fusion 2: {3,4} at 0.45
ax.plot([x[3], x[3]], [0, 0.45], color="black", lw=1.8)
ax.plot([x[4], x[4]], [0, 0.45], color="black", lw=1.8)
ax.plot([x[3], x[4]], [0.45, 0.45], color="black", lw=1.8)
ax.text(3.5, 0.47, "0.45", ha="center", fontsize=10, color="crimson")
mid34 = (x[3] + x[4]) / 2

# fusion 3: {1,2} + {3,4} at 0.8
ax.plot([mid12, mid12], [0.3, 0.8], color="black", lw=1.8)
ax.plot([mid34, mid34], [0.45, 0.8], color="black", lw=1.8)
ax.plot([mid12, mid34], [0.8, 0.8], color="black", lw=1.8)
ax.text((mid12 + mid34) / 2, 0.82, "0.8", ha="center", fontsize=10, color="crimson")

for obs, xi in x.items():
    ax.text(xi, -0.03, str(obs), ha="center", va="top", fontsize=13, fontweight="bold")

ax.set_ylim(-0.05, 0.95)
ax.set_xlim(0.5, 4.5)
ax.set_ylabel("fusion height")
ax.set_xticks([])
ax.spines[["top", "right"]].set_visible(False)
ax.set_title("REFERENCE ONLY — copy by hand, do not submit this image", fontsize=9)
fig.tight_layout()
fig.savefig("reference_q2a_complete_linkage.png", dpi=170)
print("saved reference_q2a_complete_linkage.png")
