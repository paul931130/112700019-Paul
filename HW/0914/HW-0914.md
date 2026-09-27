# HW-0914 — Answers

ISLP §2.4, Exercises 2, 3(b), 7. (Q3(a) is a separate hand-drawn photo, `HW-0914-Q3a.jpg`;
Q8 is a separate notebook, `HW-0914-Q8.ipynb`.)

---

## Q2 — classification/regression, inference/prediction, n and p

| Scenario | Classification / Regression | Inference / Prediction | n | p |
|---|---|---|---|---|
| (a) Top 500 US firms: profit, employees, industry → CEO salary | **Regression** — CEO salary is a continuous quantity, not a category | **Inference** — the question is "which factors *affect* CEO salary," i.e. understanding the relationship, not forecasting an unseen firm's salary | 500 | 3 (profit, number of employees, industry) |
| (b) New product launch: 20 past products, price/marketing budget/competition price + 10 others → success or failure | **Classification** — the response is binary (success/failure) | **Prediction** — the goal is to know whether *the new product* will succeed, not to explain why past products succeeded | 20 | 13 (price, marketing budget, competition price, + 10 other variables) |
| (c) USD/Euro % change vs. weekly % change in US/British/German markets, all weeks of 2012 | **Regression** — % change is continuous | **Prediction** — forecasting the exchange-rate change from market movements | 52 (weeks in 2012) | 3 (% change in US, British, German markets) |

---

## Q3(b) — why each curve has that shape

- **Training error** falls monotonically as flexibility increases, because a more flexible model
  has more capacity to fit the exact points it was trained on — with enough flexibility it can
  interpolate the training data almost perfectly, driving training error toward zero (and, with
  enough parameters, **below** the irreducible error, since the model is now fitting noise
  specific to that training sample rather than the true signal).
- **(Squared) bias** falls as flexibility increases, because a rigid, low-flexibility model (e.g.
  a straight line) can't bend to match a truly non-linear relationship — that mismatch *is* bias —
  and more flexible models can approximate the true f more closely.
- **Variance** rises as flexibility increases, because a flexible model chases the specific noise
  in whichever training sample it happened to see; a small change in the training data swings a
  high-flexibility fit around a lot more than it swings a rigid one.
- **Test error** is **U-shaped** because it decomposes into bias² + variance + irreducible error
  (Eq. 2.7 in the book): bias² is falling and variance is rising as flexibility increases, so their
  sum has a minimum somewhere in the middle — too little flexibility underfits (bias dominates),
  too much overfits (variance dominates), and the U's minimum is the flexibility level that best
  trades one off against the other.
- **Irreducible (Bayes) error** is flat, because it comes from the random noise ε in Y itself, not
  from the model — no amount of tuning the method's flexibility can push it down, which is exactly
  why it forms a horizontal floor that the test-error curve can approach but never cross.

---

## Q7 — K-nearest neighbours

Data (test point X₁=X₂=X₃=0):

| Obs. | X1 | X2 | X3 | Y |
|---|---|---|---|---|
| 1 | 0 | 3 | 0 | Red |
| 2 | 2 | 0 | 0 | Red |
| 3 | 0 | 1 | 3 | Red |
| 4 | 0 | 1 | 2 | Green |
| 5 | -1 | 0 | 1 | Green |
| 6 | 1 | 1 | 1 | Red |

**(a) Euclidean distances** to (0,0,0), d = √(X1² + X2² + X3²):

| Obs. | Calculation | Distance |
|---|---|---|
| 1 | √(0²+3²+0²) = √9 | 3.000 |
| 2 | √(2²+0²+0²) = √4 | 2.000 |
| 3 | √(0²+1²+3²) = √10 | 3.162 |
| 4 | √(0²+1²+2²) = √5 | 2.236 |
| 5 | √(1²+0²+1²) = √2 | **1.414** |
| 6 | √(1²+1²+1²) = √3 | 1.732 |

**(b) K = 1:** the single nearest observation is **Obs. 5** (distance 1.414) → prediction **Green**.

**(c) K = 3:** the three nearest are Obs. 5 (1.414, Green), Obs. 6 (1.732, Red), Obs. 2 (2.000, Red)
→ majority vote is 2 Red vs. 1 Green → prediction **Red**.

**(d)** **Small.** A highly non-linear Bayes boundary needs a flexible, very local decision rule to
trace it — a small K only looks at the nearest handful of points, so the fitted boundary can bend
sharply to follow a non-linear true boundary. A large K averages over many neighbours across a
wider region, smoothing the decision boundary toward something closer to linear — exactly the
opposite of what a highly non-linear boundary needs.
