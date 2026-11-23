# Income Tax Statement & Anticipatory / Final Calculator FY 2026-27 (AY 2027-28)
### Mobile-Friendly &bull; 1-Click A4 PDF Downloads &bull; Pure Black & White Print Statements &bull; Form 10E Arrear Relief

A modern, responsive, standalone web application patterned after [ecostatt.com](https://ecostatt.com/income-tax/tax-calculator2026-27/) and the statutory Indian Income Tax guidelines for **Financial Year 2026–27 (Assessment Year 2027–2028)**.

Live Web App: **[https://sureshmagnolia.github.io/IT/](https://sureshmagnolia.github.io/IT/)**

---

## 🌟 Key Features

### 1. 📱 Mobile Friendly & Zero Horizontal Scroll
- Engineered with strict viewport containment (`overflow-x: hidden; max-width: 100vw;`).
- **Responsive Salary Table**:
  - On desktop/laptops: Clean 7-column table with monthly inputs and Copy Down buttons.
  - On mobile devices: Automatically transforms into a clean, self-contained **Card per Month** layout with labels and inputs side-by-side, complete with per-month `⬇️ Copy Down` action buttons.
  - Zero awkward horizontal scrolling or awkward table cutoffs.
- Navigation bar, buttons, and summary comparison cards flex and wrap neatly to fit any smartphone screen size.

### 2. 📥 Direct Neat A4 PDF Downloads
- Direct 1-click PDF download buttons on all statement views:
  - **`📥 Download A4 PDF (New Regime Statement)`**
  - **`📥 Download A4 PDF (Old Regime Statement)`**
  - **`📥 Download Form 10E (A4 PDF)`**
- Powered by `html2pdf.js` to render the statements as authentic, high-resolution vector A4 portrait documents (210mm &times; 297mm) directly saved to your device.
- Plus standard **`🖨️ Print Statement`** for direct browser printing.

### 3. 📄 Strict Single-Page A4 Portrait Statement (Pure Black & White)
- **100% Monochrome Print Layout**: Pure black text (`#000000`) on white backgrounds (`#ffffff`), with crisp 1px solid black lines. No gray dithering, no color accents, and no wasted ink.
- **Strict 1-Page Containment**: Fits the entire 14-row Ecostatt statement on **exactly 1 page** (A4 Portrait, 8mm &times; 10mm margins).
- Includes:
  - Header: Title, AY 2027-28 / FY 2026-27, Anticipatory/Final mode badge, New Regime (u/s 115BAC) badge.
  - Employee Particulars: Name, Designation, PAN, PEN, Office.
  - Row 1: Gross Salary with 2x6 Monthly Breakdown (March 2026 to February 2027), Surrender, Bonus, Arrears, and Excess Pay.
  - Row 2: Deductions (Standard Deduction ₹75,000, Conveyance, NPS Employer 80CCD(2), Professional Tax).
  - Row 3: Remuneration (Valuation / Exam / Other Income).
  - Row 4: Total Income (rounded to nearest ₹10).
  - Rows 5–10: Tax computation, Rebate u/s 87A (tax nil up to ₹12 Lakh + marginal relief), Surcharge, 4% Health & Education Cess.
  - Row 11: **Relief for arrears of salary u/s 89(1)** (synced directly from Form 10E).
  - Row 12: Balance Tax Payable (Row 10 - Row 11).
  - Row 13: Income Tax deducted from salary / Advance tax paid (TDS).
  - Row 14: Balance Income Tax to be paid + Anticipatory monthly deduction installment.
  - Dual Signatures Block: Place & Date on left, Employee Signature/Designation/Office on right.

### 4. 📑 Form 10E (Section 89(1) Arrear Relief)
- Patterned after [ecostatt.com Form 10E Calculation](https://ecostatt.com/income-tax/tax-calculator2026-27/form10e-calculation/).
- **Historical Tax Slabs Engine (FY 2010–11 to FY 2025–26)**:
  - Supports both **OLD Regime** and **NEW Regime** (from FY 2020-21 onwards).
  - Age categories: Individual, Senior Citizen (60–79), Super Senior (80+).
- **Interactive Table A**: Add arrears across multiple previous financial years and compute year-by-year tax differences.
- **Annexure I**: Automatic step-by-step relief computation ($A - B$).
- **One-Click Apply**: `⚡ Apply Relief to Statement (Row 11)` injects the calculated relief into Row 11 of the statement.

### 5. ⬇️ Prominent Copy Down Options
- **Main Action Bar**: Blue `⬇️ Copy Down Monthly Gross` button copies March salary to all 12 months.
- **Per-Month Copy Down**: Click `⬇️ Copy Down` on any month (e.g. March, or July after an increment) to copy down to all subsequent months.

---

## 🚀 Deployment

- GitHub Repository: [https://github.com/sureshmagnolia/IT](https://github.com/sureshmagnolia/IT)
- Live Web App: [https://sureshmagnolia.github.io/IT/](https://sureshmagnolia.github.io/IT/)
