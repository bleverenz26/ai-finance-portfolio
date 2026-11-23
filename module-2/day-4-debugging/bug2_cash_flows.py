# Bug Hunt #2 — Cash-flow summary
# Week 2, Day 4
#
# This script has 3 bugs. All three crash the script.
#
# What it should do: total the inflows of a 5-year project (years 1-5),
# then discount every cash flow at 8% to get the project's NPV.
#
# Expected output once fixed:
#   Total inflows (years 1-5): $1,900.00
#   NPV at 8.0%: $486.82
#
# Tip: one of these errors appears before a single line runs. Why?

cash_flows = [-1000, 300, 300, 400, 400, 500]   # index 0 = year 0 (the investment)
assumptions = {"discount_rate": 0.08, "tax_rate": 0.21}

total_inflows = 0
for i in range(1, len(cash_flows)):
    total_inflows += cash_flows[i]

print(f"Total inflows (years 1-5): ${total_inflows:,.2f}")

rate = assumptions["discount_rate"]

npv = 0
for year, cf in enumerate(cash_flows):
    npv += cf / (1 + rate) ** year

print(f"NPV at {rate:.1%}: ${npv:,.2f}")
