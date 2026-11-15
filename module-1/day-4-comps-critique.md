///
Critiques/observations
	- P/E distorted by large gains on equity investments, something to exclude later
	- EV/Revenue is distorted by AMZN, no fault of the AI, due to Amazon's high volume low margin e-commerce
	- Should probably exclude finance leases in future. Include if all have them, otherwise exclude. 
	- AMZN D&A inflated by amortization of operating lease assets, something to exclude later
	- GOOGL amortization not included with depreciation, most years so small it is immaterial, so ok
	- GOOGL SpaceX investment counted as marketable security so increases cash, subtract only cash and cash-like securities (ex: held commercial paper) from EV, and list equity stakes separately as non-operating investments
	- GOOGL mandatory convertible preferred stock runs on an "if-converted method", agent in the future should always check for manual convertible preferred stock, if diluted share count already counts the as converted shares, don't add preferred stock to EV. If the conversion was excluded as anti-dilutive, add it as preferred. Either way, flag for review
	
What to add
A new exclusion section would help fix distortions in P/E, D&A, and debt. A new check would help make issues with mandatory preferred stock easier to diagnose. Having the ability of a dropdown inside each valuation comp cell (EV/Revenue for AMZN for example) to manually exclude would avoid distorting mean multiples when it makes sense and is justifiable. Accuracy was not an issue, manually verified all revenue, operating income, D&A, and equity inputs for Google.

[Comps prompt](prompts/day-4-comps-prompt.md)
[Comps output](outputs/GOOGL_comps_2026-11-13.xlsx)
///