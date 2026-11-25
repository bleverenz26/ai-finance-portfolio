def npv(rate, cash_flows):
    """Calculates the net present value of a series of cash flows at a specified rate and sums them, year 0 not discounted"""
    total = 0
    for t, cf in enumerate(cash_flows):
        pv = cf/((1+rate)**t)
        total += pv
    return total


def irr(cash_flows, low=0.0, high=1.0, tol=1e-6, max_iter=100):
    """Uses the bisection method to determine IRR with a cap of 100 bisections, and a hard stop without a sign change"""
    npv_low = npv(low, cash_flows)
    npv_high = npv(high, cash_flows)
    if npv_low * npv_high > 0:
        raise ValueError("No sign change between low and high, so no IRR found in this range.")
    
