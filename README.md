# Income Tax Statement & Anticipatory / Final Calculator FY 2026-27 (AY 2027-28)
### Mobile-Friendly &bull; 1-Click A4 PDF Downloads &bull; Pure Black & White Print Statements &bull; Form 10E Arrear Relief &bull; JSON Save/Import/Export

A modern, responsive, standalone web application patterned after [ecostatt.com](https://ecostatt.com/income-tax/tax-calculator2026-27/) and the statutory Indian Income Tax guidelines for **Financial Year 2026–27 (Assessment Year 2027–2028)**.

Live Web App: **[https://sureshmagnolia.github.io/IT/](https://sureshmagnolia.github.io/IT/)**

---

## 🌟 Key Features

### 1. 💾 Save, Restore, Export & Import JSON Data
- **`💾 Save Draft`**: Saves all entered employee details, monthly gross salaries, deductions, and Form 10E Table A rows directly into your browser's `localStorage`.
- **`📂 Load Draft`**: Instantly restores your previously saved draft at any time.
- **`📥 Export JSON`**: Downloads a standalone, human-readable JSON backup file (`<name>_income_tax_2026_27.json`) to your computer.
- **`📤 Import JSON`**: Upload any previously exported JSON file to restore the complete calculation state across different computers or browsers.

### 2. 📄 Clean Ecostatt Gross Salary Layout & Zero PDF Clipping
- **Authentic 2-Column Monthly Layout**:
  - Replicates Ecostatt's official design with two neat columns (March–August on the left, September–February on the right) with aligned colons and figures.
  - Subtotal (a), Leave Surrender/Arrears (b), Excess Pay (c), and Total Salary (a+b-c) lined up cleanly with zero messy overlapping boxes.
- **Strict A4 Containment with Zero Clipping**:
  - Engineered with a fixed 184mm width budget and 8mm margins in `html2pdf.js` and CSS print media.
  - Eliminates the previous right-edge clipping bug so that all amounts and signature blocks fit completely on paper without losing digits.

### 3. 📱 Mobile Friendly & Zero Horizontal Scroll
- Strict viewport containment (`overflow-x: hidden; max-width: 100vw;`).
- **Responsive Salary Table**:
  - On desktop/laptops: Clean 7-column table with monthly inputs and Copy Down buttons.
  - On mobile devices ($\le 768\text{px}$): Automatically transforms into a clean **Card per Month** layout with side-by-side labels and per-month `⬇️ Copy Down` action buttons.
  - Zero awkward horizontal scrolling or table cutoffs.

### 4. 📥 Direct Neat A4 PDF Downloads
- Direct 1-click PDF download buttons on all statement views:
  - **`📥 Download A4 PDF (New Regime Statement)`**
  - **`📥 Download A4 PDF (Old Regime Statement)`**
  - **`📥 Download Form 10E (A4 PDF)`**
- Powered by `html2pdf.js` to render authentic, vector-crisp A4 portrait documents (210mm &times; 297mm) directly saved to your device.
- Plus standard **`🖨️ Print Statement`** for direct browser printing.

### 5. 📑 Form 10E (Section 89(1) Arrear Relief)
- Patterned after [ecostatt.com Form 10E Calculation](https://ecostatt.com/income-tax/tax-calculator2026-27/form10e-calculation/).
- **Historical Tax Slabs Engine (FY 2010–11 to FY 2025–26)**:
  - Supports both **OLD Regime** and **NEW Regime** (from FY 2020-21 onwards).
  - Age categories: Individual, Senior Citizen (60–79), Super Senior (80+).
- **Interactive Table A**: Add arrears across multiple previous financial years and compute year-by-year tax differences.
- **Annexure I**: Automatic step-by-step relief computation ($A - B$).
- **One-Click Apply**: `⚡ Apply Relief to Statement (Row 11)` injects the calculated relief into Row 11 of the statement.

---

## 🚀 Deployment

- GitHub Repository: [https://github.com/sureshmagnolia/IT](https://github.com/sureshmagnolia/IT)
- Live Web App: [https://sureshmagnolia.github.io/IT/](https://sureshmagnolia.github.io/IT/)
