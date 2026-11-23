# Income Tax Statement & Anticipatory / Final Calculator (FY 2026–27 / AY 2027–28)

A standalone, 100% offline, client-side HTML application for Indian salaried employees and government personnel (matching the structure and conventions of [ecostatt.com](https://ecostatt.com/income-tax/tax-calculator2026-27/)).

---

## 🌟 Newly Added Features

1. **Clean Start & "✕ Clear All Data"**:
   - The form now starts clean with empty fields and default zero balances (it does **not** force sample data on startup).
   - A dedicated **"✕ Clear All Data"** button in the header resets all inputs, allowances, deductions, and schedules with a single click.
   - Sample buttons (**"Kerala Govt Sample"** and **"Central/PSU Sample"**) remain available whenever you want to test.

2. **"↓ Copy Down" on Monthly Gross Income**:
   - Each monthly card (March through January) now features a **"↓ Copy Down"** button.
   - Enter your salary in any month (e.g., March or a pay revision in July) and click **"↓ Copy Down"** to copy that exact amount downward to all subsequent months automatically.
   - Includes a **"Copy March to All 12 Months"** master button and a **"Quick DA Hike"** helper.

3. **Anticipatory Statement vs. Final Statement Modes**:
   - Switch easily between **Anticipatory Statement** and **Final Statement**:
     - **Anticipatory Statement** *(during the year)*:
       - Enter the tax already deducted from salary till date.
       - Choose your pending recovery period (e.g., *October 2026 to February 2027 = 5 Months*).
       - Automatically computes the exact **Monthly TDS Installment** (`Balance Tax / Pending Months`).
       - Formats official titles, text, and Section E schedule for anticipatory submission.
     - **Final Statement** *(at year-end in Jan/Feb)*:
       - Computes final annual tax liability vs total annual TDS deducted.
       - Shows net balance tax to be deducted from February salary or refund due.
       - Optional challan entry (BSR code, challan serial no, date, and amount).
       - Updates declarations and certifications for final year-end closing.

4. **Print Statements for Both Regimes (or Single Regime)**:
   - On the statement view, choose your print layout:
     - 🔘 **Both Regimes (Comparative Dual Statement)**: Prints the full itemized computation for *both* New Tax Regime (u/s 115BAC) and Old Tax Regime, along with the comparative abstract, recommendation, recovery schedule, declaration, and DDO certificate.
     - 🔘 **New Tax Regime Only**: Formatted statement exclusively for Section 115BAC.
     - 🔘 **Old Tax Regime Only**: Formatted statement exclusively for Old Regime with Chapter VI-A deductions.

5. **A4 Print Ready (`@media print`)**:
   - Formatted for clean printing to physical paper or **Save as PDF** via your browser's Print dialog (`Ctrl+P` or the **"Print / Save to PDF"** button).
   - Hides web toolbars, buttons, and responsive controls, rendering crisp black borders and clean page breaks.

---

## 🚀 How to Open and Use

1. Navigate to:
   `C:\Users\sures\.gemini\antigravity\scratch\income-tax-calculator-2026-27\`
2. Double-click [index.html](file:///C:/Users/sures/.gemini/antigravity/scratch/income-tax-calculator-2026-27/index.html) to open in your browser.
3. Choose your **Statement Mode** (*Anticipatory* or *Final*).
4. Enter your March salary and click **"Copy March to All 12 Months"** or click **"↓ Copy Down"** on any month where a revision occurred.
5. Fill in any arrears, HRA details, or Chapter VI-A deductions.
6. Check the live comparison cards to see which regime saves more tax.
7. Click **"2. Official Printable Statement"** to view and print your statement!
