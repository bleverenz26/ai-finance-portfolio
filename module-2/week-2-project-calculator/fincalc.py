def npv(rate, cash_flows):
    """Calculates the net present value of a series of cash flows at a specified rate and sums them, year 0 not discounted"""
    total = 0
    for t, cf in enumerate(cash_flows):
        pv = cf/((1+rate)**t)
        total += pv
    return total