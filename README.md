# Income Tax Statement & Anticipatory / Final Calculator FY 2026-27 (AY 2027-28)
### With Form 10E (Section 89(1) Arrear Relief) & Single-Page A4 Portrait Statement

A modern, responsive, standalone web application patterned after [ecostatt.com](https://ecostatt.com/income-tax/tax-calculator2026-27/) and the statutory Indian Income Tax guidelines for **Financial Year 2026–27 (Assessment Year 2027–2028)**.

Live Web App: **[https://sureshmagnolia.github.io/IT/](https://sureshmagnolia.github.io/IT/)**

---

## 🌟 Key Features

### 1. Single-Page A4 Portrait Statement (New Regime)
- **Exact Layout Replication:** Replicates the 14-row Ecostatt statement format matching the model PDF `Income Tax 2026-27 Statement-- Suresh V (2).pdf`.
- **Strict A4 Portrait Containment:** Engineered with `@page { size: A4 portrait; margin: 8mm 10mm; }` to fit the complete statement on **exactly 1 page** without any second-page spillovers.
- Contains:
  - Header: Title, AY 2027-28 / FY 2026-27, Anticipatory/Final tag, New Regime (u/s 115BAC) badge.
  - Employee Particulars: Name, Designation, PAN, PEN, Office.
  - Row 1: Gross Salary with 2x6 Monthly Breakdown (March 2026 to February 2027), Surrender, Bonus, Arrears, and Excess Pay.
  - Row 2: Standard Deduction (₹75,000), Conveyance, NPS Employer 80CCD(2), Professional Tax.
  - Row 3: Remuneration (Valuation / Exam / Other Income).
  - Row 4: Total Income (rounded to nearest ₹10).
  - Row 5–10: Tax computation, Rebate u/s 87A (up to ₹60,000 for income &le; ₹12L + marginal relief), Surcharge, 4% Health & Education Cess.
  - Row 11: **Relief for arrears of salary u/s 89(1)** (synced directly from Form 10E).
  - Row 12: Balance Tax Payable (Row 10 - Row 11).
  - Row 13: Income Tax deducted from salary / Advance tax paid (TDS).
  - Row 14: Balance Income Tax to be paid + Anticipatory note showing monthly deduction installment.
  - Dual Signatures Block: Place & Date on left, Employee Signature/Designation/Office on right.

### 2. Form 10E Calculation (Section 89(1) Arrear Relief)
- Patterned after [ecostatt.com Form 10E Calculation](https://ecostatt.com/income-tax/tax-calculator2026-27/form10e-calculation/).
- **Historical Tax Formulas Supported:** FY 2010–11 through FY 2025–26:
  - Supports both **OLD Regime** and **NEW Regime** (from FY 2020-21 onwards).
  - Age categories: Individual, Senior Citizen (60–79), Super Senior (80+).
  - Historical standard deductions, tax slabs, rebate u/s 87A, surcharge tiers, and cess (3% / 4%).
- **Interactive Table A Generator:**
  - Add arrears across multiple previous financial years (e.g., DA arrears, pay revision arrears).
  - Automatically computes tax without arrear, tax with arrear, and tax difference for each year.
- **Annexure I Summary:**
  - Step 1: Current Year (FY 2026-27) Tax with arrears ($A_1$)
  - Step 2: Current Year Tax without arrears ($A_2$)
  - Step 3: Current Year Tax on arrears: $A = A_1 - A_2$
  - Step 4: Previous Years Total Tax on arrears: $B = \sum \text{Diff}$
  - Step 5: **Relief u/s 89(1)**: $\max(0, A - B)$
- **One-Click Application:** Button `⚡ Apply Relief to Statement (Row 11)` automatically injects the calculated relief into Row 11 of the Income Tax Statement and recalculates balance tax and pending monthly deductions.
- **Printable Statutory Form 10E:** Generates the official Form No. 10E with Rule 21AA verification and Table A ready for DDO submission.

### 3. Anticipatory Statement & Monthly TDS Deduction
- Toggle between **ANTICIPATORY STATEMENT** and **FINAL STATEMENT**.
- Specify **Pending Months** (1 to 12).
- Automatically calculates:
  $$\text{Monthly TDS} = \frac{\text{Balance Tax Payable (Row 12)} - \text{TDS Deducted (Row 13)}}{\text{Pending Months}}$$
- Displays note on statement: `(To be deducted @ ₹X / month for Y pending months)`.

### 4. Usability Tools
- **📋 Copy March Gross Down:** Copies March Basic Pay, Allowances, PF, and TDS down to all 12 months in one click.
- **📈 Apply DA Hike %:** Prompt to apply DA percentage hike (e.g. 4%) from any specified month.
- **📄 Load Suresh V Sample:** Instant one-click pre-population matching the model PDF.
- **🧹 Clear All Data:** Resets all fields to blank/zero for a fresh start.
- **⚖️ Old Regime Comparison:** Side-by-side comparison with Chapter VI-A deductions (80C, 80CCD(1B), 80D, 24(b), etc.).

---

## 🖨️ Printing Instructions

1. Click **Print New Regime Statement (Single Page A4)** or press `Ctrl + P`.
2. In the print dialog:
   - **Destination:** Save as PDF or select your printer.
   - **Paper Size:** A4.
   - **Orientation:** Portrait.
   - **Margins:** Default or None (margins are built into the CSS).
   - **Headers and Footers:** Uncheck (to hide URL and timestamp).
   - **Background graphics:** Check (to preserve subtle table shading).
3. The statement will fit on **exactly 1 single page**.

---

## 🚀 Deployment

The site is hosted via GitHub Pages:
- Repository: [https://github.com/sureshmagnolia/IT](https://github.com/sureshmagnolia/IT)
- Live URL: [https://sureshmagnolia.github.io/IT/](https://sureshmagnolia.github.io/IT/)
- Deployment workflow: `.github/workflows/deploy.yml` triggers on every push to `main`.
