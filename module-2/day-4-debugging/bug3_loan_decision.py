# Bug Hunt #3 — Mortgage payment and approval check
# Week 2, Day 4
#
# This script has 3 bugs. Only ONE of them crashes.
# The other two run fine and give you a wrong answer.
#
# What it should do: work out the monthly payment on a $250,000,
# 30-year mortgage at 6.5%, then compute the borrower's debt-to-income
# ratio (DTI) and make a lending decision.
#
# The lending rule:
#   DTI above 43%  -> Decline
#   DTI above 36%  -> Review
#   otherwise      -> Approve
#
# Expected output once fixed:
#   Monthly payment: $1,580.17
#   Debt-to-income: 47.6%
#   Decision: Decline
#
# Tip: once it stops crashing, ask yourself whether each number is
# believable before you check it against the expected output.


def monthly_payment(principal, annual_rate, years):
    r = annual_rate / 12
    n = years * 12
    pay = principal * r / (1 - (1 + r) ** -n)
    return pay


def loan_decision(dti):
    if dti > 0.43:
        return "Decline"
    elif dti > 0.36:
        return "Review"
    else:
        return "Approve"


payment = monthly_payment(250000, 0.065, 30)
other_debts = 800        # car loan + student loan, per month
monthly_income = 5000    # gross, per month

dti = (payment + other_debts) / monthly_income

print(f"Monthly payment: ${payment:,.2f}")
print(f"Debt-to-income: {dti:.1%}")
print(f"Decision: {loan_decision(dti)}")
