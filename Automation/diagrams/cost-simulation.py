#!/usr/bin/env python3
"""Cost-benefit simulation chart for Automation.md ("Simulating the Budget").

Renders cost-simulation.svg and cost-simulation.png next to this file.
Run: python Automation/diagrams/cost-simulation.py  (needs matplotlib)

Every number here matches the tables in the whitepaper — change them together.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

HERE = Path(__file__).resolve().parent

# ── Assumptions ───────────────────────────────────────────────────────────────
DAY_RATE = 650.0            # € per engineer-day (freelance rate)
HOURLY = DAY_RATE / 8       # € 81.25 per hour
GAIN = 0.70                 # time saved per request (optimistic view) → the automation budget
MAX_REQ = 1000              # requests per year on the x-axis

SCENARIOS = [               # (label, hours per request, colour) — ordinal blue ramp
    ("2 h / request", 2, "#86b6ef"),
    ("4 h / request", 4, "#2a78d6"),
    ("8 h / request", 8, "#104281"),
]
# Unstable team: newcomers + lost tribal knowledge → +25 % time per request,
# plus onboarding of 2 replacements × 15 days a year.
UNSTABLE_HOURS = 4 * 1.25
UNSTABLE_FIXED = 2 * 15 * DAY_RATE      # € 19,500
UNSTABLE_COLOR = "#eb6834"

EXAMPLE_REQ = 500           # the worked example marked on both panels

# ── Chrome (light surface — the whitepaper renders on white) ─────────────────
INK, INK2, MUTED = "#0b0b0b", "#52514e", "#898781"
GRID, AXIS, SURFACE = "#e1e0d9", "#c3c2b7", "#ffffff"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 11,
    "axes.edgecolor": AXIS,
    "axes.labelcolor": INK2,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "svg.fonttype": "none",
})

xs = list(range(0, MAX_REQ + 1, 10))


def manual(hours, fixed=0.0):
    return [n * hours * HOURLY + (fixed if n else 0.0) for n in xs]


def eur_k(v, _pos=None):
    return "€0" if v == 0 else f"€{v / 1000:,.0f}k"


fig, axes = plt.subplots(1, 2, figsize=(12, 5.4), sharey=True, facecolor=SURFACE)
panels = [
    ("Manual handling cost per year", 1.0),
    (f"Automation budget per year ({GAIN:.0%} time gain)", GAIN),
]

for ax, (title, factor) in zip(axes, panels):
    ax.set_facecolor(SURFACE)
    ax.grid(axis="y", color=GRID, linewidth=1)
    ax.set_axisbelow(True)
    ax.set_title(title, loc="left", color=INK, fontsize=12.5, fontweight="bold", pad=12)
    ax.set_xlim(0, MAX_REQ * 1.2)   # room on the right for end labels
    ax.set_ylim(0, 680_000)
    ax.set_xticks(range(0, MAX_REQ + 1, 250))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _p: f"{v:,.0f}"))
    ax.yaxis.set_major_formatter(FuncFormatter(eur_k))
    ax.set_xlabel("Rule requests per year")
    ax.tick_params(length=0)

    for label, hours, color in SCENARIOS:
        ys = [y * factor for y in manual(hours)]
        ax.plot(xs, ys, color=color, linewidth=2, solid_capstyle="round")
        ax.annotate(label, (xs[-1], ys[-1]), xytext=(8, 0), textcoords="offset points",
                    va="center", color=INK2, fontsize=10)

    ys = [y * factor for y in manual(UNSTABLE_HOURS, UNSTABLE_FIXED)]
    ax.plot(xs, ys, color=UNSTABLE_COLOR, linewidth=2, linestyle=(0, (5, 3)))
    ax.annotate("4 h, unstable team", (xs[-1], ys[-1]), xytext=(8, 0),
                textcoords="offset points", va="center", color=INK2, fontsize=10)

    # Worked example: 500 requests at 4 h
    ey = EXAMPLE_REQ * 4 * HOURLY * factor
    ax.plot([EXAMPLE_REQ], [ey], "o", markersize=8, color="#2a78d6",
            markeredgecolor=SURFACE, markeredgewidth=2, zorder=5)
    ax.annotate(f"{EXAMPLE_REQ} requests × 4 h = €{ey:,.0f}", (EXAMPLE_REQ, ey),
                xytext=(560, 38_000 if factor == 1 else 24_000), textcoords="data",
                ha="left", va="center", color=INK, fontsize=10, fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=INK2, linewidth=1,
                                shrinkA=2, shrinkB=5))

axes[0].set_ylabel("€ per year")
fig.text(0.01, 0.005,
         f"Assumptions: €{DAY_RATE:,.0f}/day (€{HOURLY:.2f}/h), 8 h day. Unstable team: +25 % time per "
         f"request and 2 × 15 onboarding days a year (€{UNSTABLE_FIXED:,.0f}).\n"
         f"Budget = {GAIN:.0%} of the time per request (optimistic view); it must cover licence, integration, maintainer time and training.",
         color=MUTED, fontsize=9)
fig.tight_layout(rect=(0, 0.06, 1, 1))

for ext in ("svg", "png"):
    fig.savefig(HERE / f"cost-simulation.{ext}", dpi=192, facecolor=SURFACE)
print("wrote", HERE / "cost-simulation.svg", "and .png")
