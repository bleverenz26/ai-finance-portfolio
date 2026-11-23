# Bug Hunt #1 — Compound growth
# Week 2, Day 4
#
# This script has 3 bugs. All three crash the script.
#
# What it should do: grow $10,000 at 7% a year for 10 years, then show
# what that future amount is worth in today's dollars at 3% inflation.
#
# Expected output once fixed:
#   Future value: $19,671.51
#   Real (today's dollars) value: $14,637.45
#
# Tip: fix one error, rerun, read the next one. Bugs hide behind each other.

principal = 10000
annual_rate = 0.07
years = 10
inflation = 0.03

future_value = principal * (1 + annual_rate) ** years
real_value = future_value / (1 + inflation) ** years

print("Future value: " f"${future_value:,.2f}")
print("Real (today's dollars) value: " f"${real_value:,.2f}")
