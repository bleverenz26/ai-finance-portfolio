# Bug Hunt #4 — Amortization schedule
# Week 2, Day 4
#
# This script has 3 bugs. NONE of them crash. It runs, prints numbers,
# and looks fine at a glance. This is the kind of bug that ends up in a
# model someone sends to a client.
#
# What it should do: amortize a $20,000 car loan at 6% over 5 years,
# paid monthly, and print a summary.
#
# Expected output once fixed:
#   Monthly payment: $386.66
#   Months in schedule: 60
#   Total interest paid: $3,199.36
#   Ending balance: $0.00
#
# (If you see "$-0.00" for the ending balance, that's fine: it's a tiny
#  floating-point leftover like -0.0000000005, not a bug.)
#
# Tip: a loan schedule must end at zero. If it doesn't, print the first
# three months (interest, principal, balance) and check them by hand.

principal = 20000
annual_rate = 0.06
years = 5

r = annual_rate / 12
n = years * 12
payment = principal * r / (1 - (1 + r) ** -n)

balance = principal
total_interest = 0
months = 0

for month in range(0, n):
    interest = balance * r
    principal_paid = payment - interest
    balance -= principal_paid
    total_interest += interest
    months += 1

print(f"Monthly payment: ${payment:,.2f}")
print(f"Months in schedule: {months}")
print(f"Total interest paid: ${total_interest:,.2f}")
print(f"Ending balance: ${balance:,.2f}")
