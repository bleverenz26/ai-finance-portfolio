///
OBJECTIVE
Trading comps for Google (GOOGL) vs large tech mega-cap peers on LTM multiples, to decide whether GOOGL is trading at a premium and if so, if the premium is large enough to rule out a long position.

UNIVERSE
Target company: GOOGL | Peers: MSFT, META, AMZN, AAPL

AS-OF DATE & PERIODS
- Price: closing price on Fri Nov 13, 2026, the same date for every company. 
- Financials: each company's most recent 10-Q or 10-K filed on or before Nov 13, 2026. Ignore fiscal-year labels (FY26/FY27); identify every period by its period-end date. 
- LTM = latest fiscal year + current YTD − prior-year YTD. If the latest filing is a 10-K, LTM = that fiscal year. Show the build.
- Balance sheet items: from the most recent filing's balance sheet, using the current period-end column (not the prior fiscal year-end comparative column). The balance sheet date must match the LTM period end.

DEFINITIONS 
- Diluted shares: diluted weighted-average shares from the latest quarter's income statement. 
- Market cap = price × diluted shares. 
- EV = market cap + total debt + preferred stock + noncontrolling interests − cash & equivalents − short-term investments. 
	- Total debt = short-term borrowings + current portion of long-term debt + long-term debt + finance lease liabilities. EXCLUDE operating lease liabilities. 
	- Do NOT count long-term investments as cash. 
	- Commercial paper issued is short term debt, commercial paper held counts as a cash equivalent. If commercial paper held is not a separate line item, it is already included in cash and cash equivalents. 
	- If preferred stock or noncontrolling interests have no balance, use 0 and say so.         
- EBITDA (reported) = GAAP operating income + D&A from the cash flow statement. No other add-backs. 
- P/E = price / LTM GAAP diluted EPS. 
- P/B = market cap / shareholders' equity attributable to the company (exclude noncontrolling interests). 
- Any multiple with a negative denominator shows "NM".

SOURCES 
- All financials: SEC EDGAR filings only (not Yahoo, not news articles). 
- Price: Yahoo Finance historical close. If unavailable, use another source and name it. 
- For every input: filing type, period end, line-item name as written in the filing, and link.

OUTPUT 
Spreadsheet (in Excel) with three tabs: 
1. Comps: Company | Ticker | LTM period end | Price | Diluted shares | Market cap | EV | LTM Revenue | LTM EBITDA | EV/Revenue | EV/EBITDA | P/E | P/B. $ in millions; multiples to one decimal (e.g., 12.3x). Peer mean and median rows (excluding GOOGL). GOOGL row highlighted. 
2. Inputs: every raw number, with its source details. 
3. Flags: every assumption made and every issue below. All calculations as live formulas referencing the Inputs tab, not typed-in values.

CHECKS & FLAGS 
- Flag if LTM period ends differ by more than 3 months between companies. 
- Compare your market cap to Yahoo's; flag differences over 5% with the likely reason. 
- Flag one-time items inside operating income (impairments, restructuring, litigation) larger than 5% of operating income. Don't adjust; just flag. 
- Never fill a missing number with an estimate. Leave it blank and flag it.
-Flag any material debt issuance, repayment, or acquisition disclosed in subsequent events or 8-Ks after the balance sheet date. Don't adjust; just flag.

[Comps output](../outputs/GOOGL_comps_2026-11-13.xlsx)
///