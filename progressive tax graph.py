import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 1200, 10000)
breakpoints = [14, 50, 88, 150, 300, 500, 1000]
epsilon = 0.08

ranges = [
    (0,    14,   lambda x: x*0.06,                   lambda x: x*0.06,  lambda x: x*0.94,                   lambda x: x*0.94),
    (14,   50,   lambda x: 0.84+0.15*(x-14),         lambda x: x*0.15,  lambda x: x-(0.84+0.15*(x-14)),     lambda x: x*0.85),
    (50,   88,   lambda x: 6.24+0.24*(x-50),         lambda x: x*0.24,  lambda x: x-(6.24+0.24*(x-50)),     lambda x: x*0.76),
    (88,   150,  lambda x: 15.36+0.35*(x-88),        lambda x: x*0.35,  lambda x: x-(15.36+0.35*(x-88)),    lambda x: x*0.65),
    (150,  300,  lambda x: 37.06+0.38*(x-150),       lambda x: x*0.38,  lambda x: x-(37.06+0.38*(x-150)),   lambda x: x*0.62),
    (300,  500,  lambda x: 94.06+0.40*(x-300),       lambda x: x*0.40,  lambda x: x-(94.06+0.40*(x-300)),   lambda x: x*0.60),
    (500,  1000, lambda x: 174.06+0.42*(x-500),      lambda x: x*0.42,  lambda x: x-(174.06+0.42*(x-500)),  lambda x: x*0.58),
    (1000, 1200, lambda x: 384.06+0.45*(x-1000),     lambda x: x*0.45,  lambda x: x-(384.06+0.45*(x-1000)), lambda x: x*0.55),
]

f1 = np.full_like(x, np.nan)
g1 = np.full_like(x, np.nan)
f2 = np.full_like(x, np.nan)
g2 = np.full_like(x, np.nan)

for x_start, x_end, fn_f1, fn_g1, fn_f2, fn_g2 in ranges:
    mask = (x > x_start) & (x < x_end)
    f1[mask] = fn_f1(x[mask])
    g1[mask] = fn_g1(x[mask])
    f2[mask] = fn_f2(x[mask])
    g2[mask] = fn_g2(x[mask])

# Used epsilon to handle discontinuities.
for bp in breakpoints:
    bp_mask = (x > bp - epsilon) & (x < bp + epsilon)
    f1[bp_mask] = np.nan
    g1[bp_mask] = np.nan
    f2[bp_mask] = np.nan
    g2[bp_mask] = np.nan

# ── graph 1: tax amount ──────────────────────────────
gwase_list = {14: 0.84, 50: 6.24, 88: 15.36, 150: 37.06, 300: 94.06, 500: 174.06, 1000: 384.06}

plt.figure()
for a, val in gwase_list.items():
    plt.vlines(x=a, ymin=0, ymax=val, color='gray', linestyle='--', linewidth=1)
plt.plot(x, f1, label='Progressive Tax Amount (1M KRW)')
plt.plot(x, g1, label='Non-Progressive Tax Amount (1M KRW)')
plt.axhline(0)
plt.legend()
plt.title("Progressive Tax Graph")
plt.show()

# ── graph 2: after-tax income ─────────────────────────
sodeug_list = {14: 13.16, 50: 43.76, 88: 72.64, 150: 112.94, 300: 205.94, 500: 325.94, 1000: 615.94}

plt.figure()
for a, val in sodeug_list.items():
    plt.vlines(x=a, ymin=0, ymax=val, color='gray', linestyle='--', linewidth=1)
plt.plot(x, f2, label='After-Tax Income (Progressive Tax, 1M KRW)')
plt.plot(x, g2, label='After-Tax Income (Non-Progressive Tax, 1M KRW)')
plt.axhline(0)
plt.legend()
plt.title("Progressive Tax Graph")
plt.show()