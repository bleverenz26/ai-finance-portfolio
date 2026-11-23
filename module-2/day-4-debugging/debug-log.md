## Bug 1.1
- Error: TypeError on line 16
- Cause: "0.07"
- Fix: change 0.07
- How I Found it: sanity check
## Bug 1.2
- Error: TypeError on line 23
- Cause: "Future value: $" + future_value
- Fix: changed to incorporate f-string
- How I Found it: traceback
## Bug 1.3
- Error: NameError on line 23
- Cause: real_valu
- Fix: changed to real_value
- How I Found it: sanity check
## Bug 2.1
- Error: IndentationError on line 27
- Cause: npv not indented after for
- Fix: properly indented
- How I Found it: traceback
## Bug 2.2
- Error: IndexError on line 20
- Cause: for i in range(1, len(cash_flows) + 1):
    total_inflows += cash_flows[i]
- Fix: got rid of +1 after len
- How I Found it: originally I got it wrong and changed [i] to [1] but 1800 didn't match up to the expected 1900 so something else was wrong
## Bug 2.3
- Error: KeyError on line 24
- Cause: Discount_rate
- Fix: changed to discount_rate
- How I Found it: traceback
## Bug 3.1
- Error: TypeError on line 44
- Cause: payment was Nonetype
- Fix: changed payment under the monthly_payment key to pay then added a return pay line
- How I Found it: traceback
## Bug 3.2
- Error: LogicError, code ran fine but gave wrong result
- Cause: monthly payments so annual rate needs to be divided by 12
- Fix: annual_rate / 12
- How I Found it: sanity check
## Bug 3.3
- Error: LogicError, code ran fine but gave wrong result
- Cause: dti does not run strictest test first
- Fix: make if dti > 43 decline the first check
- How I Found it: sanity check
## Bug 4.1
- Error: LogicError, code ran fine but gave wrong result
- Cause: wrong range
- Fix: changed to range(0,n) instead of (1,n)
- How I Found it: sanity check
## Bug 4.2
- Error: LogicError, wrong output (total interest $5,900.00 instead of $3,199.36)
- Cause: interest was calculated on the original `principal` every month
  instead of the remaining `balance`, so it never shrank as the loan was
  paid down ($20,000 × 0.5% = $100 a month, every month)
- Fix: `interest = balance * r`
- How I found it: sanity check
## Bug 4.3
- Error: LogicError, wrong output (ending balance $-2,812.71 instead of $0.00)
- Cause: `balance -= payment` subtracted the whole payment, including the
  interest portion, so the balance fell too fast and went negative. Only
  the principal portion of a payment reduces the loan.
- Fix: `balance -= principal_paid`
- How I found it: sanity check
## Bug 5.1 (appeared twice: downside and upside loops)
- Error: LogicError, wrong output (all three NPVs identical at the base value, $1,089.79)
- Cause: `for cf in downside[1:]: cf = cf * 0.8` only changed the temporary
  loop variable `cf`. It never wrote anything back into the list, so the
  scenarios were never changed.
- Fix: loop over positions instead of values, and assign into the list:
  `for i in range(1, len(downside)): downside[i] = downside[i] * 0.8`
- Wrong turns along the way:
  - `float(base) * 1.2` → TypeError. You can't multiply or convert a whole
    list; work on one item at a time.
  - `downside = base[cf] * 0.8` → TypeError ('float' object is not iterable).
    It replaced the whole list with a single number. The left side of `=`
    has to be `downside[cf]`.
- How I found it: AI hint (ladder step 4), then a small test in the >>> prompt
## Bug 5.2
- Error: LogicError, wrong output (all three NPVs still identical, now at a "mix"
  where every inflow was 0.96x the base, i.e. 0.8 x 1.2)
- Cause: `downside = base` and `upside = base` don't create new lists. They
  give the SAME list extra names. Both loops edited that one list, which
  also silently changed the base case.
- Fix: give each scenario its own copy: `downside = base.copy()`,
  `upside = base.copy()`
- How I found it: AI hint; confirmed by printing `base` after the downside loop
- Lesson: a scenario should never be able to change the base case. Same idea
  as pasting values instead of linking cells when you copy a sheet in Excel.