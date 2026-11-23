# Bug Hunt #5 — Scenario analysis
# Week 2, Day 4
#
# This script has 2 bugs (one of them shows up twice). Neither crashes.
# They interact: fixing the first one changes the symptom but doesn't
# make the output right.
#
# What it should do: take a base-case set of project cash flows, build a
# downside case where every inflow (years 1-5) is 20% lower and an upside
# case where every inflow is 20% higher, then compare NPVs at 9%.
# The year-0 investment stays the same in every scenario.
#
# Expected output once fixed:
#   Base NPV:     $1,089.79
#   Downside NPV: $-128.17
#   Upside NPV:   $2,307.75
#
# This is the one where you practice asking AI for a HINT, not a fix.
# Use the ladder from today's lesson.


def npv(rate, cash_flows):
    total = 0
    for year, cf in enumerate(cash_flows):
        total += cf / (1 + rate) ** year
    return total


base = [-5000, 1200, 1400, 1600, 1800, 2000]
rate = 0.09
down = base.copy()
up = base.copy()

downside = down
for cf in range(1, len(down)):
    downside[cf] = down[cf] * 0.8

upside = up
for cf in range(1, len(up)):
    upside[cf] = up[cf] * 1.2

print(f"Base NPV:     ${npv(rate, base):,.2f}")
print(f"Downside NPV: ${npv(rate, downside):,.2f}")
print(f"Upside NPV:   ${npv(rate, upside):,.2f}")