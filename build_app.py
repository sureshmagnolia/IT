import os

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Income Tax Statement & Anticipatory / Final Calculator FY 2026-27 (AY 2027-28)</title>
  <style>
    :root {
      --primary: #1e3a8a;
      --primary-light: #2563eb;
      --primary-dark: #172554;
      --secondary: #0d9488;
      --accent: #f59e0b;
      --danger: #dc2626;
      --success: #16a34a;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #1e293b;
      --text-muted: #64748b;
      --border: #cbd5e1;
      --border-focus: #3b82f6;
      --radius: 8px;
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding-bottom: 95px;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 16px;
    }

    /* App Header */
    .app-header {
      background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 100%);
      color: white;
      padding: 18px 20px;
      border-radius: var(--radius);
      margin-bottom: 18px;
      box-shadow: var(--shadow);
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }

    .app-header-title h1 {
      font-size: 1.5rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .app-header-title p {
      color: #cbd5e1;
      font-size: 0.86rem;
      margin-top: 3px;
    }

    .header-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 7px 12px;
      font-size: 0.82rem;
      font-weight: 600;
      border-radius: 6px;
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s ease;
      text-decoration: none;
    }

    .btn-sm {
      padding: 4px 8px;
      font-size: 0.75rem;
    }

    .btn-primary {
      background-color: var(--primary-light);
      color: white;
    }
    .btn-primary:hover {
      background-color: var(--primary);
    }

    .btn-success {
      background-color: var(--success);
      color: white;
    }
    .btn-success:hover {
      background-color: #15803d;
    }

    .btn-outline {
      background-color: transparent;
      border-color: rgba(255, 255, 255, 0.45);
      color: white;
    }
    .btn-outline:hover {
      background-color: rgba(255, 255, 255, 0.15);
      border-color: white;
    }

    .btn-outline-dark {
      background-color: white;
      border-color: var(--border);
      color: var(--text);
    }
    .btn-outline-dark:hover {
      background-color: #f1f5f9;
      border-color: #94a3b8;
    }

    .btn-danger {
      background-color: #fee2e2;
      color: var(--danger);
      border-color: #fca5a5;
    }
    .btn-danger:hover {
      background-color: #fecaca;
    }

    .btn-copy-down {
      background-color: #e0f2fe;
      color: #0369a1;
      border: 1px solid #bae6fd;
      border-radius: 4px;
      padding: 3px 6px;
      font-size: 0.68rem;
      font-weight: 600;
      cursor: pointer;
      margin-top: 4px;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      transition: background 0.15s ease;
    }
    .btn-copy-down:hover {
      background-color: #bae6fd;
      color: #0284c7;
    }

    /* View Switcher */
    .view-switcher {
      display: flex;
      background-color: #e2e8f0;
      border-radius: 8px;
      padding: 4px;
      margin-bottom: 18px;
    }

    .view-tab {
      flex: 1;
      text-align: center;
      padding: 9px 14px;
      font-weight: 600;
      font-size: 0.92rem;
      border-radius: 6px;
      cursor: pointer;
      border: none;
      background: transparent;
      color: var(--text-muted);
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }

    .view-tab.active {
      background-color: white;
      color: var(--primary);
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    /* Cards */
    .card {
      background-color: var(--card-bg);
      border-radius: var(--radius);
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      margin-bottom: 18px;
      overflow: hidden;
    }

    .card-header {
      background-color: #f8fafc;
      padding: 11px 16px;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
    }

    .card-header h2 {
      font-size: 1rem;
      font-weight: 600;
      color: var(--primary-dark);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .card-body {
      padding: 16px;
    }

    /* Grids */
    .grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; }
    .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
    .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
    .grid-6 { display: grid; grid-template-columns: repeat(6, 1fr); gap: 9px; }

    @media (max-width: 900px) {
      .grid-4, .grid-6 { grid-template-columns: repeat(2, 1fr); }
      .grid-3 { grid-template-columns: 1fr; }
    }
    @media (max-width: 600px) {
      .grid-2, .grid-4, .grid-6 { grid-template-columns: 1fr; }
    }

    /* Form Elements */
    .form-group {
      margin-bottom: 10px;
    }

    .form-group label {
      display: block;
      font-size: 0.78rem;
      font-weight: 600;
      color: #334155;
      margin-bottom: 3px;
    }

    .form-group .label-desc {
      font-size: 0.7rem;
      font-weight: normal;
      color: var(--text-muted);
    }

    .form-control {
      width: 100%;
      padding: 7px 9px;
      font-size: 0.85rem;
      border: 1px solid var(--border);
      border-radius: 6px;
      background-color: white;
      color: var(--text);
      transition: border-color 0.15s ease, box-shadow 0.15s ease;
    }

    .form-control:focus {
      outline: none;
      border-color: var(--border-focus);
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
    }

    .form-control.number-input {
      text-align: right;
      font-variant-numeric: tabular-nums;
      font-family: inherit;
    }

    .radio-group {
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      padding: 4px 0;
    }

    .radio-label {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.83rem;
      cursor: pointer;
    }

    /* Statement Type Switcher Banner */
    .statement-type-box {
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      border-radius: 8px;
      padding: 10px 14px;
      margin-bottom: 16px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }

    /* Salary Month Card */
    .salary-month-card {
      background-color: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px;
      position: relative;
    }

    .month-header {
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 4px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .month-badge {
      font-size: 0.65rem;
      background: #e2e8f0;
      color: #475569;
      padding: 1px 4px;
      border-radius: 3px;
    }

    /* Quick DA Hike Tool */
    .quick-tools-bar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
      background: #f1f5f9;
      padding: 7px 12px;
      border-radius: 6px;
      margin-bottom: 12px;
      font-size: 0.8rem;
    }

    /* Sticky Bottom Floating Bar */
    .sticky-bar {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: #ffffff;
      border-top: 2px solid var(--primary);
      box-shadow: 0 -4px 15px rgba(0, 0, 0, 0.12);
      padding: 9px 20px;
      z-index: 1000;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }

    .stat-pill {
      display: flex;
      flex-direction: column;
    }

    .stat-pill .stat-label {
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      font-weight: 600;
    }

    .stat-pill .stat-value {
      font-size: 1rem;
      font-weight: 700;
      color: var(--text);
      font-variant-numeric: tabular-nums;
    }

    .stat-pill.highlight-new .stat-value {
      color: #0369a1;
    }
    .stat-pill.highlight-old .stat-value {
      color: #b45309;
    }

    .recommendation-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 11px;
      border-radius: 20px;
      font-weight: 700;
      font-size: 0.8rem;
    }

    .recommendation-badge.new-win {
      background-color: #dcfce7;
      color: #166534;
      border: 1px solid #86efac;
    }

    .recommendation-badge.old-win {
      background-color: #fef3c7;
      color: #92400e;
      border: 1px solid #fde68a;
    }

    .recommendation-badge.equal {
      background-color: #e2e8f0;
      color: #334155;
    }

    /* Regime Comparison Cards */
    .comparison-container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-bottom: 18px;
    }

    @media (max-width: 768px) {
      .comparison-container { grid-template-columns: 1fr; }
    }

    .regime-box {
      border: 2px solid var(--border);
      border-radius: var(--radius);
      padding: 14px;
      background: white;
      cursor: pointer;
      position: relative;
      transition: all 0.2s ease;
    }

    .regime-box:hover {
      border-color: #93c5fd;
    }

    .regime-box.selected {
      border-color: var(--primary-light);
      box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2);
    }

    .regime-box.winner {
      border-color: var(--success);
      background: #f0fdf4;
    }

    .regime-title {
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 6px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .tag-badge {
      font-size: 0.7rem;
      padding: 2px 7px;
      border-radius: 12px;
      font-weight: 600;
    }
    .tag-default { background: #e0f2fe; color: #0369a1; }
    .tag-optional { background: #f1f5f9; color: #475569; }

    /* Section 80C Progress Bar */
    .cap-progress {
      width: 100%;
      height: 9px;
      background-color: #e2e8f0;
      border-radius: 5px;
      overflow: hidden;
      margin: 6px 0;
    }

    .cap-bar {
      height: 100%;
      background-color: var(--primary-light);
      transition: width 0.3s ease;
    }

    .cap-bar.overflow { background-color: var(--success); }

    /* ======================================================= */
    /* PRINT VIEW STYLES & OFFICIAL SINGLE-PAGE A4 FORMAT      */
    /* ======================================================= */
    #print-statement-view {
      display: none;
      background: white;
      padding: 24px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 40px;
    }

    .statement-controls-bar {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      background: #f8fafc;
      padding: 10px 14px;
      border-radius: 6px;
      border: 1px solid var(--border);
      margin-bottom: 20px;
    }

    /* Common Statement Styles */
    .official-header {
      text-align: center;
      border-bottom: 2px double #000;
      padding-bottom: 8px;
      margin-bottom: 10px;
    }

    .official-header h2 {
      font-size: 1.15rem;
      text-transform: uppercase;
      font-weight: 800;
      color: #000;
      letter-spacing: 0.03em;
      line-height: 1.25;
    }

    .official-header h3 {
      font-size: 0.95rem;
      font-weight: 700;
      margin-top: 2px;
      color: #111;
    }

    .official-header p {
      font-size: 0.8rem;
      color: #333;
      margin-top: 2px;
    }

    .statement-meta-table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 10px;
      font-size: 0.82rem;
    }

    .statement-meta-table td {
      padding: 3.5px 6px;
      border: 1px solid #475569;
    }

    .statement-meta-table td.meta-key {
      font-weight: 600;
      background-color: #f8fafc;
      width: 25%;
    }

    .statement-meta-table td.meta-val {
      width: 25%;
    }

    .statement-section-title {
      font-size: 0.86rem;
      font-weight: 700;
      text-transform: uppercase;
      background-color: #f1f5f9;
      padding: 4px 8px;
      border: 1px solid #475569;
      border-bottom: none;
      margin-top: 8px;
      color: #000;
    }

    .statement-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.8rem;
      margin-bottom: 8px;
    }

    .statement-table th, .statement-table td {
      border: 1px solid #475569;
      padding: 3.5px 6px;
    }

    .statement-table th {
      background-color: #f1f5f9;
      font-weight: 700;
      text-align: center;
      color: #000;
    }

    .statement-table tr.total-row {
      font-weight: 700;
      background-color: #f8fafc;
    }

    .statement-table td.amt {
      text-align: right;
      font-variant-numeric: tabular-nums;
    }

    /* Side-by-Side 2-Column Section for Single-Page Layout */
    .side-by-side-grid {
      display: flex;
      gap: 10px;
      margin-bottom: 8px;
    }

    .side-by-side-grid > .col-left {
      flex: 1;
      min-width: 0;
    }

    .side-by-side-grid > .col-right {
      flex: 1;
      min-width: 0;
    }

    /* Side-by-Side Bottom Signatures */
    .bottom-signatures-grid {
      display: flex;
      gap: 10px;
      margin-top: 8px;
    }

    .sig-box-left, .sig-box-right {
      flex: 1;
      border: 1px solid #475569;
      border-radius: 4px;
      padding: 8px 10px;
      font-size: 0.8rem;
      background-color: #fafafa;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .sig-box-left h4, .sig-box-right h4 {
      font-size: 0.82rem;
      text-transform: uppercase;
      border-bottom: 1px solid #94a3b8;
      padding-bottom: 3px;
      margin-bottom: 6px;
      color: #000;
    }

    .signature-line-compact {
      border-top: 1px solid #000;
      margin-top: 28px;
      padding-top: 3px;
      text-align: center;
      font-weight: 700;
    }

    /* PRINT MEDIA RULES - STRICT A4 PORTRAIT SINGLE PAGE */
    @page {
      size: A4 portrait;
      margin: 6mm 8mm 6mm 8mm;
    }

    @media print {
      html, body {
        width: 210mm !important;
        height: 297mm !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #fff !important;
        color: #000 !important;
        font-size: 7.8pt !important;
        line-height: 1.2 !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }

      .app-header, .view-switcher, .header-actions, .sticky-bar, #calculator-form-view, .no-print {
        display: none !important;
      }

      .container {
        max-width: 100% !important;
        width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
      }

      #print-statement-view {
        display: block !important;
        padding: 0 !important;
        margin: 0 !important;
        box-shadow: none !important;
        border: none !important;
        background: transparent !important;
      }

      /* Single Page A4 Lock */
      .a4-single-page {
        page-break-inside: avoid !important;
        page-break-after: avoid !important;
        max-height: 283mm !important;
        overflow: hidden !important;
      }

      .page-break-before {
        page-break-before: always !important;
      }

      .official-header {
        margin-bottom: 5px !important;
        padding-bottom: 3px !important;
      }

      .official-header h2 {
        font-size: 9.8pt !important;
        letter-spacing: 0.02em !important;
      }

      .official-header h3 {
        font-size: 8.8pt !important;
      }

      .official-header p {
        font-size: 7.2pt !important;
      }

      .statement-meta-table {
        margin-bottom: 5px !important;
        font-size: 7.2pt !important;
      }

      .statement-meta-table td {
        padding: 2px 4px !important;
        border-color: #000 !important;
      }

      .statement-section-title {
        font-size: 7.5pt !important;
        padding: 2.5px 5px !important;
        margin-top: 3px !important;
        background-color: #f0f0f0 !important;
        border-color: #000 !important;
        color: #000 !important;
      }

      .statement-table {
        margin-bottom: 4px !important;
        font-size: 7.2pt !important;
      }

      .statement-table th, .statement-table td {
        padding: 2px 4px !important;
        border-color: #000 !important;
      }

      .statement-table th, .statement-meta-table td.meta-key {
        background-color: #f0f0f0 !important;
        color: #000 !important;
      }

      .side-by-side-grid {
        display: flex !important;
        flex-direction: row !important;
        gap: 8px !important;
        margin-bottom: 4px !important;
      }

      .bottom-signatures-grid {
        display: flex !important;
        flex-direction: row !important;
        gap: 8px !important;
        margin-top: 4px !important;
      }

      .sig-box-left, .sig-box-right {
        border-color: #000 !important;
        padding: 4px 6px !important;
        font-size: 7pt !important;
        background-color: #fff !important;
      }

      .signature-line-compact {
        margin-top: 22px !important;
        font-size: 7pt !important;
      }
    }
  </style>
</head>
<body>

<div class="container">
  <!-- Main Application Header -->
  <header class="app-header">
    <div class="app-header-title">
      <h1>
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="2" y="3" width="20" height="18" rx="2"/><line x1="8" y1="7" x2="16" y2="7"/><line x1="8" y1="11" x2="16" y2="11"/><line x1="8" y1="15" x2="10" y2="15"/><line x1="14" y1="15" x2="16" y2="15"/>
        </svg>
        Income Tax Statement Generator (FY 2026–27)
      </h1>
      <p>Anticipatory & Final Statement Calculator (Assessment Year 2027–28) | Single Page A4 Form 16</p>
    </div>

    <div class="header-actions">
      <button type="button" class="btn btn-outline" id="btn-fill-kerala" title="Load sample salary structure for Kerala State Govt employee">
        Kerala Govt Sample
      </button>
      <button type="button" class="btn btn-outline" id="btn-fill-corporate" title="Load sample salary structure for Central / Corporate employee">
        Central/PSU Sample
      </button>
      <button type="button" class="btn btn-danger" id="btn-clear-all" title="Clear all sample data and start completely fresh">
        ✕ Clear All Data
      </button>
      <button type="button" class="btn btn-outline" id="btn-save-draft" title="Save current entries to browser storage">
        Save Draft
      </button>
      <button type="button" class="btn btn-outline" id="btn-load-draft" title="Restore saved entries">
        Restore
      </button>
      <button type="button" class="btn btn-outline" id="btn-export-json" title="Download backup of your inputs">
        Export JSON
      </button>
      <label class="btn btn-outline" style="margin-bottom:0; cursor:pointer;" title="Load backup from file">
        Import JSON
        <input type="file" id="btn-import-file" accept=".json" style="display:none;">
      </label>
    </div>
  </header>

  <!-- View Switcher -->
  <nav class="view-switcher no-print">
    <button type="button" class="view-tab active" id="tab-calculator">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
      1. Calculator & Data Entry
    </button>
    <button type="button" class="view-tab" id="tab-statement">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
      2. Official Printable Statement (A4 Portrait)
    </button>
  </nav>

  <!-- ========================================== -->
  <!-- TAB 1: CALCULATOR & DATA ENTRY VIEW        -->
  <!-- ========================================== -->
  <div id="calculator-form-view">
    
    <!-- STATEMENT TYPE SELECTION BANNER -->
    <div class="statement-type-box">
      <div>
        <span style="font-weight: 700; font-size: 0.92rem; color: #1e3a8a;">Choose Statement Mode:</span>
        <div class="radio-group" style="display: inline-flex; margin-left: 12px;">
          <label class="radio-label">
            <input type="radio" name="statement-type" value="anticipatory" checked>
            <strong>Anticipatory Statement</strong> (During Year - With Pending Installments)
          </label>
          <label class="radio-label">
            <input type="radio" name="statement-type" value="final">
            <strong>Final Statement</strong> (Year-End Assessment in Feb)
          </label>
        </div>
      </div>
      <div>
        <span style="font-size: 0.78rem; color: #475569;">
          Sets the official title, installment recovery schedule, and declarations.
        </span>
      </div>
    </div>

    <!-- REGIME COMPARISON SUMMARY CARDS -->
    <div class="comparison-container">
      <!-- New Regime Card -->
      <div class="regime-box" id="regime-box-new" title="Click to select New Regime">
        <div class="regime-title">
          <span>New Tax Regime (Section 115BAC)</span>
          <span class="tag-badge tag-default">Default Regime</span>
        </div>
        <p style="font-size: 0.78rem; color: var(--text-muted); margin-bottom: 8px;">
          Standard Deduction ₹75,000 | Tax rebate up to ₹12,00,000 (Tax Free up to ₹12,75,000 Gross)
        </p>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
          <span style="font-size: 0.82rem; font-weight: 600;">Net Taxable Income:</span>
          <span style="font-size: 0.95rem; font-weight: 700;" id="sum-taxable-new">₹0</span>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
          <span style="font-size: 0.82rem; font-weight: 600;">Total Tax Payable (incl Cess):</span>
          <span style="font-size: 1.2rem; font-weight: 800; color: #0369a1;" id="sum-tax-new">₹0</span>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; font-size: 0.82rem;">
          <span style="color: var(--text-muted);" id="sum-balance-label-new">Balance Tax to Deduct:</span>
          <span style="font-weight: 700;" id="sum-balance-new">₹0</span>
        </div>
      </div>

      <!-- Old Regime Card -->
      <div class="regime-box" id="regime-box-old" title="Click to select Old Regime">
        <div class="regime-title">
          <span>Old Tax Regime</span>
          <span class="tag-badge tag-optional">With Deductions</span>
        </div>
        <p style="font-size: 0.78rem; color: var(--text-muted); margin-bottom: 8px;">
          Standard Deduction ₹50,000 | HRA, 80C (up to 1.5L), 80D, Housing Loan Interest (2L)
        </p>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
          <span style="font-size: 0.82rem; font-weight: 600;">Net Taxable Income:</span>
          <span style="font-size: 0.95rem; font-weight: 700;" id="sum-taxable-old">₹0</span>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
          <span style="font-size: 0.82rem; font-weight: 600;">Total Tax Payable (incl Cess):</span>
          <span style="font-size: 1.2rem; font-weight: 800; color: #b45309;" id="sum-tax-old">₹0</span>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: baseline; font-size: 0.82rem;">
          <span style="color: var(--text-muted);" id="sum-balance-label-old">Balance Tax to Deduct:</span>
          <span style="font-weight: 700;" id="sum-balance-old">₹0</span>
        </div>
      </div>
    </div>

    <!-- 1. BASIC DETAILS CARD -->
    <div class="card">
      <div class="card-header">
        <h2>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          1. Basic Details of Employee
        </h2>
        <span style="font-size: 0.78rem; color: var(--text-muted);">Required for official statement</span>
      </div>
      <div class="card-body">
        <div class="grid-3">
          <div class="form-group">
            <label for="emp-name">Employee Name</label>
            <input type="text" id="emp-name" class="form-control" placeholder="e.g. Suresh Kumar K">
          </div>
          <div class="form-group">
            <label for="emp-designation">Designation</label>
            <input type="text" id="emp-designation" class="form-control" placeholder="e.g. Senior Superintendent">
          </div>
          <div class="form-group">
            <label for="emp-pan">PAN Number</label>
            <input type="text" id="emp-pan" class="form-control" placeholder="e.g. ABCDE1234F" style="text-transform: uppercase;">
          </div>
        </div>

        <div class="grid-3">
          <div class="form-group">
            <label for="emp-office">Office / Department / Institution</label>
            <input type="text" id="emp-office" class="form-control" placeholder="e.g. Directorate of Economics & Statistics">
          </div>
          <div class="form-group">
            <label for="emp-pen">PEN / PRAN / PF Number</label>
            <input type="text" id="emp-pen" class="form-control" placeholder="e.g. 542198">
          </div>
          <div class="form-group">
            <label for="emp-ddo">DDO Code / Station</label>
            <input type="text" id="emp-ddo" class="form-control" placeholder="e.g. 0101-01 / Thiruvananthapuram">
          </div>
        </div>

        <div class="grid-2" style="margin-top: 4px; padding-top: 10px; border-top: 1px dashed var(--border);">
          <div class="form-group">
            <label>Taxpayer Category (Age Category)</label>
            <div class="radio-group">
              <label class="radio-label">
                <input type="radio" name="taxpayer-category" value="general" checked> Individual (&lt; 60 yrs)
              </label>
              <label class="radio-label">
                <input type="radio" name="taxpayer-category" value="senior"> Senior Citizen (60 – 79 yrs)
              </label>
              <label class="radio-label">
                <input type="radio" name="taxpayer-category" value="supersenior"> Super Senior (80+ yrs)
              </label>
            </div>
          </div>

          <div class="form-group">
            <label>Selected Tax Regime for Official Statement</label>
            <div class="radio-group">
              <label class="radio-label">
                <input type="radio" name="chosen-regime" value="new" checked>
                <strong>NEW Regime</strong> (Default / Section 115BAC)
              </label>
              <label class="radio-label">
                <input type="radio" name="chosen-regime" value="old">
                <strong>OLD Regime</strong> (With HRA & 80C deductions)
              </label>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 2. MONTHLY SALARY TABLE (MARCH 2026 TO FEBRUARY 2027) -->
    <div class="card">
      <div class="card-header">
        <h2>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
          2. Monthly Gross Salary / Pension (March 2026 – February 2027)
        </h2>
        <div style="display: flex; gap: 8px;">
          <button type="button" class="btn btn-outline-dark btn-sm" id="btn-copy-march" title="Copy March salary value to all 12 months">
            Copy March to All 12 Months
          </button>
        </div>
      </div>
      <div class="card-body">
        
        <!-- Quick DA Hike helper bar -->
        <div class="quick-tools-bar">
          <span style="font-weight: 600; color: #334155;">Quick DA Hike Helper:</span>
          <span>Add</span>
          <input type="number" id="quick-da-amount" class="form-control" style="width: 80px; padding: 4px 7px; font-size: 0.78rem;" placeholder="e.g. 3000">
          <span>₹ from month</span>
          <select id="quick-da-start-month" class="form-control" style="width: 135px; padding: 4px 7px; font-size: 0.78rem;">
            <option value="4">July 2026 (M5)</option>
            <option value="6">Sept 2026 (M7)</option>
            <option value="7">Oct 2026 (M8)</option>
            <option value="9">Dec 2026 (M10)</option>
            <option value="10">Jan 2027 (M11)</option>
          </select>
          <button type="button" class="btn btn-primary btn-sm" id="btn-apply-da-hike">
            Apply Hike Downwards
          </button>
          <span style="color: var(--text-muted); font-size: 0.74rem; margin-left: auto;">
            Tip: Click <strong>"↓ Copy Down"</strong> on any month to copy its value downward!
          </span>
        </div>

        <p style="font-size: 0.78rem; color: var(--text-muted); margin-bottom: 10px;">
          Enter the Gross Salary drawn for each month (SPARK starts with March salary drawn in April).
        </p>

        <div class="grid-6" id="salary-months-grid">
          <!-- 12 Months Cards -->
          <div class="salary-month-card">
            <div class="month-header"><span>March 2026</span><span class="month-badge">M1</span></div>
            <input type="number" id="m-0" class="form-control number-input month-salary" placeholder="0" min="0">
            <button type="button" class="btn-copy-down" onclick="window.copyDownFrom(0)">↓ Copy Down</button>
          </div>
          <div class="salary-month-card">
            <div class="month-header"><span>April 2026</span><span class="month-badge">M2</span></div>
            <input type="number" id="m-1" class="form-control number-input month-salary" placeholder="0" min="0">
            <button type="button" class="btn-copy-down" onclick="window.copyDownFrom(1)">↓ Copy Down</button>
          </div>
          <div class="salary-month-card">
            <div class="month-header"><span>May 2026</span><span class="month-badge">M3</span></div>
            <input type="number" id="m-2" class="form-control number-input month-salary" placeholder="0" min="0">
            <button type="button" class="btn-copy-down" onclick="window.copyDownFrom(2)">↓ Copy Down</button>
          </div>
          <div class="salary-month-card">
            <div class="month-header"><span>June 2026</span><span class="month-badge">M4</span></div>
            <input type="number" id="m-3" class="form-control number-input month-salary" placeholder="0" min="0">
            <button type="button" class="btn-copy-down" onclick="window.copyDownFrom(3)">↓ Copy Down</button>
          </div>
          <div class="salary-month-card">
            <div class="month-header"><span>July 2026</span><span class="month-badge">M5</span></div>
            <input type="number" id="m-4" class="form-control number-input month-salary" placeholder="0" min="0">
            <button type="button" class="btn-copy-down" onclick="window.copyDownFrom(4)">↓ Copy Down</button>
          </div>
          <div class="salary-month-card">
            <div class="month-header"><span>August 2026</span><span class="month-badge">M6</span></div>
            <input type="number" id="m-5" class="form-control number-input month-salary" placeholder="0" min="0">
            <button type="button" class="btn-copy-down" onclick="window.copyDownFrom(5)">↓ Copy Down</button>
          </div>
          <div class="salary-month-card">
            <div class="month-header"><span>Sept 2026</span><span class="month-badge">M7</span></div>
            <input type="number" id="m-6" class="form-control number-input month-salary" placeholder="0" min="0">
            <button type="button" class="btn-copy-down" onclick="window.copyDownFrom(6)">↓ Copy Down</button>
          </div>
          <div class="salary-month-card">
            <div class="month-header"><span>Oct 2026</span><span class="month-badge">M8</span></div>
            <input type="number" id="m-7" class="form-control number-input month-salary" placeholder="0" min="0">
            <button type="button" class="btn-copy-down" onclick="window.copyDownFrom(7)">↓ Copy Down</button>
          </div>
          <div class="salary-month-card">
            <div class="month-header"><span>Nov 2026</span><span class="month-badge">M9</span></div>
            <input type="number" id="m-8" class="form-control number-input month-salary" placeholder="0" min="0">
            <button type="button" class="btn-copy-down" onclick="window.copyDownFrom(8)">↓ Copy Down</button>
          </div>
          <div class="salary-month-card">
            <div class="month-header"><span>Dec 2026</span><span class="month-badge">M10</span></div>
            <input type="number" id="m-9" class="form-control number-input month-salary" placeholder="0" min="0">
            <button type="button" class="btn-copy-down" onclick="window.copyDownFrom(9)">↓ Copy Down</button>
          </div>
          <div class="salary-month-card">
            <div class="month-header"><span>Jan 2027</span><span class="month-badge">M11</span></div>
            <input type="number" id="m-10" class="form-control number-input month-salary" placeholder="0" min="0">
            <button type="button" class="btn-copy-down" onclick="window.copyDownFrom(10)">↓ Copy Down</button>
          </div>
          <div class="salary-month-card">
            <div class="month-header"><span>Feb 2027</span><span class="month-badge">M12</span></div>
            <input type="number" id="m-11" class="form-control number-input month-salary" placeholder="0" min="0">
            <div style="font-size:0.68rem; color: var(--text-muted); text-align:center; padding-top:5px;">Last Month</div>
          </div>
        </div>

        <div style="margin-top: 12px; padding: 8px 12px; background: #f1f5f9; border-radius: 6px; display: flex; justify-content: space-between; align-items: center;">
          <span style="font-weight: 600; font-size: 0.86rem;">Total 12 Months Salary:</span>
          <span style="font-size: 1.1rem; font-weight: 700; color: var(--primary);" id="total-monthly-salary">₹0</span>
        </div>
      </div>
    </div>

    <!-- 3. ARREARS, ALLOWANCES & OTHER INCOMES -->
    <div class="card">
      <div class="card-header">
        <h2>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><line x1="12" y1="18" x2="12" y2="20"/><line x1="12" y1="4" x2="12" y2="6"/></svg>
          3. Arrears, Allowances & Other Incomes
        </h2>
      </div>
      <div class="card-body">
        <div class="grid-4">
          <div class="form-group">
            <label for="da-arrear">DA Arrears</label>
            <input type="number" id="da-arrear" class="form-control number-input inc-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="pr-arrear">Pay Revision (PR) Arrears</label>
            <input type="number" id="pr-arrear" class="form-control number-input inc-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="other-arrear">Any Other Arrears</label>
            <input type="number" id="other-arrear" class="form-control number-input inc-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="leave-surrender">Earned Leave Surrender</label>
            <input type="number" id="leave-surrender" class="form-control number-input inc-input" placeholder="0">
          </div>
        </div>

        <div class="grid-4">
          <div class="form-group">
            <label for="bonus">Festival Allowance / Bonus / Ex-gratia</label>
            <input type="number" id="bonus" class="form-control number-input inc-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="excess-pay" style="color: var(--danger);">Excess Pay Drawn, Dies non, etc. (-)</label>
            <input type="number" id="excess-pay" class="form-control number-input inc-input" placeholder="0" title="Will be deducted from Gross Salary">
          </div>
          <div class="form-group">
            <label for="other-salary-inc">Other Salary Income</label>
            <input type="text" id="other-salary-label" class="form-control" placeholder="Description (e.g. Special Duty)" style="font-size: 0.74rem; margin-bottom: 3px;">
            <input type="number" id="other-salary-inc" class="form-control number-input inc-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="any-other-inc">Any Other Income (Interest/Exam)</label>
            <input type="text" id="any-other-label" class="form-control" placeholder="Description (e.g. Bank Interest)" style="font-size: 0.74rem; margin-bottom: 3px;">
            <input type="number" id="any-other-inc" class="form-control number-input inc-input" placeholder="0">
          </div>
        </div>

        <div style="margin-top: 8px; padding: 8px 12px; background: #e0f2fe; border-radius: 6px; display: flex; justify-content: space-between; align-items: center;">
          <span style="font-weight: 700; color: #0369a1;">Total Gross Income (Salary + Arrears + Other):</span>
          <span style="font-size: 1.15rem; font-weight: 800; color: #0369a1;" id="total-gross-income">₹0</span>
        </div>
      </div>
    </div>

    <!-- 4. HRA EXEMPTION (SECTION 10(13A)) - OLD REGIME -->
    <div class="card">
      <div class="card-header">
        <h2>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
          4. House Rent Allowance (HRA) Exemption u/s 10(13A) (Old Regime Only)
        </h2>
      </div>
      <div class="card-body">
        <p style="font-size: 0.78rem; color: var(--text-muted); margin-bottom: 10px;">
          Applicable if paying rent. Least of: (1) Actual HRA, (2) Rent paid - 10% of salary, (3) 40%/50% of salary.
        </p>

        <div class="grid-4">
          <div class="form-group">
            <label for="hra-rent-paid">Total Rent Paid for Year</label>
            <input type="number" id="hra-rent-paid" class="form-control number-input hra-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="hra-actual-received">Actual HRA Received</label>
            <input type="number" id="hra-actual-received" class="form-control number-input hra-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="hra-basic-da">Total Basic Pay + DA</label>
            <input type="number" id="hra-basic-da" class="form-control number-input hra-input" placeholder="0">
          </div>
          <div class="form-group">
            <label>City Category</label>
            <select id="hra-city-metro" class="form-control hra-input">
              <option value="0">Non-Metro (40% of Basic+DA)</option>
              <option value="1">Metro (50% of Basic+DA)</option>
            </select>
          </div>
        </div>

        <div style="margin-top: 8px; padding: 8px 12px; background: #fef3c7; border-radius: 6px; display: flex; justify-content: space-between; align-items: center;">
          <span style="font-weight: 700; color: #92400e;">Calculated HRA Exemption:</span>
          <span style="font-size: 1.1rem; font-weight: 800; color: #92400e;" id="total-hra-exemption">₹0</span>
        </div>
      </div>
    </div>

    <!-- 5. GENERAL DEDUCTIONS (SECTION 16 & CHAPTER VI-A OTHER THAN 80C) -->
    <div class="card">
      <div class="card-header">
        <h2>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          5. General Deductions (Section 16, 24(b), 80D, 80CCD, 80E, etc.)
        </h2>
      </div>
      <div class="card-body">
        <div class="grid-3">
          <div class="form-group">
            <label>Standard Deduction u/s 16(ia)</label>
            <div style="font-size: 0.82rem; padding: 7px 9px; background: #f1f5f9; border-radius: 6px; font-weight: 600;">
              Auto: ₹75,000 (New) | ₹50,000 (Old)
            </div>
          </div>
          <div class="form-group">
            <label for="prof-tax">Professional Tax Paid u/s 16(iii)</label>
            <input type="number" id="prof-tax" class="form-control number-input ded-input" placeholder="0" max="2500">
            <span class="label-desc">Max ₹2,500/year (Old Regime only)</span>
          </div>
          <div class="form-group">
            <label for="housing-loan-int">Housing Loan Interest u/s 24(b)</label>
            <input type="number" id="housing-loan-int" class="form-control number-input ded-input" placeholder="0" max="200000">
            <span class="label-desc">Max ₹2,00,000 (Old Regime)</span>
          </div>
        </div>

        <div class="grid-3">
          <div class="form-group">
            <label for="sec-80eea">Additional Home Loan Interest u/s 80EEA</label>
            <input type="number" id="sec-80eea" class="form-control number-input ded-input" placeholder="0" max="150000">
          </div>
          <div class="form-group">
            <label for="sec-80d-self">Mediclaim (Self/Family) u/s 80D</label>
            <input type="number" id="sec-80d-self" class="form-control number-input ded-input" placeholder="0" max="50000">
          </div>
          <div class="form-group">
            <label for="sec-80d-parents">Mediclaim (Parents) u/s 80D</label>
            <input type="number" id="sec-80d-parents" class="form-control number-input ded-input" placeholder="0" max="50000">
          </div>
        </div>

        <div class="grid-3">
          <div class="form-group">
            <label for="sec-80ccd1b">NPS Additional Contribution u/s 80CCD(1B)</label>
            <input type="number" id="sec-80ccd1b" class="form-control number-input ded-input" placeholder="0" max="50000">
            <span class="label-desc">Max ₹50,000 (over & above 80C)</span>
          </div>
          <div class="form-group">
            <label for="sec-80ccd2">NPS Employer Contribution u/s 80CCD(2)</label>
            <input type="number" id="sec-80ccd2" class="form-control number-input ded-input" placeholder="0">
            <span class="label-desc">Allowed in BOTH New & Old Regimes</span>
          </div>
          <div class="form-group">
            <label for="sec-80e">Education Loan Interest u/s 80E</label>
            <input type="number" id="sec-80e" class="form-control number-input ded-input" placeholder="0">
          </div>
        </div>

        <div class="grid-4">
          <div class="form-group">
            <label for="sec-80g">Donations u/s 80G</label>
            <input type="number" id="sec-80g" class="form-control number-input ded-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="sec-80eeb">EV Loan Interest u/s 80EEB</label>
            <input type="number" id="sec-80eeb" class="form-control number-input ded-input" placeholder="0" max="150000">
          </div>
          <div class="form-group">
            <label for="sec-80tta">SB Interest u/s 80TTA / 80TTB</label>
            <input type="number" id="sec-80tta" class="form-control number-input ded-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="sec-80u-dd">Disability / Medical u/s 80U/DD</label>
            <input type="number" id="sec-80u-dd" class="form-control number-input ded-input" placeholder="0">
          </div>
        </div>
      </div>
    </div>

    <!-- 6. DEDUCTIONS UNDER SECTION 80C, 80CCC, 80CCD(1) (MAX: RS. 1.5 LAKH) -->
    <div class="card">
      <div class="card-header">
        <h2>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.21 15.89A10 10 0 1 1 8 2.83"/><path d="M22 12A10 10 0 0 0 12 2v10z"/></svg>
          6. Deductions under Section 80C (Maximum Limit: ₹1,50,000 - Old Regime)
        </h2>
        <span style="font-size: 0.82rem; font-weight: 700;" id="label-80c-status">Total: ₹0 / ₹1,50,000</span>
      </div>
      <div class="card-body">
        <div class="cap-progress">
          <div class="cap-bar" id="bar-80c" style="width: 0%;"></div>
        </div>

        <div class="grid-4">
          <div class="form-group">
            <label for="c-gpf">General Provident Fund (GPF)</label>
            <input type="number" id="c-gpf" class="form-control number-input c80-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="c-sli">SLI, GIS, FBS, GPAIS</label>
            <input type="number" id="c-sli" class="form-control number-input c80-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="c-lic">Life Insurance Premium (LIC)</label>
            <input type="number" id="c-lic" class="form-control number-input c80-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="c-ppf">Public Provident Fund (PPF)</label>
            <input type="number" id="c-ppf" class="form-control number-input c80-input" placeholder="0">
          </div>
        </div>

        <div class="grid-4">
          <div class="form-group">
            <label for="c-hba-principal">Housing Loan Principal</label>
            <input type="number" id="c-hba-principal" class="form-control number-input c80-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="c-tuition">Tuition Fees (max 2 children)</label>
            <input type="number" id="c-tuition" class="form-control number-input c80-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="c-bank-fd">5-Yr Tax Saver Bank FD</label>
            <input type="number" id="c-bank-fd" class="form-control number-input c80-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="c-elss">ELSS Mutual Funds</label>
            <input type="number" id="c-elss" class="form-control number-input c80-input" placeholder="0">
          </div>
        </div>

        <div class="grid-4">
          <div class="form-group">
            <label for="c-nsc">NSC VIII Issue</label>
            <input type="number" id="c-nsc" class="form-control number-input c80-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="c-post-office">5-Yr Post Office TD</label>
            <input type="number" id="c-post-office" class="form-control number-input c80-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="c-nps-emp">NPS Employee (80CCD1)</label>
            <input type="number" id="c-nps-emp" class="form-control number-input c80-input" placeholder="0">
          </div>
          <div class="form-group">
            <label for="c-other">Sukanya Samriddhi / Other</label>
            <input type="number" id="c-other" class="form-control number-input c80-input" placeholder="0">
          </div>
        </div>

        <div style="margin-top: 8px; padding: 8px 12px; background: #f8fafc; border: 1px solid var(--border); border-radius: 6px; display: flex; justify-content: space-between; align-items: center;">
          <span><strong>Total 80C Claimed:</strong> <span id="val-80c-gross">₹0</span></span>
          <span style="font-weight: 700; color: var(--primary);">Eligible 80C (Capped at ₹1.5L): <span id="val-80c-eligible">₹0</span></span>
        </div>
      </div>
    </div>

    <!-- 7. TAX DEDUCTED AT SOURCE (TDS) & ANTICIPATORY/FINAL SETTLEMENT -->
    <div class="card">
      <div class="card-header">
        <h2>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          7. Tax Deducted at Source (TDS) & Settlement Installments
        </h2>
      </div>
      <div class="card-body">
        <div class="grid-3">
          <div class="form-group">
            <label for="tds-paid"><span id="tds-input-label">Tax Already Deducted from Salary Till Date</span></label>
            <input type="number" id="tds-paid" class="form-control number-input" placeholder="0">
            <span class="label-desc" id="tds-input-desc">Total TDS deducted from monthly salary drawn so far</span>
          </div>

          <div class="form-group" id="group-pending-months">
            <label for="pending-from-month">Pending Recovery Period</label>
            <select id="pending-from-month" class="form-control">
              <option value="0">March 2026 to February 2027 (12 Months)</option>
              <option value="4">July 2026 to February 2027 (8 Months)</option>
              <option value="6">Sept 2026 to February 2027 (6 Months)</option>
              <option value="7" selected>October 2026 to February 2027 (5 Months)</option>
              <option value="8">November 2026 to February 2027 (4 Months)</option>
              <option value="9">December 2026 to February 2027 (3 Months)</option>
              <option value="10">January 2027 to February 2027 (2 Months)</option>
              <option value="11">February 2027 (1 Month Final)</option>
            </select>
            <span class="label-desc">Balance tax is divided across these pending months</span>
          </div>

          <div class="form-group" id="group-installment-display">
            <label>Suggested Monthly TDS Installment</label>
            <div style="font-size: 1.15rem; font-weight: 700; color: var(--primary); padding: 7px 10px; background: #eff6ff; border-radius: 6px; border: 1px solid #bfdbfe;" id="val-monthly-installment">
              ₹0 / month
            </div>
            <span class="label-desc" id="desc-monthly-installment">for remaining pending months</span>
          </div>
        </div>

        <div id="final-statement-extra-fields" style="display: none; margin-top: 8px; padding-top: 10px; border-top: 1px dashed var(--border);">
          <div class="grid-3">
            <div class="form-group">
              <label for="final-challan-bsr">Challan BSR Code (if paid separately)</label>
              <input type="text" id="final-challan-bsr" class="form-control" placeholder="e.g. 0510324">
            </div>
            <div class="form-group">
              <label for="final-challan-no">Challan Serial No. & Date</label>
              <input type="text" id="final-challan-no" class="form-control" placeholder="e.g. 00142 dt 15/02/2027">
            </div>
            <div class="form-group">
              <label for="final-challan-amt">Challan Amount Paid (₹)</label>
              <input type="number" id="final-challan-amt" class="form-control number-input" placeholder="0">
            </div>
          </div>
        </div>

      </div>
    </div>

  </div> <!-- END CALCULATOR VIEW -->

  <!-- ======================================================= -->
  <!-- TAB 2: OFFICIAL PRINTABLE STATEMENT VIEW                -->
  <!-- ======================================================= -->
  <div id="print-statement-view">
    
    <!-- Print Controls Toolbar (Screen Only) -->
    <div class="statement-controls-bar no-print">
      <div style="display: flex; align-items: center; gap: 14px; flex-wrap: wrap;">
        <span style="font-weight: 700; color: #1e3a8a; font-size: 0.88rem;">Print Layout Option:</span>
        <div class="radio-group" style="padding: 0;">
          <label class="radio-label">
            <input type="radio" name="print-regime-choice" value="new" checked>
            <strong>New Regime Only (Single A4 Page)</strong>
          </label>
          <label class="radio-label">
            <input type="radio" name="print-regime-choice" value="old">
            Old Regime
          </label>
          <label class="radio-label">
            <input type="radio" name="print-regime-choice" value="both">
            Both Regimes (Comparative)
          </label>
        </div>
      </div>

      <div style="display: flex; gap: 10px;">
        <button type="button" class="btn btn-primary" onclick="window.print()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
          Print / Save to PDF
        </button>
        <button type="button" class="btn btn-outline-dark" id="btn-back-to-form">
          Back to Edit Form
        </button>
      </div>
    </div>

    <!-- ===================================================== -->
    <!-- VIEW A: NEW REGIME STATEMENT (FITS ON SINGLE A4 PAGE) -->
    <!-- ===================================================== -->
    <div id="wrapper-section-new-regime" class="a4-single-page">
      
      <!-- Official Header -->
      <div class="official-header">
        <h2 id="new-stmt-main-title">ANTICIPATORY STATEMENT OF INCOME TAX ASSESSMENT FOR FY 2026–2027</h2>
        <h3>ASSESSMENT YEAR 2027–2028 | NEW TAX REGIME (u/s 115BAC)</h3>
        <p id="new-stmt-sub-title">(Statement under Section 192 of the Income Tax Act, 1961 for Salaried Employees & Pensioners)</p>
      </div>

      <!-- Part A: Employee Particulars (2 compact rows) -->
      <div class="statement-section-title">A. Particulars of Employee & Office</div>
      <table class="statement-meta-table">
        <tr>
          <td class="meta-key">1. Name of Employee</td>
          <td class="meta-val" id="new-meta-name" style="font-weight: 700;">-</td>
          <td class="meta-key">2. Designation</td>
          <td class="meta-val" id="new-meta-designation">-</td>
        </tr>
        <tr>
          <td class="meta-key">3. PAN Number</td>
          <td class="meta-val" id="new-meta-pan" style="font-weight: 700;">-</td>
          <td class="meta-key">4. PEN / PRAN / PF No.</td>
          <td class="meta-val" id="new-meta-pen">-</td>
        </tr>
        <tr>
          <td class="meta-key">5. Office / Department</td>
          <td class="meta-val" id="new-meta-office">-</td>
          <td class="meta-key">6. DDO Code & Station</td>
          <td class="meta-val" id="new-meta-ddo">-</td>
        </tr>
        <tr>
          <td class="meta-key">7. Category (Age)</td>
          <td class="meta-val" id="new-meta-category">Individual (&lt; 60 yrs)</td>
          <td class="meta-key">8. Tax Regime Opted</td>
          <td class="meta-val" style="font-weight: 700; color: #1e3a8a;">NEW REGIME (u/s 115BAC)</td>
        </tr>
      </table>

      <!-- Side-by-Side 2-Column Core: Left = Monthly Salary + Arrears; Right = Tax Computation + Recovery -->
      <div class="side-by-side-grid">
        
        <!-- LEFT COLUMN: Monthly Salary Table & Arrears -->
        <div class="col-left">
          <div class="statement-section-title">B. Monthly Salary Drawn (Mar 2026 – Feb 2027)</div>
          <table class="statement-table">
            <thead>
              <tr>
                <th style="width: 12%;">M#</th>
                <th style="width: 58%;">Month & Year</th>
                <th style="width: 30%;">Gross Pay (₹)</th>
              </tr>
            </thead>
            <tbody>
              <tr><td class="text-center">1</td><td>March 2026 (drawn in Apr)</td><td class="amt" id="new-stmt-m0">0</td></tr>
              <tr><td class="text-center">2</td><td>April 2026</td><td class="amt" id="new-stmt-m1">0</td></tr>
              <tr><td class="text-center">3</td><td>May 2026</td><td class="amt" id="new-stmt-m2">0</td></tr>
              <tr><td class="text-center">4</td><td>June 2026</td><td class="amt" id="new-stmt-m3">0</td></tr>
              <tr><td class="text-center">5</td><td>July 2026</td><td class="amt" id="new-stmt-m4">0</td></tr>
              <tr><td class="text-center">6</td><td>August 2026</td><td class="amt" id="new-stmt-m5">0</td></tr>
              <tr><td class="text-center">7</td><td>September 2026</td><td class="amt" id="new-stmt-m6">0</td></tr>
              <tr><td class="text-center">8</td><td>October 2026</td><td class="amt" id="new-stmt-m7">0</td></tr>
              <tr><td class="text-center">9</td><td>November 2026</td><td class="amt" id="new-stmt-m8">0</td></tr>
              <tr><td class="text-center">10</td><td>December 2026</td><td class="amt" id="new-stmt-m9">0</td></tr>
              <tr><td class="text-center">11</td><td>January 2027</td><td class="amt" id="new-stmt-m10">0</td></tr>
              <tr><td class="text-center">12</td><td>February 2027</td><td class="amt" id="new-stmt-m11">0</td></tr>
              <tr class="total-row">
                <td colspan="2" style="font-weight: 700; text-align: right;">Total 12 Months Salary:</td>
                <td class="amt" id="new-stmt-total-12m" style="font-weight: 700;">0</td>
              </tr>
            </tbody>
          </table>

          <!-- Arrears & Other Additions sub-table -->
          <div class="statement-section-title" style="margin-top: 4px;">Arrears & Other Salary Additions</div>
          <table class="statement-table">
            <tbody>
              <tr>
                <td style="width: 70%;">DA Arrears / Pay Revision Arrears</td>
                <td class="amt" style="width: 30%;" id="new-stmt-arr-dapr">0</td>
              </tr>
              <tr>
                <td>Earned Leave Surrender</td>
                <td class="amt" id="new-stmt-arr-surrender">0</td>
              </tr>
              <tr>
                <td>Festival Allowance / Bonus / Ex-gratia</td>
                <td class="amt" id="new-stmt-arr-bonus">0</td>
              </tr>
              <tr>
                <td>Other Salary / Other Incomes (Interest, etc.)</td>
                <td class="amt" id="new-stmt-arr-other">0</td>
              </tr>
              <tr>
                <td>Less: Excess Pay Drawn / Dies non refunded (-)</td>
                <td class="amt" id="new-stmt-arr-excess">0</td>
              </tr>
              <tr class="total-row" style="background-color: #e0f2fe;">
                <td style="font-weight: 700; color: #0369a1;">TOTAL GROSS INCOME (Salary + Arrears)</td>
                <td class="amt" id="new-stmt-gross-total" style="font-weight: 800; color: #0369a1;">0</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- RIGHT COLUMN: Tax Computation & Recovery Schedule -->
        <div class="col-right">
          <div class="statement-section-title">C. Income & Tax Computation (New Regime)</div>
          <table class="statement-table">
            <tbody>
              <tr>
                <td style="width: 70%;">1. Gross Salary Income</td>
                <td class="amt" style="width: 30%; font-weight: 600;" id="new-stmt-c-gross">0</td>
              </tr>
              <tr>
                <td>2. Less: Standard Deduction u/s 16(ia)</td>
                <td class="amt">75,000</td>
              </tr>
              <tr>
                <td>3. Less: Employer NPS Contribution u/s 80CCD(2)</td>
                <td class="amt" id="new-stmt-c-80ccd2">0</td>
              </tr>
              <tr class="total-row" style="background-color: #f1f5f9;">
                <td><strong>4. NET TAXABLE INCOME (Rounded to ₹10)</strong></td>
                <td class="amt" id="new-stmt-c-taxable" style="font-weight: 800;">0</td>
              </tr>
              <tr>
                <td>5. Tax on Taxable Income as per New Slabs</td>
                <td class="amt" id="new-stmt-c-slabtax">0</td>
              </tr>
              <tr>
                <td>6. Less: Tax Rebate under Section 87A (Max ₹60,000)</td>
                <td class="amt" id="new-stmt-c-rebate" style="color: #15803d;">0</td>
              </tr>
              <tr>
                <td>7. Less: Marginal Relief u/s 87A (if applicable)</td>
                <td class="amt" id="new-stmt-c-marginal">0</td>
              </tr>
              <tr>
                <td>8. Tax after Section 87A Rebate</td>
                <td class="amt" id="new-stmt-c-tax-after-rebate">0</td>
              </tr>
              <tr>
                <td>9. Add: Health and Education Cess @ 4%</td>
                <td class="amt" id="new-stmt-c-cess">0</td>
              </tr>
              <tr class="total-row" style="background-color: #eff6ff;">
                <td style="font-weight: 800; color: #1e3a8a;">10. TOTAL ANNUAL TAX PAYABLE</td>
                <td class="amt" id="new-stmt-c-totaltax" style="font-weight: 800; color: #1e3a8a;">0</td>
              </tr>
            </tbody>
          </table>

          <!-- TDS & Recovery Schedule -->
          <div class="statement-section-title" style="margin-top: 4px;" id="new-sched-title">D. Tax Recovery & Installment Schedule</div>
          <table class="statement-table">
            <tbody>
              <tr>
                <td style="width: 70%;">1. Total Annual Tax Liability:</td>
                <td class="amt" style="width: 30%; font-weight: 700;" id="new-sched-tax">0</td>
              </tr>
              <tr>
                <td>2. Less: Tax Deducted at Source (TDS) Till Date:</td>
                <td class="amt" style="font-weight: 700;" id="new-sched-tds">0</td>
              </tr>
              <tr class="total-row" style="background-color: #fef2f2;">
                <td style="font-weight: 700; color: #b91c1c;" id="new-sched-bal-label">3. Balance Tax to be Deducted / Recovered:</td>
                <td class="amt" id="new-sched-bal" style="font-weight: 800; color: #b91c1c;">0</td>
              </tr>
              <tr id="new-row-installment">
                <td style="font-weight: 700; color: #1e3a8a;">
                  4. Monthly TDS Installment for Pending Period:
                  <div style="font-size: 0.68rem; font-weight: normal; color: #555;" id="new-sched-pending-desc">
                    (Pending: October 2026 to February 2027 = 5 Months)
                  </div>
                </td>
                <td class="amt" style="font-size: 0.95rem; font-weight: 800; color: #1e3a8a;" id="new-sched-monthly">
                  0
                </td>
              </tr>
            </tbody>
          </table>
        </div>

      </div>

      <!-- Side-by-Side Bottom Sign-off: Left = Declaration; Right = DDO Certificate -->
      <div class="bottom-signatures-grid">
        <div class="sig-box-left">
          <h4>EMPLOYEE DECLARATION</h4>
          <p id="new-decl-text" style="line-height: 1.35; margin-bottom: 6px;">
            I, <strong id="new-decl-name">_________________</strong>, <span id="new-decl-desig">_________________</span>, hereby declare that the particulars of my salary, allowances, and deductions under the New Tax Regime for FY 2026-27 are true, correct, and complete to the best of my knowledge and belief.
          </p>
          <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-top: auto;">
            <div>
              <p>Place: <span id="new-decl-place">_________________</span></p>
              <p style="margin-top: 3px;">Date: <span id="new-decl-date">_________________</span></p>
            </div>
            <div style="text-align: center; width: 140px;">
              <div class="signature-line-compact">Signature of Employee</div>
            </div>
          </div>
        </div>

        <div class="sig-box-right">
          <h4>VERIFICATION BY DRAWING & DISBURSING OFFICER (DDO)</h4>
          <p style="line-height: 1.35; margin-bottom: 6px;">
            Certified that the salary figures and allowances stated above have been verified with official treasury schedules/SPARK records of this office and appropriate TDS is scheduled for recovery as per Section 192 of the Income Tax Act, 1961.
          </p>
          <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-top: auto;">
            <div>
              <p>Station: <span id="new-ddo-station">_________________</span></p>
              <p style="margin-top: 3px;">Date: <span id="new-ddo-date">_________________</span></p>
              <p style="margin-top: 3px; font-size: 0.68rem; color: #555;">[Office Seal / Treasury Stamp]</p>
            </div>
            <div style="text-align: center; width: 140px;">
              <div class="signature-line-compact">Signature of DDO</div>
            </div>
          </div>
        </div>
      </div>

    </div> <!-- END VIEW A: NEW REGIME SINGLE-PAGE -->


    <!-- ===================================================== -->
    <!-- VIEW B: OLD REGIME STATEMENT                          -->
    <!-- ===================================================== -->
    <div id="wrapper-section-old-regime">
      <div class="official-header">
        <h2 id="old-stmt-main-title">STATEMENT OF INCOME TAX ASSESSMENT FOR FY 2026–2027</h2>
        <h3>ASSESSMENT YEAR 2027–2028 | OLD TAX REGIME (WITH DEDUCTIONS)</h3>
        <p>(Statement under Section 192 of the Income Tax Act, 1961 for Salaried Employees / Pensioners)</p>
      </div>

      <div class="statement-section-title">A. Particulars of Employee & Office</div>
      <table class="statement-meta-table">
        <tr>
          <td class="meta-key">1. Name of Employee</td>
          <td class="meta-val" id="stmt-name">-</td>
          <td class="meta-key">2. Designation</td>
          <td class="meta-val" id="stmt-designation">-</td>
        </tr>
        <tr>
          <td class="meta-key">3. PAN Number</td>
          <td class="meta-val" id="stmt-pan">-</td>
          <td class="meta-key">4. PEN / PRAN / PF No.</td>
          <td class="meta-val" id="stmt-pen">-</td>
        </tr>
        <tr>
          <td class="meta-key">5. Office / Department</td>
          <td class="meta-val" id="stmt-office">-</td>
          <td class="meta-key">6. DDO Code / Station</td>
          <td class="meta-val" id="stmt-ddo">-</td>
        </tr>
        <tr>
          <td class="meta-key">7. Category (Age)</td>
          <td class="meta-val" id="stmt-category">Individual (&lt; 60 yrs)</td>
          <td class="meta-key">8. Tax Regime Opted</td>
          <td class="meta-val" style="font-weight: 700; color: #b45309;">OLD REGIME (With Deductions)</td>
        </tr>
      </table>

      <!-- Section B: Monthly Statement -->
      <div class="statement-section-title">B. Monthly Statement of Gross Salary / Pension Drawn</div>
      <table class="statement-table">
        <thead>
          <tr>
            <th>Sl No</th>
            <th>Month & Year</th>
            <th>Gross Amount (₹)</th>
            <th>Sl No</th>
            <th>Month & Year</th>
            <th>Gross Amount (₹)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="text-center">1</td><td>March 2026</td><td class="amt" id="stmt-m0">0</td>
            <td class="text-center">7</td><td>September 2026</td><td class="amt" id="stmt-m6">0</td>
          </tr>
          <tr>
            <td class="text-center">2</td><td>April 2026</td><td class="amt" id="stmt-m1">0</td>
            <td class="text-center">8</td><td>October 2026</td><td class="amt" id="stmt-m7">0</td>
          </tr>
          <tr>
            <td class="text-center">3</td><td>May 2026</td><td class="amt" id="stmt-m2">0</td>
            <td class="text-center">9</td><td>November 2026</td><td class="amt" id="stmt-m8">0</td>
          </tr>
          <tr>
            <td class="text-center">4</td><td>June 2026</td><td class="amt" id="stmt-m3">0</td>
            <td class="text-center">10</td><td>December 2026</td><td class="amt" id="stmt-m9">0</td>
          </tr>
          <tr>
            <td class="text-center">5</td><td>July 2026</td><td class="amt" id="stmt-m4">0</td>
            <td class="text-center">11</td><td>January 2027</td><td class="amt" id="stmt-m10">0</td>
          </tr>
          <tr>
            <td class="text-center">6</td><td>August 2026</td><td class="amt" id="stmt-m5">0</td>
            <td class="text-center">12</td><td>February 2027</td><td class="amt" id="stmt-m11">0</td>
          </tr>
          <tr class="total-row">
            <td colspan="2" style="font-weight: 700; text-align: right;">Total 12 Months Salary Drawn:</td>
            <td class="amt" id="stmt-total-12m" style="font-weight: 700;">0</td>
            <td colspan="2" style="font-weight: 700; text-align: right;">Arrears & Other Additions:</td>
            <td class="amt" id="stmt-total-arrears" style="font-weight: 700;">0</td>
          </tr>
        </tbody>
      </table>

      <!-- Section C: Old Regime Computation -->
      <div class="statement-section-title">C. Tax Computation under OLD TAX REGIME (With All Deductions)</div>
      <table class="statement-table">
        <tbody>
          <tr><td style="width: 70%;">1. Gross Salary (12 Months Salary + Arrears + Bonus + Surrender)</td><td class="amt" style="width: 30%;" id="stmt-old-gross">0</td></tr>
          <tr><td>2. Less: Excess Pay Drawn / Dies non refunded</td><td class="amt" id="stmt-old-excess">0</td></tr>
          <tr><td>3. Less: HRA Exemption u/s 10(13A)</td><td class="amt" id="stmt-old-hra">0</td></tr>
          <tr><td>4. Less: Standard Deduction u/s 16(ia) <em>(₹50,000 for Old Regime)</em></td><td class="amt">50,000</td></tr>
          <tr><td>5. Less: Professional Tax Paid u/s 16(iii)</td><td class="amt" id="stmt-old-pt">0</td></tr>
          <tr class="total-row"><td><strong>6. Income Chargeable under the Head 'Salaries'</strong></td><td class="amt" id="stmt-old-inc-salary" style="font-weight: 600;">0</td></tr>
          <tr><td>7. Less: Loss from House Property (Housing Loan Interest u/s 24(b))</td><td class="amt" id="stmt-old-hloan">0</td></tr>
          <tr><td>8. Add: Any Other Income (Interest, exam duty, etc.)</td><td class="amt" id="stmt-old-otherinc">0</td></tr>
          <tr class="total-row"><td><strong>9. Gross Total Income (GTI)</strong></td><td class="amt" id="stmt-old-gti" style="font-weight: 700;">0</td></tr>
          <tr>
            <td>
              10. Less: Deductions under Chapter VI-A:<br>
              <span style="font-size: 0.76rem; color: #475569;">
                - 80C (GPF, SLI, LIC, PPF, HBA Principal, Tuition, etc. Capped at ₹1.5L): ₹<span id="stmt-old-sub80c">0</span><br>
                - 80CCD(1B) Addl NPS: ₹<span id="stmt-old-sub80ccd1b">0</span> | 80CCD(2) Employer NPS: ₹<span id="stmt-old-sub80ccd2">0</span><br>
                - 80D Mediclaim: ₹<span id="stmt-old-sub80d">0</span> | 80E, 80G, 80EEB, 80TTA, 80U: ₹<span id="stmt-old-subother">0</span>
              </span>
            </td>
            <td class="amt" id="stmt-old-total-deductions" style="font-weight: 600;">0</td>
          </tr>
          <tr class="total-row" style="background-color: #f1f5f9;">
            <td><strong>11. TOTAL TAXABLE INCOME (Rounded to ₹10)</strong></td>
            <td class="amt" id="stmt-old-taxable" style="font-weight: 800;">0</td>
          </tr>
          <tr><td>12. Tax Computed on Total Income as per Old Slabs</td><td class="amt" id="stmt-old-slabtax">0</td></tr>
          <tr><td>13. Less: Tax Rebate under Section 87A <em>(Up to ₹12,500)</em></td><td class="amt" id="stmt-old-rebate" style="color: #15803d;">0</td></tr>
          <tr><td>14. Add: Health and Education Cess @ 4%</td><td class="amt" id="stmt-old-cess">0</td></tr>
          <tr class="total-row" style="background-color: #fef3c7;">
            <td style="font-weight: 800; color: #b45309;">15. TOTAL ANNUAL TAX PAYABLE (OLD REGIME)</td>
            <td class="amt" id="stmt-old-totaltax" style="font-weight: 800; color: #b45309;">0</td>
          </tr>
          <tr><td>16. Less: Tax Deducted at Source (TDS) Till Date</td><td class="amt" id="stmt-old-tds-paid">0</td></tr>
          <tr class="total-row" style="background-color: #fef2f2;">
            <td style="font-weight: 800; color: #b91c1c;">17. BALANCE TAX TO BE DEDUCTED / (REFUND)</td>
            <td class="amt" id="stmt-old-bal-tax" style="font-weight: 800; color: #b91c1c;">0</td>
          </tr>
        </tbody>
      </table>

      <!-- Old Regime Bottom Signatures -->
      <div class="bottom-signatures-grid" style="margin-top: 10px;">
        <div class="sig-box-left">
          <h4>EMPLOYEE DECLARATION</h4>
          <p style="line-height: 1.35; margin-bottom: 6px;">
            I, <strong id="old-decl-name">_________________</strong>, hereby declare that the particulars furnished above in respect of my salary, allowances, and deductions under the Old Tax Regime for FY 2026-27 are true and correct.
          </p>
          <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-top: auto;">
            <div>
              <p>Place: <span id="old-decl-place">_________________</span></p>
              <p style="margin-top: 3px;">Date: <span id="old-decl-date">_________________</span></p>
            </div>
            <div style="text-align: center; width: 140px;">
              <div class="signature-line-compact">Signature of Employee</div>
            </div>
          </div>
        </div>

        <div class="sig-box-right">
          <h4>VERIFICATION BY DRAWING & DISBURSING OFFICER (DDO)</h4>
          <p style="line-height: 1.35; margin-bottom: 6px;">
            Certified that the salary figures, allowances, and Chapter VI-A deductions stated above have been verified with official records.
          </p>
          <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-top: auto;">
            <div>
              <p>Station: <span id="old-ddo-station">_________________</span></p>
              <p style="margin-top: 3px;">Date: <span id="old-ddo-date">_________________</span></p>
            </div>
            <div style="text-align: center; width: 140px;">
              <div class="signature-line-compact">Signature of DDO</div>
            </div>
          </div>
        </div>
      </div>
    </div> <!-- END VIEW B: OLD REGIME -->


    <!-- ===================================================== -->
    <!-- VIEW C: COMPARATIVE ABSTRACT TABLE (FOR BOTH REGIMES) -->
    <!-- ===================================================== -->
    <div id="wrapper-section-comparative-abstract" class="page-break-before">
      <div class="statement-section-title">E. Comparative Statement: New Regime vs Old Regime</div>
      <table class="statement-table">
        <thead>
          <tr>
            <th>Particulars</th>
            <th>New Tax Regime (u/s 115BAC)</th>
            <th>Old Tax Regime</th>
            <th>Variance / Net Difference</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Gross Total Income (GTI)</td>
            <td class="amt" id="stmt-comp-gross-new">0</td>
            <td class="amt" id="stmt-comp-gross-old">0</td>
            <td class="text-center">-</td>
          </tr>
          <tr>
            <td>Total Deductions (Std Ded, HRA, 80C, 80D, etc.)</td>
            <td class="amt" id="stmt-comp-ded-new">0</td>
            <td class="amt" id="stmt-comp-ded-old">0</td>
            <td class="amt" id="stmt-comp-ded-diff">0</td>
          </tr>
          <tr>
            <td>Net Taxable Income</td>
            <td class="amt" id="stmt-comp-taxable-new">0</td>
            <td class="amt" id="stmt-comp-taxable-old">0</td>
            <td class="amt" id="stmt-comp-taxable-diff">0</td>
          </tr>
          <tr class="total-row">
            <td>Total Tax Payable (incl Cess)</td>
            <td class="amt" id="stmt-comp-tax-new" style="color: #0369a1;">0</td>
            <td class="amt" id="stmt-comp-tax-old" style="color: #b45309;">0</td>
            <td class="amt" id="stmt-comp-tax-diff" style="font-weight: 800; color: #15803d;">0</td>
          </tr>
          <tr>
            <td>Beneficial / Recommended Regime</td>
            <td colspan="3" class="text-center" id="stmt-comp-recommendation" style="font-weight: 700; color: #15803d;">
              -
            </td>
          </tr>
        </tbody>
      </table>
    </div>

  </div> <!-- END PRINT STATEMENT VIEW -->

</div> <!-- END CONTAINER -->

<!-- Sticky Bottom Live Bar -->
<div class="sticky-bar no-print">
  <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
    <div class="stat-pill">
      <span class="stat-label">Gross Income</span>
      <span class="stat-value" id="bar-gross">₹0</span>
    </div>
    <div class="stat-pill">
      <span class="stat-label">Deductions (Old)</span>
      <span class="stat-value" id="bar-deductions">₹50,000</span>
    </div>
    <div class="stat-pill highlight-new">
      <span class="stat-label">New Regime Tax</span>
      <span class="stat-value" id="bar-tax-new">₹0</span>
    </div>
    <div class="stat-pill highlight-old">
      <span class="stat-label">Old Regime Tax</span>
      <span class="stat-value" id="bar-tax-old">₹0</span>
    </div>
    <div class="recommendation-badge" id="bar-recommendation">
      -
    </div>
  </div>

  <div style="display: flex; gap: 8px;">
    <button type="button" class="btn btn-primary" id="btn-view-statement">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
      Generate Statement
    </button>
  </div>
</div>

<script>
(function() {
  'use strict';

  function formatINR(val) {
    if (isNaN(val) || val === null) return '0';
    let sign = val < 0 ? '-' : '';
    let absVal = Math.round(Math.abs(val));
    return sign + absVal.toLocaleString('en-IN');
  }

  function getNum(id) {
    let el = document.getElementById(id);
    if (!el) return 0;
    let v = parseFloat(el.value);
    return isNaN(v) ? 0 : v;
  }

  function setNum(id, val) {
    let el = document.getElementById(id);
    if (el) el.value = (val === 0 || val === undefined) ? '' : val;
  }

  function setText(id, text) {
    let el = document.getElementById(id);
    if (el) el.innerText = text;
  }

  function computeHRAExemption(rentPaid, actualHRA, basicPlusDA, isMetro) {
    if (rentPaid <= 0 || actualHRA <= 0) return 0;
    let excessRent = Math.max(0, rentPaid - (0.10 * basicPlusDA));
    let salaryPct = (isMetro ? 0.50 : 0.40) * basicPlusDA;
    return Math.min(actualHRA, excessRent, salaryPct);
  }

  function computeNewRegimeTax(taxableIncome) {
    let tax = 0;
    let rebate87A = 0;
    let marginalRelief = 0;

    if (taxableIncome > 400000) tax += Math.min(taxableIncome - 400000, 400000) * 0.05;
    if (taxableIncome > 800000) tax += Math.min(taxableIncome - 800000, 400000) * 0.10;
    if (taxableIncome > 1200000) tax += Math.min(taxableIncome - 1200000, 400000) * 0.15;
    if (taxableIncome > 1600000) tax += Math.min(taxableIncome - 1600000, 400000) * 0.20;
    if (taxableIncome > 2000000) tax += Math.min(taxableIncome - 2000000, 400000) * 0.25;
    if (taxableIncome > 2400000) tax += (taxableIncome - 2400000) * 0.30;

    if (taxableIncome <= 1200000) {
      rebate87A = Math.min(tax, 60000);
      tax = 0;
    } else {
      let excessIncome = taxableIncome - 1200000;
      if (tax > excessIncome) {
        marginalRelief = tax - excessIncome;
        tax = excessIncome;
      }
    }

    let surchargeRate = 0;
    if (taxableIncome > 50000000) surchargeRate = 0.25;
    else if (taxableIncome > 20000000) surchargeRate = 0.25;
    else if (taxableIncome > 10000000) surchargeRate = 0.15;
    else if (taxableIncome > 5000000) surchargeRate = 0.10;

    let surcharge = tax * surchargeRate;
    let cess = Math.round((tax + surcharge) * 0.04);
    let totalTax = Math.round(tax + surcharge + cess);

    return { tax, rebate87A, marginalRelief, surcharge, cess, totalTax };
  }

  function computeOldRegimeTax(taxableIncome, category) {
    let exemption = 250000;
    if (category === 'senior') exemption = 300000;
    else if (category === 'supersenior') exemption = 500000;

    let tax = 0;
    let rebate87A = 0;

    if (taxableIncome > exemption) {
      let slab5 = Math.min(taxableIncome - exemption, 500000 - exemption);
      if (slab5 > 0) tax += slab5 * 0.05;
    }
    if (taxableIncome > 500000) {
      tax += Math.min(taxableIncome - 500000, 500000) * 0.20;
    }
    if (taxableIncome > 1000000) {
      tax += (taxableIncome - 1000000) * 0.30;
    }

    if (taxableIncome <= 500000) {
      rebate87A = Math.min(tax, 12500);
      tax = 0;
    }

    let surchargeRate = 0;
    if (taxableIncome > 50000000) surchargeRate = 0.37;
    else if (taxableIncome > 20000000) surchargeRate = 0.25;
    else if (taxableIncome > 10000000) surchargeRate = 0.15;
    else if (taxableIncome > 5000000) surchargeRate = 0.10;

    let surcharge = tax * surchargeRate;
    let cess = Math.round((tax + surcharge) * 0.04);
    let totalTax = Math.round(tax + surcharge + cess);

    return { tax, rebate87A, marginalRelief: 0, surcharge, cess, totalTax };
  }

  window.copyDownFrom = function(startIdx) {
    let sourceVal = getNum('m-' + startIdx);
    if (sourceVal <= 0) {
      alert('Please enter a valid salary amount first before copying down.');
      return;
    }
    for (let i = startIdx + 1; i < 12; i++) {
      setNum('m-' + i, sourceVal);
    }
    calculateAll();
  };

  function calculateAll() {
    let monthlySalarySum = 0;
    for (let i = 0; i < 12; i++) {
      monthlySalarySum += getNum('m-' + i);
    }
    setText('total-monthly-salary', '₹' + formatINR(monthlySalarySum));

    let daArrear = getNum('da-arrear');
    let prArrear = getNum('pr-arrear');
    let otherArrear = getNum('other-arrear');
    let leaveSurrender = getNum('leave-surrender');
    let bonus = getNum('bonus');
    let excessPay = getNum('excess-pay');
    let otherSalaryInc = getNum('other-salary-inc');
    let anyOtherInc = getNum('any-other-inc');

    let totalArrears = daArrear + prArrear + otherArrear + leaveSurrender + bonus + otherSalaryInc;
    let totalGross = Math.max(0, monthlySalarySum + totalArrears - excessPay + anyOtherInc);
    setText('total-gross-income', '₹' + formatINR(totalGross));

    let rentPaid = getNum('hra-rent-paid');
    let actualHRA = getNum('hra-actual-received');
    let basicDA = getNum('hra-basic-da');
    let isMetro = document.getElementById('hra-city-metro').value === '1';
    let hraExemption = computeHRAExemption(rentPaid, actualHRA, basicDA, isMetro);
    setText('total-hra-exemption', '₹' + formatINR(hraExemption));

    let cGpf = getNum('c-gpf');
    let cSli = getNum('c-sli');
    let cLic = getNum('c-lic');
    let cPpf = getNum('c-ppf');
    let cHba = getNum('c-hba-principal');
    let cTuition = getNum('c-tuition');
    let cBankFd = getNum('c-bank-fd');
    let cElss = getNum('c-elss');
    let cNsc = getNum('c-nsc');
    let cPostOffice = getNum('c-post-office');
    let cNpsEmp = getNum('c-nps-emp');
    let cOther = getNum('c-other');

    let gross80C = cGpf + cSli + cLic + cPpf + cHba + cTuition + cBankFd + cElss + cNsc + cPostOffice + cNpsEmp + cOther;
    let eligible80C = Math.min(gross80C, 150000);
    setText('val-80c-gross', '₹' + formatINR(gross80C));
    setText('val-80c-eligible', '₹' + formatINR(eligible80C));
    setText('label-80c-status', 'Total: ₹' + formatINR(gross80C) + ' / ₹1,50,000');
    let pct80C = Math.min(100, Math.round((gross80C / 150000) * 100));
    let barEl = document.getElementById('bar-80c');
    if (barEl) {
      barEl.style.width = pct80C + '%';
      if (gross80C >= 150000) barEl.classList.add('overflow');
      else barEl.classList.remove('overflow');
    }

    let profTax = Math.min(2500, getNum('prof-tax'));
    let housingLoanInt = Math.min(200000, getNum('housing-loan-int'));
    let sec80EEA = Math.min(150000, getNum('sec-80eea'));
    let sec80DSelf = Math.min(50000, getNum('sec-80d-self'));
    let sec80DPar = Math.min(50000, getNum('sec-80d-parents'));
    let sec80CCD1B = Math.min(50000, getNum('sec-80ccd1b'));
    let sec80CCD2 = getNum('sec-80ccd2');
    let sec80E = getNum('sec-80e');
    let sec80G = getNum('sec-80g');
    let sec80EEB = Math.min(150000, getNum('sec-80eeb'));
    let sec80TTA = Math.min(50000, getNum('sec-80tta'));
    let sec80UDD = getNum('sec-80u-dd');

    let category = 'general';
    let catRadios = document.getElementsByName('taxpayer-category');
    for (let r of catRadios) { if (r.checked) { category = r.value; break; } }

    let stmtType = 'anticipatory';
    let stmtTypeRadios = document.getElementsByName('statement-type');
    for (let str of stmtTypeRadios) { if (str.checked) { stmtType = str.value; break; } }

    let stdDedNew = 75000;
    let totalDedNew = stdDedNew + sec80CCD2;
    let netTaxableNew = Math.max(0, totalGross - totalDedNew);
    netTaxableNew = Math.round(netTaxableNew / 10) * 10;
    let resNew = computeNewRegimeTax(netTaxableNew);

    let stdDedOld = 50000;
    let totalDedOld = stdDedOld + profTax + hraExemption + housingLoanInt + eligible80C + 
                      sec80EEA + sec80DSelf + sec80DPar + sec80CCD1B + sec80CCD2 + 
                      sec80E + sec80G + sec80EEB + sec80TTA + sec80UDD;
    let netTaxableOld = Math.max(0, totalGross - totalDedOld);
    netTaxableOld = Math.round(netTaxableOld / 10) * 10;
    let resOld = computeOldRegimeTax(netTaxableOld, category);

    let tdsPaid = getNum('tds-paid');
    let balanceNew = resNew.totalTax - tdsPaid;
    let balanceOld = resOld.totalTax - tdsPaid;

    let chosenRegime = 'new';
    let chosenRadios = document.getElementsByName('chosen-regime');
    for (let cr of chosenRadios) { if (cr.checked) { chosenRegime = cr.value; break; } }
    let chosenBalance = (chosenRegime === 'new') ? balanceNew : balanceOld;

    let pendingStartIdx = parseInt(document.getElementById('pending-from-month').value) || 0;
    let pendingMonthsCount = 12 - pendingStartIdx;
    if (pendingMonthsCount < 1) pendingMonthsCount = 1;

    let monthlyInstallment = Math.max(0, Math.ceil(chosenBalance / pendingMonthsCount));

    let pendingGroup = document.getElementById('group-pending-months');
    let installmentGroup = document.getElementById('group-installment-display');
    let finalExtra = document.getElementById('final-statement-extra-fields');
    let tdsLabel = document.getElementById('tds-input-label');
    let tdsDesc = document.getElementById('tds-input-desc');

    if (stmtType === 'final') {
      pendingGroup.style.display = 'none';
      installmentGroup.style.display = 'none';
      finalExtra.style.display = 'block';
      tdsLabel.innerText = 'Total TDS Deducted from Salary for the Year';
      tdsDesc.innerText = 'Sum of all TDS deductions made during March to February';
    } else {
      pendingGroup.style.display = 'block';
      installmentGroup.style.display = 'block';
      finalExtra.style.display = 'none';
      tdsLabel.innerText = 'Tax Already Deducted from Salary Till Date';
      tdsDesc.innerText = 'TDS deducted from monthly salary drawn so far';
      setText('val-monthly-installment', '₹' + formatINR(monthlyInstallment) + ' / month');
      setText('desc-monthly-installment', 'for ' + pendingMonthsCount + ' pending months (till Feb 2027)');
    }

    setText('sum-taxable-new', '₹' + formatINR(netTaxableNew));
    setText('sum-tax-new', '₹' + formatINR(resNew.totalTax));
    setText('sum-balance-new', (balanceNew >= 0 ? '₹' : '-₹') + formatINR(Math.abs(balanceNew)));

    setText('sum-taxable-old', '₹' + formatINR(netTaxableOld));
    setText('sum-tax-old', '₹' + formatINR(resOld.totalTax));
    setText('sum-balance-old', (balanceOld >= 0 ? '₹' : '-₹') + formatINR(Math.abs(balanceOld)));

    let newBox = document.getElementById('regime-box-new');
    let oldBox = document.getElementById('regime-box-old');
    let recBadge = document.getElementById('bar-recommendation');

    newBox.classList.remove('winner', 'selected');
    oldBox.classList.remove('winner', 'selected');

    if (chosenRegime === 'new') newBox.classList.add('selected');
    else oldBox.classList.add('selected');

    let diff = Math.abs(resNew.totalTax - resOld.totalTax);
    if (resNew.totalTax < resOld.totalTax) {
      newBox.classList.add('winner');
      recBadge.className = 'recommendation-badge new-win';
      recBadge.innerHTML = '★ NEW REGIME SAVES ₹' + formatINR(diff);
    } else if (resOld.totalTax < resNew.totalTax) {
      oldBox.classList.add('winner');
      recBadge.className = 'recommendation-badge old-win';
      recBadge.innerHTML = '★ OLD REGIME SAVES ₹' + formatINR(diff);
    } else {
      recBadge.className = 'recommendation-badge equal';
      recBadge.innerHTML = 'BOTH REGIMES HAVE SAME TAX LIABILITY';
    }

    setText('bar-gross', '₹' + formatINR(totalGross));
    setText('bar-deductions', '₹' + formatINR(totalDedOld));
    setText('bar-tax-new', '₹' + formatINR(resNew.totalTax));
    setText('bar-tax-old', '₹' + formatINR(resOld.totalTax));

    populateStatement({
      empName: document.getElementById('emp-name').value || 'Employee Name',
      designation: document.getElementById('emp-designation').value || 'Designation',
      pan: (document.getElementById('emp-pan').value || 'PAN NOT PROVIDED').toUpperCase(),
      office: document.getElementById('emp-office').value || 'Office / Institution',
      pen: document.getElementById('emp-pen').value || 'N/A',
      ddo: document.getElementById('emp-ddo').value || 'N/A',
      category: category,
      stmtType: stmtType,
      chosenRegime: chosenRegime,
      monthlySalarySum: monthlySalarySum,
      totalArrears: totalArrears,
      excessPay: excessPay,
      totalGross: totalGross,
      hraExemption: hraExemption,
      profTax: profTax,
      housingLoanInt: housingLoanInt,
      anyOtherInc: anyOtherInc,
      stdDedNew: stdDedNew,
      stdDedOld: stdDedOld,
      totalDedNew: totalDedNew,
      totalDedOld: totalDedOld,
      netTaxableNew: netTaxableNew,
      netTaxableOld: netTaxableOld,
      resNew: resNew,
      resOld: resOld,
      tdsPaid: tdsPaid,
      balanceNew: balanceNew,
      balanceOld: balanceOld,
      eligible80C: eligible80C,
      sec80CCD1B: sec80CCD1B,
      sec80CCD2: sec80CCD2,
      sec80DSelf: sec80DSelf,
      sec80DPar: sec80DPar,
      sec80E: sec80E,
      sec80G: sec80G,
      sec80EEB: sec80EEB,
      sec80TTA: sec80TTA,
      sec80UDD: sec80UDD,
      pendingMonthsCount: pendingMonthsCount,
      pendingStartIdx: pendingStartIdx,
      monthlyInstallment: monthlyInstallment
    });
  }

  function populateStatement(data) {
    let isFinal = (data.stmtType === 'final');
    
    // Set Titles
    if (isFinal) {
      setText('new-stmt-main-title', 'FINAL STATEMENT OF INCOME TAX ASSESSMENT FOR FY 2026–2027');
      setText('new-stmt-sub-title', '(Final Statement under Section 192 of the Income Tax Act, 1961 for Annual Assessment)');
      setText('old-stmt-main-title', 'FINAL STATEMENT OF INCOME TAX ASSESSMENT FOR FY 2026–2027');
      setText('new-sched-title', 'D. Final Tax Assessment & Settlement');
      setText('new-sched-bal-label', '3. Balance Tax Payable in Feb Salary / (Refund):');
      document.getElementById('new-row-installment').style.display = 'none';
      setText('new-decl-text', 'I, ' + data.empName + ', ' + data.designation + ', hereby declare that the particulars of my complete annual salary, allowances, and deductions under the New Tax Regime for FY 2026-27 are true, correct, and complete.');
    } else {
      setText('new-stmt-main-title', 'ANTICIPATORY STATEMENT OF INCOME TAX ASSESSMENT FOR FY 2026–2027');
      setText('new-stmt-sub-title', '(Anticipatory Statement under Section 192 of the Income Tax Act, 1961 for Monthly TDS Deductions)');
      setText('old-stmt-main-title', 'ANTICIPATORY STATEMENT OF INCOME TAX ASSESSMENT FOR FY 2026–2027');
      setText('new-sched-title', 'D. Tax Recovery & Installment Schedule');
      setText('new-sched-bal-label', '3. Balance Tax to be Deducted / Recovered:');
      document.getElementById('new-row-installment').style.display = 'table-row';
      setText('new-decl-text', 'I, ' + data.empName + ', ' + data.designation + ', hereby declare that the particulars of my salary, allowances, and deductions under the New Tax Regime for FY 2026-27 are true and correct to the best of my knowledge and belief.');
    }

    // Population for View A: New Regime Single Page
    setText('new-meta-name', data.empName);
    setText('new-meta-designation', data.designation);
    setText('new-meta-pan', data.pan);
    setText('new-meta-pen', data.pen);
    setText('new-meta-office', data.office);
    setText('new-meta-ddo', data.ddo);

    let catText = 'Individual (< 60 yrs)';
    if (data.category === 'senior') catText = 'Senior Citizen (60 – 79 yrs)';
    else if (data.category === 'supersenior') catText = 'Super Senior (80+ yrs)';
    setText('new-meta-category', catText);

    // Left Column Monthly Salaries
    for (let i = 0; i < 12; i++) {
      setText('new-stmt-m' + i, formatINR(getNum('m-' + i)));
    }
    setText('new-stmt-total-12m', formatINR(data.monthlySalarySum));

    // Arrears
    let daArr = getNum('da-arrear');
    let prArr = getNum('pr-arrear');
    setText('new-stmt-arr-dapr', formatINR(daArr + prArr));
    setText('new-stmt-arr-surrender', formatINR(getNum('leave-surrender')));
    setText('new-stmt-arr-bonus', formatINR(getNum('bonus')));
    setText('new-stmt-arr-other', formatINR(getNum('other-salary-inc') + data.anyOtherInc));
    setText('new-stmt-arr-excess', formatINR(data.excessPay));
    setText('new-stmt-gross-total', formatINR(data.totalGross));

    // Right Column Tax Computation
    setText('new-stmt-c-gross', formatINR(data.totalGross));
    setText('new-stmt-c-80ccd2', formatINR(data.sec80CCD2));
    setText('new-stmt-c-taxable', formatINR(data.netTaxableNew));
    setText('new-stmt-c-slabtax', formatINR(data.resNew.tax + data.resNew.rebate87A + data.resNew.marginalRelief));
    setText('new-stmt-c-rebate', formatINR(data.resNew.rebate87A));
    setText('new-stmt-c-marginal', formatINR(data.resNew.marginalRelief));
    setText('new-stmt-c-tax-after-rebate', formatINR(data.resNew.tax));
    setText('new-stmt-c-cess', formatINR(data.resNew.cess));
    setText('new-stmt-c-totaltax', formatINR(data.resNew.totalTax));

    // Schedule
    setText('new-sched-tax', '₹' + formatINR(data.resNew.totalTax));
    setText('new-sched-tds', '₹' + formatINR(data.tdsPaid));
    if (data.balanceNew < 0) {
      setText('new-sched-bal', '₹' + formatINR(Math.abs(data.balanceNew)) + ' (Refund)');
    } else {
      setText('new-sched-bal', '₹' + formatINR(data.balanceNew));
    }

    let monthNames = ['March 2026', 'April 2026', 'May 2026', 'June 2026', 'July 2026', 'August 2026', 'September 2026', 'October 2026', 'November 2026', 'December 2026', 'January 2027', 'February 2027'];
    let startMonthName = monthNames[data.pendingStartIdx] || 'October 2026';
    setText('new-sched-pending-desc', '(Pending Period: ' + startMonthName + ' to February 2027 = ' + data.pendingMonthsCount + ' Months)');
    let monthlyInstNew = Math.max(0, Math.ceil(data.balanceNew / data.pendingMonthsCount));
    setText('new-sched-monthly', '₹' + formatINR(monthlyInstNew) + ' / month');

    // Declarations
    setText('new-decl-name', data.empName);
    setText('new-decl-desig', data.designation);
    let today = new Date().toLocaleDateString('en-IN', { day: '2-digit', month: '2-digit', year: 'numeric' });
    setText('new-decl-date', today);
    setText('new-ddo-date', today);
    let stn = data.ddo.split('/')[1] || data.office || 'Thiruvananthapuram';
    setText('new-decl-place', stn.trim());
    setText('new-ddo-station', stn.trim());

    // Also update View B: Old Regime Data
    setText('stmt-name', data.empName);
    setText('stmt-designation', data.designation);
    setText('stmt-pan', data.pan);
    setText('stmt-office', data.office);
    setText('stmt-pen', data.pen);
    setText('stmt-ddo', data.ddo);
    setText('stmt-category', catText);
    for (let i = 0; i < 12; i++) setText('stmt-m' + i, formatINR(getNum('m-' + i)));
    setText('stmt-total-12m', formatINR(data.monthlySalarySum));
    setText('stmt-total-arrears', formatINR(data.totalArrears - data.excessPay));

    setText('stmt-old-gross', formatINR(data.totalGross));
    setText('stmt-old-excess', formatINR(data.excessPay));
    setText('stmt-old-hra', formatINR(data.hraExemption));
    setText('stmt-old-pt', formatINR(data.profTax));
    let incSalaryOld = Math.max(0, data.totalGross - data.stdDedOld - data.profTax - data.hraExemption);
    setText('stmt-old-inc-salary', formatINR(incSalaryOld));
    setText('stmt-old-hloan', formatINR(data.housingLoanInt));
    setText('stmt-old-otherinc', formatINR(data.anyOtherInc));
    let gtiOld = Math.max(0, incSalaryOld - data.housingLoanInt + data.anyOtherInc);
    setText('stmt-old-gti', formatINR(gtiOld));
    setText('stmt-old-sub80c', formatINR(data.eligible80C));
    setText('stmt-old-sub80ccd1b', formatINR(data.sec80CCD1B));
    setText('stmt-old-sub80ccd2', formatINR(data.sec80CCD2));
    setText('stmt-old-sub80d', formatINR(data.sec80DSelf + data.sec80DPar));
    setText('stmt-old-subother', formatINR(data.sec80E + data.sec80G + data.sec80EEB + data.sec80TTA + data.sec80UDD));
    let totalChapVI = data.eligible80C + data.sec80CCD1B + data.sec80CCD2 + data.sec80DSelf + data.sec80DPar + data.sec80E + data.sec80G + data.sec80EEB + data.sec80TTA + data.sec80UDD;
    setText('stmt-old-total-deductions', formatINR(totalChapVI));
    setText('stmt-old-taxable', formatINR(data.netTaxableOld));
    setText('stmt-old-slabtax', formatINR(data.resOld.tax + data.resOld.rebate87A));
    setText('stmt-old-rebate', formatINR(data.resOld.rebate87A));
    setText('stmt-old-cess', formatINR(data.resOld.cess));
    setText('stmt-old-totaltax', formatINR(data.resOld.totalTax));
    setText('stmt-old-tds-paid', formatINR(data.tdsPaid));
    setText('stmt-old-bal-tax', (data.balanceOld < 0 ? '-' : '') + '₹' + formatINR(Math.abs(data.balanceOld)));

    setText('old-decl-name', data.empName);
    setText('old-decl-place', stn.trim());
    setText('old-decl-date', today);
    setText('old-ddo-station', stn.trim());
    setText('old-ddo-date', today);

    // View C: Comparative Abstract
    setText('stmt-comp-gross-new', formatINR(data.totalGross));
    setText('stmt-comp-gross-old', formatINR(data.totalGross));
    setText('stmt-comp-ded-new', formatINR(data.totalDedNew));
    setText('stmt-comp-ded-old', formatINR(data.totalDedOld));
    setText('stmt-comp-ded-diff', formatINR(Math.abs(data.totalDedNew - data.totalDedOld)));
    setText('stmt-comp-taxable-new', formatINR(data.netTaxableNew));
    setText('stmt-comp-taxable-old', formatINR(data.netTaxableOld));
    setText('stmt-comp-taxable-diff', formatINR(Math.abs(data.netTaxableNew - data.netTaxableOld)));
    setText('stmt-comp-tax-new', formatINR(data.resNew.totalTax));
    setText('stmt-comp-tax-old', formatINR(data.resOld.totalTax));
    let taxDiff = Math.abs(data.resNew.totalTax - data.resOld.totalTax);
    setText('stmt-comp-tax-diff', '₹' + formatINR(taxDiff));

    let recText = '';
    if (data.resNew.totalTax < data.resOld.totalTax) {
      recText = 'NEW REGIME IS MORE BENEFICIAL (Tax Savings: ₹' + formatINR(taxDiff) + ')';
    } else if (data.resOld.totalTax < data.resNew.totalTax) {
      recText = 'OLD REGIME IS MORE BENEFICIAL (Tax Savings: ₹' + formatINR(taxDiff) + ')';
    } else {
      recText = 'EQUAL TAX LIABILITY UNDER BOTH REGIMES';
    }
    setText('stmt-comp-recommendation', recText);

    applyPrintRegimeFilter();
  }

  function applyPrintRegimeFilter() {
    let printChoice = 'new';
    let radios = document.getElementsByName('print-regime-choice');
    for (let r of radios) { if (r.checked) { printChoice = r.value; break; } }

    let wrapNew = document.getElementById('wrapper-section-new-regime');
    let wrapOld = document.getElementById('wrapper-section-old-regime');
    let wrapComp = document.getElementById('wrapper-section-comparative-abstract');

    if (printChoice === 'new') {
      wrapNew.style.display = 'block';
      wrapOld.style.display = 'none';
      wrapComp.style.display = 'none';
    } else if (printChoice === 'old') {
      wrapNew.style.display = 'none';
      wrapOld.style.display = 'block';
      wrapComp.style.display = 'none';
    } else {
      // Both
      wrapNew.style.display = 'block';
      wrapOld.style.display = 'block';
      wrapComp.style.display = 'block';
    }
  }

  function clearAllData() {
    if (!confirm('Are you sure you want to clear all data and reset the form to blank?')) return;
    
    document.querySelectorAll('input[type="text"], input[type="number"]').forEach(el => el.value = '');
    document.getElementById('hra-city-metro').value = '0';
    document.getElementById('pending-from-month').value = '7';
    
    let catRadio = document.querySelector('input[name="taxpayer-category"][value="general"]');
    if (catRadio) catRadio.checked = true;

    let regRadio = document.querySelector('input[name="chosen-regime"][value="new"]');
    if (regRadio) regRadio.checked = true;

    let stmtRadio = document.querySelector('input[name="statement-type"][value="anticipatory"]');
    if (stmtRadio) stmtRadio.checked = true;

    let printChoiceRadio = document.querySelector('input[name="print-regime-choice"][value="new"]');
    if (printChoiceRadio) printChoiceRadio.checked = true;

    calculateAll();
  }

  function loadKeralaGovtSample() {
    document.getElementById('emp-name').value = 'Ramesh Kumar P';
    document.getElementById('emp-designation').value = 'Senior Superintendent';
    document.getElementById('emp-pan').value = 'ABCDE1234F';
    document.getElementById('emp-office').value = 'Directorate of Economics & Statistics';
    document.getElementById('emp-pen').value = '641285';
    document.getElementById('emp-ddo').value = '0101-01 / Thiruvananthapuram';

    for (let i = 0; i < 4; i++) setNum('m-' + i, 85000);
    for (let i = 4; i < 12; i++) setNum('m-' + i, 88000);

    setNum('da-arrear', 18500);
    setNum('pr-arrear', 0);
    setNum('leave-surrender', 85000);
    setNum('bonus', 4000);
    setNum('excess-pay', 0);
    setNum('any-other-inc', 12000);

    setNum('hra-rent-paid', 120000);
    setNum('hra-actual-received', 48000);
    setNum('hra-basic-da', 840000);

    setNum('prof-tax', 2500);
    setNum('housing-loan-int', 140000);
    setNum('sec-80d-self', 22000);
    setNum('sec-80d-parents', 25000);
    setNum('sec-80ccd1b', 50000);

    setNum('c-gpf', 72000);
    setNum('c-sli', 18000);
    setNum('c-lic', 36000);
    setNum('c-hba-principal', 60000);
    setNum('c-tuition', 30000);

    setNum('tds-paid', 15000);

    calculateAll();
  }

  function loadCorporateSample() {
    document.getElementById('emp-name').value = 'Ananya Sharma';
    document.getElementById('emp-designation').value = 'Manager (Finance)';
    document.getElementById('emp-pan').value = 'BQAPS9876K';
    document.getElementById('emp-office').value = 'National Informatics Centre / PSU';
    document.getElementById('emp-pen').value = 'EMP89201';
    document.getElementById('emp-ddo').value = 'DEL-HQ-04 / New Delhi';

    for (let i = 0; i < 12; i++) setNum('m-' + i, 120000);

    setNum('bonus', 75000);
    setNum('leave-surrender', 0);
    setNum('any-other-inc', 24000);

    setNum('hra-rent-paid', 240000);
    setNum('hra-actual-received', 180000);
    setNum('hra-basic-da', 1050000);
    document.getElementById('hra-city-metro').value = '1';

    setNum('prof-tax', 2500);
    setNum('housing-loan-int', 0);
    setNum('sec-80d-self', 25000);
    setNum('sec-80d-parents', 35000);
    setNum('sec-80ccd1b', 50000);
    setNum('sec-80ccd2', 105000);

    setNum('c-ppf', 100000);
    setNum('c-elss', 50000);
    setNum('c-lic', 25000);

    setNum('tds-paid', 45000);

    calculateAll();
  }

  function copyMarchSalary() {
    let marchVal = getNum('m-0');
    if (marchVal <= 0) {
      alert('Please enter a valid salary amount in March 2026 first!');
      return;
    }
    for (let i = 1; i < 12; i++) {
      setNum('m-' + i, marchVal);
    }
    calculateAll();
  }

  function applyDAHike() {
    let hike = getNum('quick-da-amount');
    if (hike <= 0) {
      alert('Please enter a valid DA hike amount (e.g. 3000)');
      return;
    }
    let startIdx = parseInt(document.getElementById('quick-da-start-month').value) || 4;
    for (let i = startIdx; i < 12; i++) {
      let cur = getNum('m-' + i);
      setNum('m-' + i, cur + hike);
    }
    calculateAll();
  }

  function exportJSON() {
    let data = {};
    let inputs = document.querySelectorAll('input, select');
    inputs.forEach(el => {
      if (el.type === 'radio') {
        if (el.checked) data[el.name] = el.value;
      } else if (el.id) {
        data[el.id] = el.value;
      }
    });
    let jsonStr = JSON.stringify(data, null, 2);
    let blob = new Blob([jsonStr], { type: 'application/json' });
    let url = URL.createObjectURL(blob);
    let a = document.createElement('a');
    let pan = (document.getElementById('emp-pan').value || 'taxpayer').trim();
    a.href = url;
    a.download = 'Income_Tax_Statement_2026-27_' + pan + '.json';
    a.click();
    URL.revokeObjectURL(url);
  }

  function importJSON(file) {
    if (!file) return;
    let reader = new FileReader();
    reader.onload = function(e) {
      try {
        let data = JSON.parse(e.target.result);
        for (let k in data) {
          let el = document.getElementById(k);
          if (el) el.value = data[k];
          let radios = document.getElementsByName(k);
          if (radios.length > 0) {
            radios.forEach(r => { if (r.value === data[k]) r.checked = true; });
          }
        }
        calculateAll();
        alert('✓ Data imported successfully from ' + file.name);
      } catch (err) {
        alert('Invalid JSON file: ' + err.message);
      }
    };
    reader.readAsText(file);
  }

  function saveToStorage() {
    let data = {};
    let inputs = document.querySelectorAll('input, select');
    inputs.forEach(el => {
      if (el.type === 'radio') {
        if (el.checked) data[el.name] = el.value;
      } else if (el.id) {
        data[el.id] = el.value;
      }
    });
    localStorage.setItem('ecostatt_it_calculator_data', JSON.stringify(data));
    alert('✓ Draft saved successfully in your browser!');
  }

  function restoreFromStorage() {
    let raw = localStorage.getItem('ecostatt_it_calculator_data');
    if (!raw) {
      alert('No saved draft found in this browser.');
      return;
    }
    try {
      let data = JSON.parse(raw);
      for (let k in data) {
        let el = document.getElementById(k);
        if (el) el.value = data[k];
        let radios = document.getElementsByName(k);
        if (radios.length > 0) {
          radios.forEach(r => { if (r.value === data[k]) r.checked = true; });
        }
      }
      calculateAll();
      alert('✓ Draft restored successfully!');
    } catch (e) {
      alert('Failed to restore draft: ' + e.message);
    }
  }

  function showTab(tabName) {
    let calcTab = document.getElementById('tab-calculator');
    let stmtTab = document.getElementById('tab-statement');
    let calcView = document.getElementById('calculator-form-view');
    let stmtView = document.getElementById('print-statement-view');

    if (tabName === 'statement') {
      calcTab.classList.remove('active');
      stmtTab.classList.add('active');
      calcView.style.display = 'none';
      stmtView.style.display = 'block';
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      stmtTab.classList.remove('active');
      calcTab.classList.add('active');
      stmtView.style.display = 'none';
      calcView.style.display = 'block';
    }
  }

  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('input, select').forEach(el => {
      el.addEventListener('input', calculateAll);
      el.addEventListener('change', calculateAll);
    });

    document.getElementById('btn-fill-kerala').addEventListener('click', loadKeralaGovtSample);
    document.getElementById('btn-fill-corporate').addEventListener('click', loadCorporateSample);
    document.getElementById('btn-clear-all').addEventListener('click', clearAllData);
    document.getElementById('btn-copy-march').addEventListener('click', copyMarchSalary);
    document.getElementById('btn-apply-da-hike').addEventListener('click', applyDAHike);
    document.getElementById('btn-export-json').addEventListener('click', exportJSON);
    document.getElementById('btn-import-file').addEventListener('change', function(e) {
      if (e.target.files && e.target.files[0]) {
        importJSON(e.target.files[0]);
      }
    });
    document.getElementById('btn-save-draft').addEventListener('click', saveToStorage);
    document.getElementById('btn-load-draft').addEventListener('click', restoreFromStorage);

    document.getElementById('tab-calculator').addEventListener('click', () => showTab('calculator'));
    document.getElementById('tab-statement').addEventListener('click', () => showTab('statement'));
    document.getElementById('btn-view-statement').addEventListener('click', () => showTab('statement'));
    document.getElementById('btn-back-to-form').addEventListener('click', () => showTab('calculator'));

    document.getElementById('regime-box-new').addEventListener('click', () => {
      document.querySelector('input[name="chosen-regime"][value="new"]').checked = true;
      calculateAll();
    });
    document.getElementById('regime-box-old').addEventListener('click', () => {
      document.querySelector('input[name="chosen-regime"][value="old"]').checked = true;
      calculateAll();
    });

    document.querySelectorAll('input[name="print-regime-choice"]').forEach(el => {
      el.addEventListener('change', applyPrintRegimeFilter);
    });

    document.querySelectorAll('input[name="statement-type"]').forEach(el => {
      el.addEventListener('change', calculateAll);
    });

    let savedDraft = localStorage.getItem('ecostatt_it_calculator_data');
    if (savedDraft) {
      try {
        let data = JSON.parse(savedDraft);
        for (let k in data) {
          let el = document.getElementById(k);
          if (el) el.value = data[k];
          let radios = document.getElementsByName(k);
          if (radios.length > 0) {
            radios.forEach(r => { if (r.value === data[k]) r.checked = true; });
          }
        }
      } catch(e) {}
    }
    
    calculateAll();
  });

})();
</script>

</body>
</html>
'''

output_path = r'C:\Users\sures\.gemini\antigravity\scratch\income-tax-calculator-2026-27\index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated updated {output_path} ({len(html_content)} bytes)")
