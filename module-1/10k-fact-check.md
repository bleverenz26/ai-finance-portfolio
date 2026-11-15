# Summarizing a 10-K with AI: Does Prompting Still Matter?

## Goal
I tested a weak vs strong prompt for 10k summarization then checked the outputs for accuracy. The ultimate goal is to have a strong stated prompt agents use to perform this task consistently and effectively.

## Setup
- Filing: Amazon 10-K, FY2025
- Model: Claude Opus (high effort)
- Date: Nov 14, 2026

## Prompts
**Weak prompt:**
```
Summarize this 10-K.
```
**Strong prompt:** see [prompts/10k-screen.md](prompts/10k-screen.md)

## Results: weak vs. strong
Similar
- Accuracy
- Segment analysis
- Revenue and profitability breakdown
Different
- Strong had greater detail in every aspect
- Strong stated where information came from, when calculated, when non-GAAP
- Strong had the unlevered free cash flow build
- Strong had better defined company specific risks
- Strong had a more complete management outlook
- Strong had a quality of earning breakdown which included a depreciation schedule shift
- Strong model noticed a problem with its own source, not being able to Ctrl + F
[Strong](outputs/amzn-strong-summary.md)
[Weak](outputs/amzn-weak-summary.md)

## Takeaways
- The weak prompt output contained much of the essential information
- Prompting does still matter. Consistency, greater quality of information, accountability are all things to call out here
- A strong prompt only has to be developed once

## Ideas for later
- Build this prompt into an agent as a system prompt (Week 4)
- Pull filings from the EDGAR API; get the numbers from XBRL with code and use the LLM for text
- Create compatability with Excel for model building