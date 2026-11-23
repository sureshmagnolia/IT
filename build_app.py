# Income Tax Calculator & Form 10E Generator
# Generates the full index.html for deployment
import os

html_code = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Income Tax Statement & Form 10E Calculator FY 2026-27 (AY 2027-28)</title>
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
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding-bottom: 50px;
    }

    /* Navigation Bar */
    .top-nav {
      background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
      color: white;
      padding: 12px 24px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }

    .brand-title {
      font-size: 1.25rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .brand-subtitle {
      font-size: 0.8rem;
      opacity: 0.9;
      font-weight: 400;
    }

    .nav-tabs-wrapper {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }

    .tab-btn {
      background: rgba(255, 255, 255, 0.12);
      color: white;
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 0.875rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .tab-btn:hover {
      background: rgba(255, 255, 255, 0.25);
    }

    .tab-btn.active {
      background: white;
      color: var(--primary-dark);
      border-color: white;
      box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    /* Container */
    .container {
      max-width: 1240px;
      margin: 20px auto;
      padding: 0 16px;
    }

    /* Cards */
    .card {
      background: var(--card-bg);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 20px;
      margin-bottom: 20px;
      border: 1px solid var(--border);
    }

    .card-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 15px;
      padding-bottom: 8px;
      border-bottom: 2px solid #e2e8f0;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    /* Action bar */
    .action-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 20px;
      align-items: center;
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      padding: 12px 16px;
      border-radius: var(--radius);
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 0.875rem;
      font-weight: 600;
      cursor: pointer;
      border: none;
      transition: all 0.2s;
      text-decoration: none;
    }

    .btn-primary { background: var(--primary-light); color: white; }
    .btn-primary:hover { background: var(--primary); }
    .btn-success { background: var(--success); color: white; }
    .btn-success:hover { background: #15803d; }
    .btn-warning { background: var(--accent); color: #78350f; }
    .btn-warning:hover { background: #d97706; }
    .btn-danger { background: var(--danger); color: white; }
    .btn-danger:hover { background: #b91c1c; }
    .btn-secondary { background: #64748b; color: white; }
    .btn-secondary:hover { background: #475569; }
    .btn-outline { background: white; color: var(--text); border: 1px solid var(--border); }
    .btn-outline:hover { background: #f1f5f9; }

    /* Forms & Grids */
    .grid-2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
    .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
    .grid-4 { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; }

    .form-group {
      margin-bottom: 12px;
    }

    .form-group label {
      display: block;
      font-size: 0.825rem;
      font-weight: 600;
      color: #334155;
      margin-bottom: 4px;
    }

    .form-control {
      width: 100%;
      padding: 7px 10px;
      font-size: 0.875rem;
      border: 1px solid var(--border);
      border-radius: 5px;
      background: #ffffff;
      color: var(--text);
      transition: border-color 0.15s;
    }

    .form-control:focus {
      outline: none;
      border-color: var(--border-focus);
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
    }

    input[type="number"] {
      text-align: right;
      font-variant-numeric: tabular-nums;
    }

    /* Monthly Table */
    .table-responsive {
      overflow-x: auto;
      margin-bottom: 15px;
    }

    .salary-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.825rem;
    }

    .salary-table th, .salary-table td {
      border: 1px solid var(--border);
      padding: 6px 8px;
      text-align: right;
    }

    .salary-table th {
      background: #f1f5f9;
      font-weight: 700;
      color: #1e293b;
      text-align: center;
    }

    .salary-table tr:hover td {
      background: #f8fafc;
    }

    /* Comparisons & Badges */
    .badge {
      display: inline-block;
      padding: 3px 8px;
      border-radius: 12px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
    }

    .badge-primary { background: #dbeafe; color: #1e40af; }
    .badge-success { background: #dcfce7; color: #15803d; }
    .badge-warning { background: #fef3c7; color: #b45309; }

    .summary-card {
      background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
      border: 1px solid #86efac;
      border-radius: var(--radius);
      padding: 16px 18px;
      margin-bottom: 20px;
    }

    .regime-compare-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 12px;
      border-bottom: 1px solid #bbf7d0;
      padding-bottom: 10px;
    }

    .regime-compare-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: #065f46;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }

    .regime-compare-grid {
      display: grid;
      grid-template-columns: 1fr 1fr 1.3fr;
      gap: 12px;
      align-items: stretch;
    }

    .regime-box {
      background: #ffffff;
      border: 1px solid #bbf7d0;
      border-radius: 8px;
      padding: 10px 14px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }

    .regime-box-label {
      font-size: 0.775rem;
      font-weight: 600;
      color: #475569;
      margin-bottom: 3px;
      text-transform: uppercase;
    }

    .regime-box-val {
      font-size: 1.35rem;
      font-weight: 800;
      line-height: 1.15;
    }

    .regime-box-sub {
      font-size: 0.75rem;
      color: #64748b;
      margin-top: 3px;
    }

    .bottom-action-bar {
      background: #f8fafc;
      border: 2px solid #3b82f6;
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
      margin-top: 24px;
      padding: 18px 22px;
    }

    .bottom-action-content {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 14px;
    }

    .bottom-btn-group {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    /* ========================================================
       PRINT STYLES: Strict Single Page A4 Portrait Statement
       ======================================================== */
    @page {
      size: A4 portrait;
      margin: 8mm 10mm;
    }

    @media screen {
      .print-page {
        background: white;
        width: 100%;
        max-width: 210mm;
        margin: 0 auto 30px auto;
        padding: 10mm 12mm;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
        min-height: 297mm;
      }
    }

        /* Pure Black & White Print Form Styles */
    .print-page {
      background: #ffffff;
      color: #000000;
    }

    
    /* Toolbar & UI Polish */
    .action-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 20px;
      align-items: center;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      padding: 12px 16px;
      border-radius: var(--radius);
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    .toolbar-group {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      align-items: center;
    }

    .toolbar-label {
      font-size: 0.75rem;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      margin-right: 4px;
    }

    /* Statement Container: Exact 175mm max-width to guarantee zero right-edge clipping on A4 */
    .eco-stmt-container {
      font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
      color: #000000;
      font-size: 8pt;
      line-height: 1.2;
      width: 100%;
      max-width: 175mm;
      margin: 0 auto;
      padding: 0;
      box-sizing: border-box;
      background: #ffffff;
    }

    /* Modular Content Blocks (Zero Overflow, Safe A4 Fit) */
    .stmt-block {
      border: 1px solid #000000;
      margin-bottom: 4px;
      background: #ffffff;
      color: #000000;
      width: 100%;
      box-sizing: border-box;
      page-break-inside: avoid;
    }

    .stmt-block-signature {
      border: none !important;
      background: transparent !important;
      margin-top: 8px;
      margin-bottom: 0px;
    }

    .stmt-block-header {
      border: none;
      text-align: center;
      margin-bottom: 5px;
    }

    .stmt-block-header h1 {
      font-size: 10pt;
      font-weight: bold;
      margin: 0 0 2px 0;
      text-transform: uppercase;
      letter-spacing: 0.2px;
      color: #000000;
    }

    .stmt-block-header h2 {
      font-size: 8.5pt;
      margin: 0 0 2px 0;
      color: #000000;
    }

    .block-title-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #ffffff;
      border-bottom: 1px solid #000000;
      padding: 2.5px 8px;
      font-weight: bold;
      font-size: 8pt;
      color: #000000;
    }

    .block-body {
      padding: 3.5px 8px;
      background: #ffffff;
      color: #000000;
    }

    .sub-row {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      padding: 1.5px 0;
      font-size: 7.5pt;
      color: #000000;
    }

    .sub-row-total {
      border-top: 1px dashed #000000;
      font-weight: bold;
      margin-top: 2px;
      padding-top: 2px;
      font-size: 8pt;
      color: #000000;
    }

    .sub-row-highlight {
      background: #ffffff;
      border-top: 1px solid #000000;
      border-bottom: 1px solid #000000;
      padding: 2px 0;
      margin: 2px 0;
      font-weight: bold;
      color: #000000;
    }

    .grid-table {
      width: 100%;
      border-collapse: collapse;
      text-align: center;
      font-size: 7.5pt;
      margin: 2px 0 4px 0;
      border: 1px solid #000000;
      background: #ffffff;
      color: #000000;
    }

    .grid-table th, .grid-table td {
      border: 1px solid #000000;
      padding: 2px 1px;
      background: #ffffff;
      color: #000000;
    }

    .grid-table th {
      font-weight: bold;
    }

    .emp-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 8pt;
      background: #ffffff;
      color: #000000;
    }

    .emp-table td {
      padding: 2.5px 6px;
      border: 1px solid #000000;
      color: #000000;
      background: #ffffff;
    }

    .emp-table .lbl {
      font-weight: bold;
      width: 16%;
      background: #ffffff;
      color: #000000;
    }

    .emp-table .val {
      width: 34%;
      color: #000000;
    }

    .eco-emp-box {
      width: 100%;
      table-layout: fixed;
      border-collapse: collapse;
      margin-bottom: 5px;
      font-size: 8.5pt;
      color: #000000;
    }

    .eco-emp-box .label {
      font-weight: bold;
      width: 16%;
      background: #ffffff;
      color: #000000;
    }

    .eco-emp-box .val {
      width: 34%;
      color: #000000;
    }

    .eco-table {
      width: 100%;
      table-layout: fixed;
      border-collapse: collapse;
      margin-bottom: 5px;
      font-size: 8pt;
      color: #000000;
    }

    .eco-col-sl { width: 5%; text-align: center; font-weight: bold; color: #000000; }
    .eco-col-desc { width: 73%; color: #000000; }
    .eco-col-amt { width: 22%; text-align: right; font-variant-numeric: tabular-nums; font-weight: 600; color: #000000; padding-right: 8px; }

    .eco-sig-box {
      width: 100%;
      table-layout: fixed;
      margin-top: 8px;
      font-size: 8pt;
      page-break-inside: avoid;
      color: #000000;
    }

    .eco-sig-box td:last-child {
      padding-right: 8px;
    }



    .eco-header {
      text-align: center;
      margin-bottom: 6px;
      color: #000000;
    }

    .eco-header h1 {
      font-size: 11pt;
      font-weight: bold;
      margin: 0 0 2px 0;
      text-transform: uppercase;
      letter-spacing: 0.3px;
      color: #000000;
    }

    .eco-header h2 {
      font-size: 9.5pt;
      font-weight: bold;
      margin: 0 0 2px 0;
      color: #000000;
    }

    .eco-header p {
      font-size: 7.5pt;
      margin: 0;
      font-style: italic;
      color: #000000;
    }

    .eco-mode-tag {
      font-size: 8pt;
      font-weight: bold;
      text-transform: uppercase;
      border: 1px solid #000000;
      padding: 1px 6px;
      display: inline-block;
      margin-top: 3px;
      border-radius: 2px;
      background: #ffffff;
      color: #000000;
    }

    .eco-emp-box {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 5px;
      font-size: 8.5pt;
      color: #000000;
    }

    .eco-emp-box td {
      border: 1px solid #000000;
      padding: 2.5px 5px;
      vertical-align: middle;
      color: #000000;
      background: #ffffff;
    }

    .eco-emp-box .label {
      font-weight: bold;
      width: 15%;
      background: #ffffff;
      color: #000000;
    }

    .eco-emp-box .val {
      width: 35%;
      color: #000000;
    }

    .eco-table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 5px;
      font-size: 8pt;
      color: #000000;
    }

    .eco-table th, .eco-table td {
      border: 1px solid #000000;
      padding: 2.5px 4px;
      vertical-align: middle;
      color: #000000;
      background: #ffffff;
    }

    .eco-table th {
      background: #ffffff;
      font-weight: bold;
      text-align: center;
      color: #000000;
    }

    .eco-col-sl { width: 5%; text-align: center; font-weight: bold; color: #000000; }
    .eco-col-desc { width: 68%; color: #000000; }
    .eco-col-amt { width: 27%; text-align: right; font-variant-numeric: tabular-nums; font-weight: 500; color: #000000; }

    .sub-salary-table {
      width: 100%;
      border-collapse: collapse;
      margin: 3px 0;
      font-size: 7.5pt;
      color: #000000;
    }

    .sub-salary-table th, .sub-salary-table td {
      border: 1px solid #000000;
      padding: 1.5px 2px;
      text-align: center;
      color: #000000;
      background: #ffffff;
    }

    .sub-salary-table th {
      background: #ffffff;
      font-weight: bold;
      color: #000000;
    }

    .sub-salary-table td {
      text-align: right;
      padding-right: 3px;
      color: #000000;
    }

    .eco-sig-box {
      width: 100%;
      margin-top: 8px;
      font-size: 8pt;
      page-break-inside: avoid;
      color: #000000;
    }

    .eco-sig-box td {
      vertical-align: top;
      padding: 0 4px;
      color: #000000;
    }

    /* Print media overrides - STRICT PURE BLACK AND WHITE */
    @media print {
      *, *::before, *::after {
        color: #000000 !important;
        background-color: transparent !important;
        border-color: #000000 !important;
        box-shadow: none !important;
        text-shadow: none !important;
      }

      body, html {
        background: #ffffff !important;
        color: #000000 !important;
        margin: 0 !important;
        padding: 0 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }

      .no-print, .top-nav, .action-bar, .card, footer, #calculator-form-view, #tax-slabs-view {
        display: none !important;
      }

      .print-page {
        border: none !important;
        box-shadow: none !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 100% !important;
        max-width: 100% !important;
        min-height: auto !important;
        background: #ffffff !important;
        color: #000000 !important;
      }

      .eco-stmt-container, .eco-stmt-container * {
        color: #000000 !important;
        background: #ffffff !important;
        border-color: #000000 !important;
      }

      .eco-mode-tag {
        background: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
      }

      .stmt-block-signature {
        border: none !important;
        background: transparent !important;
      }

      .eco-table th, .eco-table td,
      .eco-emp-box td, .eco-emp-box th,
      .sub-salary-table th, .sub-salary-table td {
        border: 1px solid #000000 !important;
        background: #ffffff !important;
        color: #000000 !important;
      }

      /* Specific print control */
      body.printing-new-regime #old-regime-statement-view,
      body.printing-new-regime #form-10e-view,
      body.printing-new-regime #calculator-form-view {
        display: none !important;
      }

      body.printing-new-regime #new-regime-statement-view {
        display: block !important;
        page-break-after: avoid !important;
        page-break-inside: avoid !important;
      }

      body.printing-old-regime #new-regime-statement-view,
      body.printing-old-regime #form-10e-view,
      body.printing-old-regime #calculator-form-view {
        display: none !important;
      }

      body.printing-old-regime #old-regime-statement-view {
        display: block !important;
      }

      body.printing-10e #new-regime-statement-view,
      body.printing-10e #old-regime-statement-view,
      body.printing-10e #calculator-form-view {
        display: none !important;
      }

      body.printing-10e #form-10e-view {
        display: block !important;
      }

      body.printing-10e .no-print-10e {
        display: none !important;
      }
    }

    /* Mobile-Friendly & Zero Horizontal Scroll Styles */
    html, body {
      overflow-x: hidden;
      width: 100%;
      max-width: 100vw;
      margin: 0;
      padding: 0;
    }

    .container {
      width: 100%;
      max-width: 1200px;
      margin: 16px auto;
      padding: 0 12px;
      overflow-x: hidden;
    }

    .btn {
      white-space: normal;
      text-align: center;
      line-height: 1.3;
    }

    .print-page-wrapper {
      width: 100%;
      display: flex;
      justify-content: center;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      padding: 2px;
      margin-bottom: 25px;
    }

    @media screen and (max-width: 768px) {
      .top-nav {
        flex-direction: column;
        align-items: stretch;
        padding: 10px 12px;
        gap: 8px;
      }

      .brand-title {
        font-size: 1.05rem;
        justify-content: center;
        text-align: center;
      }

      .brand-subtitle {
        text-align: center;
        font-size: 0.75rem;
      }

      .nav-tabs-wrapper {
        display: flex;
        flex-wrap: wrap;
        gap: 4px;
        width: 100%;
      }

      .tab-btn {
        flex: 1 1 calc(50% - 6px);
        padding: 7px 6px;
        font-size: 0.75rem;
        justify-content: center;
        text-align: center;
      }

      .action-bar {
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
        padding: 10px;
      }

      .action-bar .btn {
        width: 100%;
        justify-content: center;
        padding: 9px 12px;
        font-size: 0.85rem;
      }

      .grid-2, .grid-3, .grid-4 {
        grid-template-columns: 1fr !important;
        gap: 10px !important;
      }

      .card {
        padding: 14px 12px;
        margin-bottom: 14px;
      }

      /* Responsive Mobile Monthly Salary Cards */
      .salary-table, .salary-table thead, .salary-table tbody, .salary-table tfoot, .salary-table tr, .salary-table td, .salary-table th {
        display: block;
        width: 100%;
        box-sizing: border-box;
      }

      .salary-table thead {
        display: none;
      }

      .salary-table tbody tr {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        margin-bottom: 12px;
        padding: 10px 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        box-sizing: border-box;
      }

      .salary-table tbody td {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: none;
        padding: 6px 0;
        text-align: left;
        border-bottom: 1px solid #f1f5f9;
        font-size: 0.85rem;
        box-sizing: border-box;
      }

      .salary-table tbody td:first-child {
        background: #f8fafc;
        padding: 6px 8px;
        border-radius: 4px;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 4px;
        border-bottom: none;
      }

      .salary-table tbody td:last-child {
        border-bottom: none;
        justify-content: center;
        padding-top: 8px;
      }

      .salary-table tbody td::before {
        content: attr(data-label);
        font-weight: 600;
        font-size: 0.8rem;
        color: #475569;
        min-width: 120px;
        text-align: left;
      }

      .salary-table tbody td:first-child::before,
      .salary-table tbody td:last-child::before {
        display: none;
      }

      .salary-table tbody td input {
        max-width: 150px;
        font-size: 0.85rem;
        padding: 5px 8px;
      }

      .salary-table tfoot {
        display: block;
        width: 100%;
        box-sizing: border-box;
        margin-top: 10px;
      }

      .salary-table tfoot tr {
        display: block;
        width: 100%;
        background: #f8fafc;
        border: 2px solid #3b82f6;
        border-radius: 8px;
        padding: 10px 14px;
        box-sizing: border-box;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
      }

      .salary-table tfoot td {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: none;
        border-bottom: 1px dashed #cbd5e1;
        padding: 6px 0;
        font-size: 0.85rem;
        box-sizing: border-box;
        width: 100%;
      }

      .salary-table tfoot td:last-child {
        display: none !important;
      }

      .salary-table tfoot td.total-heading {
        background: #1e3a8a;
        color: #ffffff;
        font-weight: 700;
        font-size: 0.85rem;
        padding: 8px 10px;
        border-radius: 6px;
        margin-bottom: 8px;
        border-bottom: none;
        justify-content: center;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 0.3px;
      }

      .salary-table tfoot td.total-heading::before {
        display: none !important;
      }

      .salary-table tfoot td::before {
        content: attr(data-label);
        font-weight: 600;
        color: #334155;
        font-size: 0.825rem;
      }

      /* Mobile comparison grid and bottom actions */
      .regime-compare-header {
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
        text-align: center;
      }

      .regime-compare-title {
        text-align: center;
      }

      .regime-badge {
        align-self: center;
        width: 100%;
        text-align: center;
        padding: 6px 12px;
        font-size: 0.85rem;
      }

      .regime-compare-grid {
        grid-template-columns: 1fr 1fr;
        gap: 8px;
      }

      .regime-box-tds {
        grid-column: span 2;
        background: #fef2f2;
        border-color: #fecaca;
        text-align: center;
        align-items: center;
      }

      .bottom-action-bar {
        padding: 14px 12px !important;
      }

      .bottom-action-content {
        flex-direction: column !important;
        align-items: stretch !important;
        text-align: center;
      }

      .bottom-btn-group {
        flex-direction: column;
        gap: 8px;
        width: 100%;
        margin-top: 10px;
      }

      .bottom-btn-group .btn {
        width: 100% !important;
        justify-content: center !important;
        padding: 11px 16px !important;
        font-size: 0.95rem !important;
      }

      /* Print Page Preview on Mobile */
      .print-page {
        padding: 6mm 6mm;
        box-shadow: none;
        border: 1px solid #cbd5e1;
      }

      .eco-header h1 {
        font-size: 9pt;
      }
      .eco-header h2 {
        font-size: 8pt;
      }
      .eco-header p {
        font-size: 7pt;
      }
      .eco-table {
        font-size: 7pt;
      }
      .eco-table th, .eco-table td {
        padding: 2px 2px;
      }
      .sub-salary-table {
        font-size: 6.5pt;
      }
      .sub-salary-table th, .sub-salary-table td {
        padding: 1px 1px;
      }
    }

  </style>
  <script src="html2pdf.bundle.min.js"></script>
  <script>
    if (typeof html2pdf === 'undefined') {
      document.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"><\\/script>');
    }
  </script>
</head>
<body>

  <!-- Top Navigation -->
  <nav class="top-nav no-print">
    <div>
      <div class="brand-title">🏛️ Income Tax FY 2026-27 (AY 2027-28)</div>
      <div class="brand-subtitle">Anticipatory & Final Statement Generator &bull; Form 10E Section 89 Relief</div>
    </div>
    <div class="nav-tabs-wrapper">
      <button class="tab-btn active" id="tab-calculator" onclick="showTab('calculator')">📊 Tax Calculator</button>
      <button class="tab-btn" id="tab-new-regime" onclick="showTab('new-regime')">📄 New Regime Statement (1-Page A4)</button>
      <button class="tab-btn" id="tab-old-regime" onclick="showTab('old-regime')">⚖️ Old Regime Statement</button>
      <button class="tab-btn" id="tab-form-10e" onclick="showTab('form-10e')">📑 Form 10E (Sec 89 Relief)</button>
      <button class="tab-btn" id="tab-slabs" onclick="showTab('slabs')">ℹ️ Tax Slabs</button>
    </div>
  </nav>

  <div class="container">

    <!-- ========================================== -->
    <!-- VIEW 1: TAX CALCULATOR & DATA ENTRY FORM  -->
    <!-- ========================================== -->
    <div id="calculator-form-view">

            <!-- Action Bar: Data Actions, Backup/Restore, Outputs -->
      <div class="action-bar no-print">
        <div class="toolbar-group">
          <span class="toolbar-label">Quick Actions:</span>
          <button class="btn btn-outline" onclick="loadSampleData()" title="Load sample college professor data">📄 Load Sample</button>
          <button class="btn btn-warning" onclick="applyDAHikePrompt()" title="Apply percentage DA hike from a month">📈 DA Hike</button>
          <button class="btn btn-danger" onclick="clearAllData()" title="Clear all entered fields to zero">🧹 Clear All</button>
        </div>

        <div class="toolbar-group">
          <span class="toolbar-label">Save & Backup:</span>
          <button class="btn btn-outline" onclick="saveDraft()" title="Save current draft to browser memory">💾 Save Draft</button>
          <button class="btn btn-outline" onclick="restoreDraft()" title="Restore previously saved draft">📂 Load Draft</button>
          <button class="btn btn-outline" onclick="exportJSON()" title="Download a JSON backup file to your computer">📥 Export JSON</button>
          <button class="btn btn-outline" onclick="triggerImportJSON()" title="Upload a previously saved JSON file">📤 Import JSON</button>
          <input type="file" id="json-file-input" accept=".json" style="display:none;" onchange="handleFileImport(event)">
        </div>

        <div class="toolbar-group" style="margin-left:auto;">
          <span class="toolbar-label">Outputs:</span>
          <button class="btn btn-outline" onclick="showTab('new-regime')">👁️ View Statement</button>
          <button class="btn btn-success" onclick="downloadNewRegimePdf()" title="Download crisp, neat single-page A4 PDF">📥 Download A4 PDF</button>
          <button class="btn btn-secondary" onclick="printNewRegimeStatement()" title="Print directly or save via browser print dialog">🖨️ Print</button>
        </div>
      </div>

      <!-- Live Tax Comparison Card (Responsive Grid) -->
      <div class="summary-card">
        <div class="regime-compare-header">
          <span class="regime-compare-title">📊 Tax Regime Comparison (FY 2026-27)</span>
          <div id="top-regime-recommendation" class="badge badge-success regime-badge">
            Comparing...
          </div>
        </div>
        <div class="regime-compare-grid">
          <div class="regime-box">
            <span class="regime-box-label">New Regime Tax</span>
            <span class="regime-box-val" style="color:#1e3a8a;" id="top-new-tax">₹0</span>
          </div>
          <div class="regime-box">
            <span class="regime-box-label">Old Regime Tax</span>
            <span class="regime-box-val" style="color:#0d9488;" id="top-old-tax">₹0</span>
          </div>
          <div class="regime-box regime-box-tds">
            <span class="regime-box-label">Anticipatory Monthly Deduction</span>
            <span class="regime-box-val" style="color:#b91c1c;" id="top-monthly-tds">₹0 / month</span>
            <span class="regime-box-sub" id="top-pending-months-label">(for remaining months)</span>
          </div>
        </div>
      </div>

      <!-- Employee Details Card -->
      <div class="card">
        <div class="card-title">
          <span>👤 Employee & Statement Details</span>
          <span style="font-size:0.8rem; font-weight:normal; color:#64748b;">(Govt of Kerala & General Salaried)</span>
        </div>
        <div class="grid-3">
          <div class="form-group">
            <label for="emp-name">Employee Name</label>
            <input type="text" class="form-control" id="emp-name" value="" placeholder="Enter Employee Name" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="emp-pan">PAN (10 digits)</label>
            <input type="text" class="form-control" id="emp-pan" value="" placeholder="PAN (10 chars)" maxlength="10" style="text-transform:uppercase;" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="emp-pen">PEN / Employee ID</label>
            <input type="text" class="form-control" id="emp-pen" value="" placeholder="PEN / Emp ID" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="emp-designation">Designation</label>
            <input type="text" class="form-control" id="emp-designation" value="" placeholder="Enter Designation" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="emp-office">Office / Department</label>
            <input type="text" class="form-control" id="emp-office" value="" placeholder="Enter Office / Department" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="emp-place">Place (for Declaration)</label>
            <input type="text" class="form-control" id="emp-place" value="" placeholder="Place" oninput="calculateAll()">
          </div>
        </div>

        <div class="grid-3" style="margin-top:10px; background:#f8fafc; padding:12px; border-radius:6px; border:1px solid #e2e8f0;">
          <div class="form-group">
            <label for="stmt-mode">Statement Mode</label>
            <select class="form-control" id="stmt-mode" onchange="calculateAll()" style="font-weight:700; color:#1e3a8a;">
              <option value="anticipatory" selected>ANTICIPATORY STATEMENT (Monthly TDS)</option>
              <option value="final">FINAL STATEMENT (Annual Tax Return)</option>
            </select>
          </div>
          <div class="form-group">
            <label for="stmt-date">Statement Date</label>
            <input type="date" class="form-control" id="stmt-date" value="2026-11-23" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="pending-months">Pending Months for TDS deduction</label>
            <input type="number" class="form-control" id="pending-months" value="3" min="1" max="12" oninput="calculateAll()">
          </div>
        </div>
      </div>

      <!-- Monthly Salary Table Card -->
      <div class="card">
        <div class="card-title">
          <span>📅 Monthly Gross Salary (March 2026 to February 2027)</span>
        </div>
        <div class="table-responsive">
          <table class="salary-table" id="salary-input-table">
            <thead>
              <tr>
                <th style="text-align:left; width:15%;">Month</th>
                <th style="width:19%;">Basic Pay + DA (Gross)</th>
                <th style="width:15%;">Other Allowances</th>
                <th style="width:16%;">Total Monthly Gross</th>
                <th style="width:15%;">PF / NPS Deducted</th>
                <th style="width:15%;">Tax Deducted (TDS)</th>
                <th style="width:12%; text-align:center;">Copy Down</th>
              </tr>
            </thead>
            <tbody id="salary-table-body">
              <!-- Dynamically populated -->
            </tbody>
            <tfoot>
              <tr style="background:#fff; font-weight:bold;">
                <td class="total-heading" style="text-align:left;">Total of Monthly Gross Salary (a):</td>
                <td id="tot-basic" data-label="Total Basic Pay + DA:">0</td>
                <td id="tot-allow" data-label="Total Other Allowances:">0</td>
                <td id="tot-gross" data-label="Total Monthly Gross Salary:" style="color:#1e3a8a; font-weight:700; font-size:0.95rem;">0</td>
                <td id="tot-pf" data-label="Total PF / NPS Deducted:">0</td>
                <td id="tot-tds" data-label="Total TDS Deducted:" style="color:#dc2626; font-weight:700; font-size:0.95rem;">0</td>
                <td class="total-dash" style="text-align:center;"><small style="color:#64748b;">-</small></td>
              </tr>
            </tfoot>
          </table>
        </div>
      </div>

      <!-- Additional Income & Section 14 Items Card -->
      <div class="grid-2">
        <div class="card">
          <div class="card-title">💵 Arrears, Surrender & Additional Receipts</div>
          <div class="form-group">
            <label for="row1b-surrender">Leave Surrender (₹)</label>
            <input type="number" class="form-control" id="row1b-surrender" value="0" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="row1b-bonus">Bonus / Festival Allowance (₹)</label>
            <input type="number" class="form-control" id="row1b-bonus" value="0" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="row1b-arrears">Salary / DA / Pay Revision Arrears (₹)</label>
            <input type="number" class="form-control" id="row1b-arrears" value="0" oninput="calculateAll()">
            <small style="color:#64748b; font-size:0.75rem;">If claiming relief u/s 89, arrears must be included in gross income.</small>
          </div>
          <div class="form-group">
            <label for="row1b-other">Other Income / Allowances (₹)</label>
            <input type="number" class="form-control" id="row1b-other" value="0" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="row1c-excess">Excess Pay Refund / Recovery (Row 1c) (₹)</label>
            <input type="number" class="form-control" id="row1c-excess" value="0" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="row3-remuneration">Examination / Valuation Remuneration (Row 3) (₹)</label>
            <input type="number" class="form-control" id="row3-remuneration" value="0" oninput="calculateAll()">
          </div>
        </div>

        <div class="card">
          <div class="card-title">🛡️ Deductions & Reliefs</div>
          <div class="form-group">
            <label>Standard Deduction (Row 2a)</label>
            <div style="display:flex; gap:10px;">
              <span class="form-control" style="background:#f1f5f9; font-weight:bold; color:#1e3a8a;">New: ₹75,000</span>
              <span class="form-control" style="background:#f1f5f9; font-weight:bold; color:#0d9488;">Old: ₹50,000</span>
            </div>
          </div>
          <div class="form-group">
            <label for="row2b-conveyance">Conveyance Allowance for Differently Abled (Row 2b) (₹)</label>
            <input type="number" class="form-control" id="row2b-conveyance" value="0" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="row2c-nps">Employer NPS Contribution u/s 80CCD(2) (Row 2c) (₹)</label>
            <input type="number" class="form-control" id="row2c-nps" value="0" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="row2e-proftax">Professional Tax / Tax on Employment (Row 2e) (₹)</label>
            <input type="number" class="form-control" id="row2e-proftax" value="2500" oninput="calculateAll()">
          </div>
          <div class="form-group" style="background:#fef3c7; padding:10px; border-radius:6px; border:1px solid #fde68a;">
            <label for="row11-relief89" style="color:#92400e; font-weight:bold;">
              Relief u/s 89(1) for Arrears (Row 11) (₹)
            </label>
            <div style="display:flex; gap:6px;">
              <input type="number" class="form-control" id="row11-relief89" value="0" oninput="calculateAll()" style="font-weight:bold; color:#b45309;">
              <button class="btn btn-warning" style="white-space:nowrap; font-size:0.75rem;" onclick="showTab('form-10e')">Calculate in 10E</button>
            </div>
            <small style="color:#b45309; font-size:0.75rem;">Calculated via Form 10E based on historical slabs.</small>
          </div>
        </div>
      </div>

            <!-- Old Regime Detailed Chapter VI-A Deductions Card -->
      <div class="card">
        <div class="card-title">
          <span>📑 Detailed Chapter VI-A Deductions (For Old Tax Regime)</span>
          <span style="font-size:0.8rem; color:#64748b;">(Applicable if opting for Old Regime)</span>
        </div>
        
        <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:6px; padding:12px; margin-bottom:14px;">
          <h4 style="font-size:0.9rem; color:#1e293b; margin-bottom:8px;">Section 80C Investments & Savings (Overall Max Limit: ₹1,50,000)</h4>
          <div class="grid-4">
            <div class="form-group">
              <label for="ded-gpf">GPF / EPF Subscription (₹)</label>
              <input type="number" class="form-control ded-80c-item" id="ded-gpf" value="0" oninput="calculateAll()">
            </div>
            <div class="form-group">
              <label for="ded-sli">SLI (State Life Insurance) (₹)</label>
              <input type="number" class="form-control ded-80c-item" id="ded-sli" value="0" oninput="calculateAll()">
            </div>
            <div class="form-group">
              <label for="ded-gis">GIS (Group Insurance) (₹)</label>
              <input type="number" class="form-control ded-80c-item" id="ded-gis" value="0" oninput="calculateAll()">
            </div>
            <div class="form-group">
              <label for="ded-lic">LIC / Life Insurance Premium (₹)</label>
              <input type="number" class="form-control ded-80c-item" id="ded-lic" value="0" oninput="calculateAll()">
            </div>
            <div class="form-group">
              <label for="ded-tuition">Tuition Fees (max 2 children) (₹)</label>
              <input type="number" class="form-control ded-80c-item" id="ded-tuition" value="0" oninput="calculateAll()">
            </div>
            <div class="form-group">
              <label for="ded-hl-principal">Housing Loan Principal Repayment (₹)</label>
              <input type="number" class="form-control ded-80c-item" id="ded-hl-principal" value="0" oninput="calculateAll()">
            </div>
            <div class="form-group">
              <label for="ded-ppf">PPF / Sukanya / NSC / 5-Yr FD (₹)</label>
              <input type="number" class="form-control ded-80c-item" id="ded-ppf" value="0" oninput="calculateAll()">
            </div>
            <div class="form-group">
              <label for="ded-80c-other">Other 80C Investments (₹)</label>
              <input type="number" class="form-control ded-80c-item" id="ded-80c-other" value="0" oninput="calculateAll()">
            </div>
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px dashed #cbd5e1; padding-top:6px; margin-top:4px;">
            <span style="font-size:0.85rem; font-weight:600; color:#334155;">Total 80C Claimed: <strong id="lbl-80c-claimed">₹0</strong></span>
            <span style="font-size:0.85rem; font-weight:700; color:#1e40af;">Eligible Deduction u/s 80C (Capped at 1.5L): <strong id="lbl-80c-eligible">₹0</strong></span>
          </div>
        </div>

        <div class="grid-3">
          <div class="form-group">
            <label for="ded-80ccd1b">80CCD(1B): Additional NPS Voluntary (Max ₹50,000)</label>
            <input type="number" class="form-control" id="ded-80ccd1b" value="0" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="ded-80d">80D: MediSep / Health Insurance (Self & Parents)</label>
            <input type="number" class="form-control" id="ded-80d" value="0" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="ded-24b">24(b): Housing Loan Interest (Self-occupied max 2L)</label>
            <input type="number" class="form-control" id="ded-24b" value="0" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="ded-80e">80E: Higher Education Loan Interest (No limit)</label>
            <input type="number" class="form-control" id="ded-80e" value="0" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="ded-80g">80G: Approved Donations (CMDRF, PMNRF, etc.)</label>
            <input type="number" class="form-control" id="ded-80g" value="0" oninput="calculateAll()">
          </div>
          <div class="form-group">
            <label for="ded-80tta">80TTA / 80TTB: Savings Bank Interest Deduction</label>
            <input type="number" class="form-control" id="ded-80tta" value="0" oninput="calculateAll()">
          </div>
        </div>
      </div>

      <!-- Bottom Action Bar for Quick Save & Statement Generation -->
      <div class="card bottom-action-bar">
        <div class="bottom-action-content">
          <div>
            <h4 style="margin:0 0 4px 0; color:#1e3a8a; font-size:1.05rem; font-weight:700;">✅ Done Entering Data?</h4>
            <p style="margin:0; font-size:0.85rem; color:#475569;">Save your draft securely or generate your official printable/downloadable A4 statement.</p>
          </div>
          <div class="bottom-btn-group">
            <button class="btn btn-outline" style="font-weight:700;" onclick="saveDraft()">💾 Save Data</button>
            <button class="btn btn-success" style="font-weight:700; font-size:0.95rem;" onclick="showTab('new-regime')">📄 Generate Statement (New Regime)</button>
            <button class="btn btn-primary" style="font-weight:700;" onclick="showTab('old-regime')">⚖️ Generate Statement (Old Regime)</button>
            <button class="btn btn-outline" onclick="exportJSON()">📥 Export JSON</button>
          </div>
        </div>
      </div>

    </div>

    <!-- ======================================================== -->
    <!-- VIEW 2: NEW REGIME STATEMENT (Single A4 Portrait Page)   -->
    <!-- Matches Prof. Rajesh K PDF Model Byte-for-Byte                -->
    <!-- ======================================================== -->
    <div id="new-regime-statement-view" style="display:none;">
      <div class="action-bar no-print">
        <button class="btn btn-outline" onclick="showTab('calculator')">⬅️ Back to Calculator</button>
        <button class="btn btn-success" onclick="downloadNewRegimePdf()" style="font-weight:700;">📥 Download A4 PDF (New Regime)</button>
        <button class="btn btn-outline" onclick="printNewRegimeStatement()">🖨️ Print Statement</button>
        <div style="flex-grow:1;"></div>
        <button class="btn btn-outline" onclick="exportJSON()" title="Export JSON backup">📥 Export JSON</button>
        <button class="btn btn-outline" onclick="showTab('form-10e')">📑 Form 10E (Sec 89)</button>
        <button class="btn btn-outline" onclick="showTab('old-regime')">⚖️ Old Regime</button>
      </div>

      <div class="print-page-wrapper">
      <div class="print-page">
                <div class="eco-stmt-container" id="ecostatt-single-page">
          
          <!-- Block 1: Document Header -->
          <div class="stmt-block stmt-block-header">
            <h1>Income Tax Statement for the Financial Year 2026-27</h1>
            <h2>(Assessment Year 2027-2028)</h2>
            <div style="font-size:7.5pt; color:#000; margin-bottom:3px;">to be furnished by the employees / officers whose income exceeds Rs. 2,50,000/-</div>
            <div>
              <span class="eco-mode-tag" id="eco-badge-mode">ANTICIPATORY STATEMENT</span>
              <span class="eco-mode-tag" style="background:#fff; color:#000; border:1px solid #000;">NEW REGIME (U/S 115BAC)</span>
            </div>
          </div>

          <!-- Block 2: Employee Information -->
          <div class="stmt-block">
            <table class="emp-table">
              <tr>
                <td class="lbl">Name:</td>
                <td class="val"><strong id="eco-emp-name"></strong></td>
                <td class="lbl">Designation:</td>
                <td class="val" id="eco-emp-desig"></td>
              </tr>
              <tr>
                <td class="lbl">PAN:</td>
                <td class="val"><strong id="eco-emp-pan"></strong></td>
                <td class="lbl">PEN:</td>
                <td class="val" id="eco-emp-pen"></td>
              </tr>
              <tr>
                <td class="lbl">Office:</td>
                <td class="val" colspan="3" id="eco-emp-office"></td>
              </tr>
            </table>
          </div>

          <!-- Block 3: Gross Salary & Monthly Breakdown -->
          <div class="stmt-block">
            <div class="block-title-row">
              <span>1. Gross Salary (Total):</span>
              <span id="eco-row1-main" style="font-size:9pt;">0</span>
            </div>
            <div class="block-body">
              <div style="font-size:7.5pt; margin-bottom:2px;"><em>(a) Monthly Gross Salary (March 2026 to February 2027):</em></div>
              <table class="grid-table">
                <thead>
                  <tr>
                    <th style="width:16.66%;">Mar</th>
                    <th style="width:16.66%;">Apr</th>
                    <th style="width:16.66%;">May</th>
                    <th style="width:16.66%;">Jun</th>
                    <th style="width:16.66%;">Jul</th>
                    <th style="width:16.66%;">Aug</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td id="m-mar">0</td>
                    <td id="m-apr">0</td>
                    <td id="m-may">0</td>
                    <td id="m-jun">0</td>
                    <td id="m-jul">0</td>
                    <td id="m-aug">0</td>
                  </tr>
                </tbody>
                <thead>
                  <tr>
                    <th>Sep</th>
                    <th>Oct</th>
                    <th>Nov</th>
                    <th>Dec</th>
                    <th>Jan</th>
                    <th>Feb</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td id="m-sep">0</td>
                    <td id="m-oct">0</td>
                    <td id="m-nov">0</td>
                    <td id="m-dec">0</td>
                    <td id="m-jan">0</td>
                    <td id="m-feb">0</td>
                  </tr>
                </tbody>
              </table>
              <div class="sub-row">
                <span>Subtotal of Monthly Gross Salary (a):</span>
                <strong id="eco-row1a">0</strong>
              </div>
              <div class="sub-row">
                <span>(b) Leave Surrender / Bonus / Arrears / Other:</span>
                <span id="eco-row1b">0</span>
              </div>
              <div class="sub-row">
                <span>(c) Excess pay refund / recovery:</span>
                <span id="eco-row1c">0</span>
              </div>
              <div class="sub-row sub-row-total">
                <span>Total Salary (a + b - c):</span>
                <span id="eco-row1-tot">0</span>
              </div>
            </div>
          </div>

          <!-- Block 4: Deductions under Section 16 & 80CCD(2) -->
          <div class="stmt-block">
            <div class="block-title-row">
              <span>2. Deductions under Section 16 & 80CCD(2):</span>
              <span id="eco-row2-main">75,000</span>
            </div>
            <div class="block-body">
              <div class="sub-row">
                <span>(a) Standard Deduction u/s 16(ia):</span>
                <span id="eco-row2a">75,000</span>
              </div>
              <div class="sub-row">
                <span>(b) Conveyance / Transport Allowance:</span>
                <span id="eco-row2b">0</span>
              </div>
              <div class="sub-row">
                <span>(c) Employer Contribution to NPS u/s 80CCD(2):</span>
                <span id="eco-row2c">0</span>
              </div>
              <div class="sub-row">
                <span>(d) Entertainment Allowance:</span>
                <span>0</span>
              </div>
              <div class="sub-row">
                <span>(e) Tax on Employment (Professional Tax):</span>
                <span id="eco-row2e">0</span>
              </div>
              <div class="sub-row sub-row-total">
                <span>Total Deductions (a + b + c + d + e):</span>
                <span id="eco-row2-sub">75,000</span>
              </div>
            </div>
          </div>

          <!-- Block 5: Taxable Income & Tax Computation -->
          <div class="stmt-block">
            <div class="block-title-row">
              <span>Taxable Income & Tax Computation:</span>
              <span>Amount (₹)</span>
            </div>
            <div class="block-body">
              <div class="sub-row">
                <span>3. Remuneration (Examination / Valuation / Other Income):</span>
                <span id="eco-row3-main">0</span>
              </div>
              <div class="sub-row sub-row-highlight">
                <span>4. Total Income rounded off to nearest Rs. 10/- [ (1 - 2) + 3 ]:</span>
                <strong id="eco-row4-main">0</strong>
              </div>
              <div class="sub-row">
                <span>5. Tax on Total Income (as per New Tax Slab FY 2026-27):</span>
                <span id="eco-row5-main">0</span>
              </div>
              <div class="sub-row">
                <span>6. Less: Rebate u/s 87A (Up to Rs. 60,000 if Total Income &le; Rs. 12,00,000):</span>
                <span id="eco-row6-main">0</span>
              </div>
              <div class="sub-row">
                <span>7. Income Tax after Rebate (5 - 6):</span>
                <span id="eco-row7-main">0</span>
              </div>
              <div class="sub-row">
                <span>8. Surcharge (if Total Income exceeds Rs. 50,00,000):</span>
                <span id="eco-row8-main">0</span>
              </div>
              <div class="sub-row">
                <span>9. Health and Education Cess @ 4% on (Tax + Surcharge):</span>
                <span id="eco-row9-main">0</span>
              </div>
              <div class="sub-row sub-row-total">
                <span>10. Total Tax Payable (7 + 8 + 9):</span>
                <strong id="eco-row10-main">0</strong>
              </div>
            </div>
          </div>

          <!-- Block 6: Arrear Relief u/s 89, TDS & Balance Tax Payable -->
          <div class="stmt-block">
            <div class="block-title-row">
              <span>Relief u/s 89, TDS & Balance Tax:</span>
              <span>Amount (₹)</span>
            </div>
            <div class="block-body">
              <div class="sub-row">
                <span>11. Less: Relief for arrears of salary u/s 89(1) (as per Form 10E):</span>
                <span id="eco-row11-main">0</span>
              </div>
              <div class="sub-row">
                <span>12. Balance Tax Payable (10 - 11):</span>
                <strong id="eco-row12-main">0</strong>
              </div>
              <div class="sub-row">
                <span>13. Income tax deducted from salary / Advance tax paid (TDS):</span>
                <span id="eco-row13-main">0</span>
              </div>
              <div class="sub-row sub-row-highlight" style="font-size:8.5pt;">
                <div>
                  <strong>14. Balance Income Tax to be paid (12 - 13):</strong>
                  <div style="font-size:7pt; font-weight:normal; color:#000;" id="eco-anticipatory-note">
                    (To be deducted @ ₹0 / month for 3 pending months)
                  </div>
                </div>
                <strong id="eco-row14-main" style="font-size:9.5pt;">0</strong>
              </div>
            </div>
          </div>

          <!-- Block 7: Declaration & Signatures (No Border, Generous Signing Space) -->
          <div class="stmt-block stmt-block-signature" style="border:none; margin-top:8px; padding:4px 2px;">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; font-size:7.5pt;">
              <div style="width:44%;">
                <p style="margin:2px 0;"><strong>Place:</strong> <span id="eco-sig-place"></span></p>
                <p style="margin:2px 0;"><strong>Date:</strong> <span id="eco-sig-date">23/11/2026</span></p>
                <div style="margin-top:36px; font-size:7.5pt; color:#000;">
                  <em>Verified that the particulars given above are true and correct.</em>
                </div>
              </div>
              <div style="width:54%; text-align:right;">
                <div style="margin-bottom:45px; padding-top:4px;">
                  <span>Signature: ________________________________</span>
                </div>
                <p style="margin:1.5px 0;"><strong>Name:</strong> <span id="eco-sig-name"></span></p>
                <p style="margin:1.5px 0;"><strong>PEN:</strong> <span id="eco-sig-pen"></span></p>
                <p style="margin:1.5px 0;"><strong>Designation:</strong> <span id="eco-sig-desig"></span></p>
                <p style="margin:1.5px 0;"><strong>Office:</strong> <span id="eco-sig-office"></span></p>
              </div>
            </div>
          </div>

        </div>
      </div>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- VIEW 3: DETAILED OLD REGIME STATEMENT                    -->
    <!-- ======================================================== -->
    <div id="old-regime-statement-view" style="display:none;">
      <div class="action-bar no-print">
        <button class="btn btn-outline" onclick="showTab('calculator')">⬅️ Back to Calculator</button>
        <button class="btn btn-success" onclick="downloadOldRegimePdf()" style="font-weight:700;">📥 Download A4 PDF (Old Regime)</button>
        <button class="btn btn-outline" onclick="printOldRegimeStatement()">🖨️ Print Statement</button>
        <div style="flex-grow:1;"></div>
        <button class="btn btn-outline" onclick="exportJSON()">📥 Export JSON</button>
        <button class="btn btn-outline" onclick="showTab('new-regime')">Switch to New Regime Statement</button>
      </div>

      <div class="print-page-wrapper">
        <div class="print-page">
                    <div class="eco-stmt-container" id="old-regime-single-page">
            
            <!-- Block 1: Header -->
            <div class="stmt-block stmt-block-header">
              <h1>Income Tax Statement for the Financial Year 2026-27</h1>
              <h2>(Assessment Year 2027-2028)</h2>
              <div style="font-size:7.5pt; color:#000; margin-bottom:3px;">Statement of Tax Computations under the OLD TAX REGIME (with Detailed Chapter VI-A Deductions)</div>
              <div>
                <span class="eco-mode-tag" id="old-badge-mode">ANTICIPATORY STATEMENT</span>
                <span class="eco-mode-tag" style="background:#fff; color:#000; border:1px solid #000;">OLD TAX REGIME</span>
              </div>
            </div>

            <!-- Block 2: Employee Information -->
            <div class="stmt-block">
              <table class="emp-table">
                <tr>
                  <td class="lbl">Name:</td>
                  <td class="val"><strong id="old-emp-name"></strong></td>
                  <td class="lbl">Designation:</td>
                  <td class="val" id="old-emp-desig"></td>
                </tr>
                <tr>
                  <td class="lbl">PAN:</td>
                  <td class="val"><strong id="old-emp-pan"></strong></td>
                  <td class="lbl">PEN:</td>
                  <td class="val" id="old-emp-pen"></td>
                </tr>
                <tr>
                  <td class="lbl">Office:</td>
                  <td class="val" colspan="3" id="old-emp-office"></td>
                </tr>
              </table>
            </div>

            <!-- Block 3: Gross Salary & Monthly Breakdown -->
            <div class="stmt-block">
              <div class="block-title-row">
                <span>1. Gross Salary (Total):</span>
                <span id="old-row1" style="font-size:9pt;">0</span>
              </div>
              <div class="block-body">
                <div style="font-size:7.5pt; margin-bottom:2px;"><em>(a) Monthly Gross Salary (March 2026 to February 2027):</em></div>
                <table class="grid-table">
                  <thead>
                    <tr>
                      <th style="width:16.66%;">Mar</th>
                      <th style="width:16.66%;">Apr</th>
                      <th style="width:16.66%;">May</th>
                      <th style="width:16.66%;">Jun</th>
                      <th style="width:16.66%;">Jul</th>
                      <th style="width:16.66%;">Aug</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td id="old-m-mar">0</td>
                      <td id="old-m-apr">0</td>
                      <td id="old-m-may">0</td>
                      <td id="old-m-jun">0</td>
                      <td id="old-m-jul">0</td>
                      <td id="old-m-aug">0</td>
                    </tr>
                  </tbody>
                  <thead>
                    <tr>
                      <th>Sep</th>
                      <th>Oct</th>
                      <th>Nov</th>
                      <th>Dec</th>
                      <th>Jan</th>
                      <th>Feb</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td id="old-m-sep">0</td>
                      <td id="old-m-oct">0</td>
                      <td id="old-m-nov">0</td>
                      <td id="old-m-dec">0</td>
                      <td id="old-m-jan">0</td>
                      <td id="old-m-feb">0</td>
                    </tr>
                  </tbody>
                </table>
                <div class="sub-row">
                  <span>Subtotal of Monthly Gross Salary (a):</span>
                  <strong id="old-row1a">0</strong>
                </div>
                <div class="sub-row">
                  <span>(b) Leave Surrender / Bonus / Arrears:</span>
                  <span id="old-row1b">0</span>
                </div>
                <div class="sub-row">
                  <span>(c) Excess pay refund / recovery:</span>
                  <span id="old-row1c">0</span>
                </div>
                <div class="sub-row sub-row-total">
                  <span>Total Salary (a + b - c):</span>
                  <span id="old-row1-tot">0</span>
                </div>
              </div>
            </div>

            <!-- Block 4: Deductions under Section 16 & Salary Income -->
            <div class="stmt-block">
              <div class="block-title-row">
                <span>2. Deductions under Section 16:</span>
                <span id="old-row2">50,000</span>
              </div>
              <div class="block-body">
                <div class="sub-row">
                  <span>(a) Standard Deduction u/s 16(ia):</span>
                  <span>50,000</span>
                </div>
                <div class="sub-row">
                  <span>(b) Tax on Employment (Professional Tax) u/s 16(iii):</span>
                  <span id="old-row2-pt">0</span>
                </div>
                <div class="sub-row sub-row-highlight">
                  <span>3. Income from Salary (1 - 2):</span>
                  <strong id="old-row3">0</strong>
                </div>
                <div class="sub-row">
                  <span>4. Remuneration (Examination / Valuation / Other Income):</span>
                  <span id="old-row4">0</span>
                </div>
                <div class="sub-row sub-row-total">
                  <span>5. Gross Total Income (GTI) (3 + 4):</span>
                  <strong id="old-row5">0</strong>
                </div>
              </div>
            </div>

            <!-- Block 5: Detailed Chapter VI-A Deductions Schedule -->
            <div class="stmt-block">
              <div class="block-title-row">
                <span>6. Deductions under Chapter VI-A:</span>
                <span id="old-row6">0</span>
              </div>
              <div class="block-body">
                <div style="border:1px solid #000; padding:3px 6px; margin-bottom:3px; font-size:7.5pt;">
                  <div style="font-weight:bold; margin-bottom:2px;">(A) Section 80C Deductions (Max Limit: Rs. 1,50,000):</div>
                  <div class="sub-row"><span>&bull; GPF / EPF Subscription:</span><span id="old-det-gpf">0</span></div>
                  <div class="sub-row"><span>&bull; SLI (State Life Insurance):</span><span id="old-det-sli">0</span></div>
                  <div class="sub-row"><span>&bull; GIS (Group Insurance Scheme):</span><span id="old-det-gis">0</span></div>
                  <div class="sub-row"><span>&bull; LIC / Life Insurance Premium:</span><span id="old-det-lic">0</span></div>
                  <div class="sub-row"><span>&bull; Tuition Fees for Children:</span><span id="old-det-tuition">0</span></div>
                  <div class="sub-row"><span>&bull; Housing Loan Principal Repayment:</span><span id="old-det-hlp">0</span></div>
                  <div class="sub-row"><span>&bull; PPF / Sukanya / NSC / Other 80C:</span><span id="old-det-ppf">0</span></div>
                  <div class="sub-row sub-row-total">
                    <span>Total 80C Claimed / Eligible Amount:</span>
                    <span><span id="old-80c-claimed">0</span> / <span id="old-80c">0</span></span>
                  </div>
                </div>
                <div class="sub-row"><span>(B) u/s 80CCD(1B) - Additional NPS Contribution (Max 50k):</span><span id="old-80ccd">0</span></div>
                <div class="sub-row"><span>(C) u/s 80D - Health Insurance / MediSep (Self & Parents):</span><span id="old-80d">0</span></div>
                <div class="sub-row"><span>(D) u/s 24(b) - Interest on Housing Loan (Max 2L):</span><span id="old-24b">0</span></div>
                <div class="sub-row"><span>(E) u/s 80E - Interest on Higher Education Loan:</span><span id="old-80e">0</span></div>
                <div class="sub-row"><span>(F) u/s 80G - Approved Donations (CMDRF / PMNRF):</span><span id="old-80g">0</span></div>
                <div class="sub-row"><span>(G) u/s 80TTA - Savings Bank Interest:</span><span id="old-80tta">0</span></div>
              </div>
            </div>

            <!-- Block 6: Taxable Income & Tax Computation -->
            <div class="stmt-block">
              <div class="block-title-row">
                <span>Taxable Income & Tax Computation:</span>
                <span>Amount (₹)</span>
              </div>
              <div class="block-body">
                <div class="sub-row sub-row-highlight">
                  <span>7. Total Taxable Income rounded off to nearest Rs. 10/- (5 - 6):</span>
                  <strong id="old-row7">0</strong>
                </div>
                <div class="sub-row">
                  <span>8. Tax on Total Income (Old Slabs: 0-2.5L Nil, 2.5-5L 5%, 5-10L 20%, >10L 30%):</span>
                  <span id="old-row8">0</span>
                </div>
                <div class="sub-row">
                  <span>9. Less: Rebate u/s 87A (Up to Rs. 12,500 if Total Income &le; Rs. 5,00,000):</span>
                  <span id="old-row9">0</span>
                </div>
                <div class="sub-row">
                  <span>10. Income Tax after Rebate (8 - 9):</span>
                  <span id="old-row10">0</span>
                </div>
                <div class="sub-row">
                  <span>11. Health and Education Cess @ 4%:</span>
                  <span id="old-row11">0</span>
                </div>
                <div class="sub-row sub-row-total">
                  <span>12. Total Tax Payable (10 + 11):</span>
                  <strong id="old-row12">0</strong>
                </div>
              </div>
            </div>

            <!-- Block 7: Relief u/s 89, TDS & Balance Tax Payable -->
            <div class="stmt-block">
              <div class="block-title-row">
                <span>Relief u/s 89, TDS & Balance Tax:</span>
                <span>Amount (₹)</span>
              </div>
              <div class="block-body">
                <div class="sub-row">
                  <span>13. Less: Relief for arrears of salary u/s 89(1) (from Form 10E):</span>
                  <span id="old-row13">0</span>
                </div>
                <div class="sub-row">
                  <span>14. Income Tax deducted from salary (TDS) / Advance tax paid:</span>
                  <span id="old-row14">0</span>
                </div>
                <div class="sub-row sub-row-highlight" style="font-size:8.5pt;">
                  <div>
                    <strong>15. Balance Income Tax to be paid (12 - 13 - 14):</strong>
                    <div style="font-size:7pt; font-weight:normal;" id="old-anticipatory-note"></div>
                  </div>
                  <strong id="old-row15" style="font-size:9.5pt;">0</strong>
                </div>
              </div>
            </div>

            <!-- Block 8: Declaration & Signatures (No Border, Generous Signing Space) -->
            <div class="stmt-block stmt-block-signature" style="border:none; margin-top:8px; padding:4px 2px;">
              <div style="display:flex; justify-content:space-between; align-items:flex-start; font-size:7.5pt;">
                <div style="width:44%;">
                  <p style="margin:2px 0;"><strong>Place:</strong> <span id="old-sig-place"></span></p>
                  <p style="margin:2px 0;"><strong>Date:</strong> <span id="old-sig-date"></span></p>
                  <div style="margin-top:36px; font-size:7.5pt; color:#000;">
                    <em>Verified that the particulars given above are true and correct.</em>
                  </div>
                </div>
                <div style="width:54%; text-align:right;">
                  <div style="margin-bottom:45px; padding-top:4px;">
                    <span>Signature: ________________________________</span>
                  </div>
                  <p style="margin:1.5px 0;"><strong>Name:</strong> <span id="old-sig-name"></span></p>
                  <p style="margin:1.5px 0;"><strong>PEN:</strong> <span id="old-sig-pen"></span></p>
                  <p style="margin:1.5px 0;"><strong>Designation:</strong> <span id="old-sig-desig"></span></p>
                  <p style="margin:1.5px 0;"><strong>Office:</strong> <span id="old-sig-office"></span></p>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- VIEW 4: FORM 10E (SECTION 89(1) ARREAR RELIEF)           -->
    <!-- Matching ecostatt.com/income-tax/.../form10e-calculation -->
    <!-- ======================================================== -->
    <div id="form-10e-view" style="display:none;">

      <div class="action-bar no-print">
        <button class="btn btn-success" onclick="downloadForm10EPdf()">📥 Download Form 10E (A4 PDF)</button>
        <button class="btn btn-primary" onclick="showTab('calculator')">⬅️ Back to Calculator</button>
        <button class="btn btn-success" onclick="apply10eToStatement()">⚡ Apply Relief to Statement (Row 11)</button>
        <button class="btn btn-secondary" onclick="printForm10E()">🖨️ Print Form 10E & Table A</button>
        <button class="btn btn-outline" onclick="loadSample10E()">💡 Load Sample Arrears</button>
        <button class="btn btn-danger" onclick="clear10EData()">🔄 Clear 10E</button>
      </div>

      <!-- Information Banner -->
      <div class="card no-print-10e" style="background:#eff6ff; border:1px solid #bfdbfe;">
        <h3 style="color:#1e3a8a; font-size:1.1rem; margin-bottom:6px;">📑 Form 10E: Calculation of Relief under Section 89(1)</h3>
        <p style="font-size:0.875rem; color:#334155;">
          When an employee receives salary in arrears (such as DA arrears, pay revision arrears, or increments) relating to previous financial years, tax is calculated in the year of receipt at current rates. Relief u/s 89(1) ensures the employee pays no extra tax than what would have been paid if the salary had been received in the respective previous year(s).
        </p>
        <div style="margin-top:8px; font-size:0.825rem; color:#1e40af; font-weight:600;">
          💡 Rule: Total Arrears received in FY 2026-27 is currently set to: <span id="f10e-cur-arrear-tag" style="background:#fff; padding:2px 8px; border-radius:4px; border:1px solid #93c5fd;">₹0</span>
        </div>
      </div>

      <!-- Previous Year Data Entry Card -->
      <div class="card no-print-10e">
        <div class="card-title">
          <span>➕ Add Previous Financial Year's Arrears</span>
          <span style="font-size:0.8rem; color:#64748b;">(Select each historical FY to which arrears relate)</span>
        </div>

        <div class="grid-4" style="align-items:end;">
          <div class="form-group">
            <label for="f10e-sel-year">Financial Year</label>
            <select class="form-control" id="f10e-sel-year" onchange="onYearSelectionChange()" style="font-weight:600;">
              <option value="2025 - 26">2025 - 26 (AY 2026-27)</option>
              <option value="2024 - 25" selected>2024 - 25 (AY 2025-26)</option>
              <option value="2023 - 24">2023 - 24 (AY 2024-25)</option>
              <option value="2022 - 23">2022 - 23 (AY 2023-24)</option>
              <option value="2021 - 22">2021 - 22 (AY 2022-23)</option>
              <option value="2020 - 21">2020 - 21 (AY 2021-22)</option>
              <option value="2019 - 20">2019 - 20 (AY 2020-21)</option>
              <option value="2018 - 19">2018 - 19 (AY 2019-20)</option>
              <option value="2017 - 18">2017 - 18 (AY 2018-19)</option>
              <option value="2016 - 17">2016 - 17 (AY 2017-18)</option>
              <option value="2015 - 16">2015 - 16 (AY 2016-17)</option>
              <option value="2014 - 15">2014 - 15 (AY 2015-16)</option>
              <option value="2013 - 14">2013 - 14 (AY 2014-15)</option>
              <option value="2012 - 13">2012 - 13 (AY 2013-14)</option>
              <option value="2011 - 12">2011 - 12 (AY 2012-13)</option>
              <option value="2010 - 11">2010 - 11 (AY 2011-12)</option>
            </select>
          </div>

          <div class="form-group">
            <label for="f10e-input-income">Taxable Income (without arrears) (₹)</label>
            <input type="number" class="form-control" id="f10e-input-income" placeholder="e.g. 750000" value="750000">
          </div>

          <div class="form-group">
            <label for="f10e-input-arrear">Arrears relating to this FY (₹)</label>
            <input type="number" class="form-control" id="f10e-input-arrear" placeholder="e.g. 80000" value="80000">
          </div>

          <div class="form-group">
            <label for="f10e-input-age">Age Category</label>
            <select class="form-control" id="f10e-input-age">
              <option value="Individual" selected>Individual (< 60 yrs)</option>
              <option value="Senior Citizen">Senior Citizen (60 - 79 yrs)</option>
              <option value="Super Senior Citizen">Super Senior (80+ yrs)</option>
            </select>
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:10px; flex-wrap:wrap; gap:10px;">
          <div style="display:flex; align-items:center; gap:16px;">
            <label style="font-weight:600; font-size:0.875rem;">Tax Regime for that FY:</label>
            <label><input type="radio" name="f10e-taxslab" id="f10e-regime-old" value="OLD" checked> OLD Regime</label>
            <label id="f10e-regime-new-wrap"><input type="radio" name="f10e-taxslab" id="f10e-regime-new" value="NEW"> NEW Regime (u/s 115BAC)</label>
          </div>
          <div>
            <button class="btn btn-primary" onclick="addPreviousYearEntry()">➕ ADD TO TABLE A</button>
          </div>
        </div>
      </div>

      <!-- Printable Form 10E & Table A Document -->
      <div class="print-page-wrapper">
      <div class="print-page">
        <div class="eco-stmt-container" id="form-10e-single-page">

          <!-- Header -->
          <div class="eco-header">
            <h1 style="font-size:12pt;">FORM NO. 10E</h1>
            <p style="font-size:8pt; font-style:normal;">[See rule 21AA]</p>
            <h2 style="font-size:9pt; margin:4px 0;">Form for furnishing particulars of income for claiming relief under section 89(1) of the Income-tax Act, 1961</h2>
          </div>

          <!-- Employee Particulars -->
          <table class="eco-emp-box" style="margin-bottom:8px;">
            <tr>
              <td class="label">1. Name of Employee:</td><td class="val"><strong id="f10e-disp-name"></strong></td>
              <td class="label">2. PAN:</td><td class="val"><strong id="f10e-disp-pan"></strong></td>
            </tr>
            <tr>
              <td class="label">3. Designation:</td><td class="val" id="f10e-disp-desig"></td>
              <td class="label">4. PEN:</td><td class="val" id="f10e-disp-pen"></td>
            </tr>
            <tr>
              <td class="label">5. Office / Address:</td><td class="val" colspan="3" id="f10e-disp-office"></td>
            </tr>
            <tr>
              <td class="label">6. Assessment Year:</td><td class="val"><strong>2027 - 2028</strong></td>
              <td class="label">7. Financial Year:</td><td class="val"><strong>2026 - 2027</strong></td>
            </tr>
          </table>

          <!-- ANNEXURE I: Statutory Section 89(1) Relief Computation Summary -->
          <div style="font-size:8.5pt; font-weight:bold; margin:6px 0 3px 0; background:#fff; padding:3px 6px; border:1px solid #000; color:#000;">
            ANNEXURE - I : Computation of Relief under Section 89(1) on Salary received in Arrears
          </div>

          <table class="eco-table">
            <thead>
              <tr>
                <th style="width:6%;">Sl.</th>
                <th style="text-align:left; width:74%;">Particulars</th>
                <th style="width:20%;">Amount (₹)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1</td>
                <td>Total Income of Current Financial Year (FY 2026-27) <strong>including Arrears</strong></td>
                <td class="eco-col-amt" id="f10e-step1-inc">0</td>
              </tr>
              <tr>
                <td>2</td>
                <td>Tax on Total Income as per item 1 (including cess)</td>
                <td class="eco-col-amt" id="f10e-step1-tax">0</td>
              </tr>
              <tr>
                <td>3</td>
                <td>Total Income of Current Financial Year (FY 2026-27) <strong>excluding Arrears</strong></td>
                <td class="eco-col-amt" id="f10e-step2-inc">0</td>
              </tr>
              <tr>
                <td>4</td>
                <td>Tax on Total Income as per item 3 (including cess)</td>
                <td class="eco-col-amt" id="f10e-step2-tax">0</td>
              </tr>
              <tr style="font-weight:bold;">
                <td>5</td>
                <td><strong>Tax on Arrears in Current Year (FY 2026-27) [ Item 2 - Item 4 ] (A)</strong></td>
                <td class="eco-col-amt"><strong id="f10e-tax-cur-arrear" style="color:#000;">0</strong></td>
              </tr>
              <tr>
                <td>6</td>
                <td>Total Tax on Total Income of Previous Years <strong>including Arrears</strong> (Sum of Col 7 of Table A)</td>
                <td class="eco-col-amt" id="f10e-prev-with-tax">0</td>
              </tr>
              <tr>
                <td>7</td>
                <td>Total Tax on Total Income of Previous Years <strong>excluding Arrears</strong> (Sum of Col 6 of Table A)</td>
                <td class="eco-col-amt" id="f10e-prev-without-tax">0</td>
              </tr>
              <tr style="font-weight:bold;">
                <td>8</td>
                <td><strong>Total Tax on Arrears in Previous Years [ Item 6 - Item 7 ] (B)</strong></td>
                <td class="eco-col-amt"><strong id="f10e-tax-prev-arrear" style="color:#000;">0</strong></td>
              </tr>
              <tr style="background:#fff; font-weight:bold; font-size:9.5pt; border:2px solid #000; color:#000;">
                <td>9</td>
                <td>
                  <strong>RELIEF UNDER SECTION 89(1) [ Item 5 - Item 8 ] (A - B)</strong>
                  <div style="font-size:7pt; font-weight:normal; color:#000;">(Transferred to Row 11 of Income Tax Statement)</div>
                </td>
                <td class="eco-col-amt"><strong id="f10e-final-relief" style="color:#000; font-size:11pt;">0</strong></td>
              </tr>
            </tbody>
          </table>

          <!-- TABLE A -->
          <div style="font-size:8.5pt; font-weight:bold; margin:10px 0 3px 0; background:#fff; padding:3px 6px; border:1px solid #000; color:#000; display:flex; justify-content:space-between; align-items:center;">
            <span>TABLE "A" : Details of Previous Financial Years' Tax and Arrear Computations</span>
            <span style="font-size:7.5pt; font-weight:normal;">[See rule 21AA(2)(a)]</span>
          </div>

          <table class="eco-table" id="table-a-grid">
            <thead>
              <tr style="background:#fff;">
                <th style="width:4%;">Sl.</th>
                <th style="width:14%;">Financial Year</th>
                <th style="width:13%;">Taxable Income (without arrear)<br>(₹)</th>
                <th style="width:12%;">Arrears Received<br>(₹)</th>
                <th style="width:13%;">Total Income [with arrear]<br>(₹)</th>
                <th style="width:13%;">Tax on Income without arrear<br>(₹)</th>
                <th style="width:13%;">Tax on Income with arrear<br>(₹)</th>
                <th style="width:12%;">Difference in Tax<br>(₹)</th>
                <th style="width:6%;" class="no-print-10e">Action</th>
              </tr>
              <tr style="background:#fff; font-size:7pt; text-align:center;">
                <th>(1)</th><th>(2)</th><th>(3)</th><th>(4)</th><th>(5)</th><th>(6)</th><th>(7)</th><th>(8)</th><th class="no-print-10e">-</th>
              </tr>
            </thead>
            <tbody id="table-a-body">
              <!-- Dynamically rendered -->
            </tbody>
            <tfoot>
              <tr style="background:#fff; font-weight:bold;">
                <td colspan="3" style="text-align:right;">Total:</td>
                <td id="tbla-tot-arrear" style="text-align:right;">0</td>
                <td></td>
                <td id="tbla-tot-tax-wo" style="text-align:right;">0</td>
                <td id="tbla-tot-tax-w" style="text-align:right;">0</td>
                <td id="tbla-tot-diff" style="text-align:right; color:#000;">0</td>
                <td class="no-print-10e"></td>
              </tr>
            </tfoot>
          </table>

          <!-- Verification statement -->
          <div style="margin-top:14px; font-size:8pt; line-height:1.4;">
            <p>
              I, <strong id="f10e-ver-name"></strong>, do hereby declare that what is stated above is true to the best of my information and belief.
            </p>
            <div style="display:flex; justify-content:space-between; margin-top:20px;">
              <div>
                <p><strong>Place:</strong> <span id="f10e-ver-place"></span></p>
                <p><strong>Date:</strong> <span id="f10e-ver-date">23/11/2026</span></p>
              </div>
              <div style="text-align:right;">
                <p>Signature: __________________________</p>
                <p><strong>Name:</strong> <span id="f10e-ver-name2"></span></p>
                <p><strong>Designation:</strong> <span id="f10e-ver-desig"></span></p>
              </div>
            </div>
          </div>

        </div>
      </div>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- VIEW 5: TAX SLABS REFERENCE FY 2026-27                   -->
    <!-- ======================================================== -->
    <div id="tax-slabs-view" style="display:none;">
      <div class="action-bar no-print">
        <button class="btn btn-primary" onclick="showTab('calculator')">⬅️ Back to Calculator</button>
      </div>

      <div class="card">
        <div class="card-title">📖 Tax Slabs Comparison for FY 2026-27 (AY 2027-28)</div>
        <div class="grid-2">
          
          <!-- New Regime Slabs -->
          <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:15px;">
            <h4 style="color:#15803d; margin-bottom:10px;">🌟 New Tax Regime (Section 115BAC)</h4>
            <ul style="font-size:0.875rem; line-height:1.6; margin-left:20px; color:#1e293b;">
              <li><strong>Standard Deduction:</strong> ₹75,000 (Salaried / Pensioners)</li>
              <li><strong>₹0 to ₹4,00,000:</strong> Nil</li>
              <li><strong>₹4,00,001 to ₹8,00,000:</strong> 5%</li>
              <li><strong>₹8,00,001 to ₹12,00,000:</strong> 10%</li>
              <li><strong>₹12,00,001 to ₹16,00,000:</strong> 15%</li>
              <li><strong>₹16,00,001 to ₹20,00,000:</strong> 20%</li>
              <li><strong>₹20,00,001 to ₹24,00,000:</strong> 25%</li>
              <li><strong>Above ₹24,00,000:</strong> 30%</li>
              <li><strong>Rebate u/s 87A:</strong> Full tax rebate up to ₹60,000 for Taxable Income up to ₹12,00,000 (Zero tax up to ₹12,75,000 gross). Marginal relief applies if income is slightly above ₹12 Lakh.</li>
              <li><strong>Health & Education Cess:</strong> 4%</li>
            </ul>
          </div>

          <!-- Old Regime Slabs -->
          <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:6px; padding:15px;">
            <h4 style="color:#0f172a; margin-bottom:10px;">🏛️ Old Tax Regime</h4>
            <ul style="font-size:0.875rem; line-height:1.6; margin-left:20px; color:#1e293b;">
              <li><strong>Standard Deduction:</strong> ₹50,000</li>
              <li><strong>₹0 to ₹2,50,000:</strong> Nil (Senior: ₹3L, Super Senior: ₹5L)</li>
              <li><strong>₹2,50,001 to ₹5,00,000:</strong> 5%</li>
              <li><strong>₹5,00,001 to ₹10,00,000:</strong> 20%</li>
              <li><strong>Above ₹10,00,000:</strong> 30%</li>
              <li><strong>Rebate u/s 87A:</strong> Up to ₹12,500 if Taxable Income &le; ₹5,00,000.</li>
              <li><strong>Deductions allowed:</strong> 80C (up to 1.5L), 80CCD(1B) (50k), 80D (health ins), 24(b) (home loan int 2L), 80E, 80G.</li>
              <li><strong>Health & Education Cess:</strong> 4%</li>
            </ul>
          </div>

        </div>
      </div>
    </div>

  </div> <!-- /container -->

  <script>
    // --- Data Model & State ---
    const months = [
      { key: 'mar', name: 'March 2026', short: 'Mar' },
      { key: 'apr', name: 'April 2026', short: 'Apr' },
      { key: 'may', name: 'May 2026', short: 'May' },
      { key: 'jun', name: 'June 2026', short: 'Jun' },
      { key: 'jul', name: 'July 2026', short: 'Jul' },
      { key: 'aug', name: 'August 2026', short: 'Aug' },
      { key: 'sep', name: 'September 2026', short: 'Sep' },
      { key: 'oct', name: 'October 2026', short: 'Oct' },
      { key: 'nov', name: 'November 2026', short: 'Nov' },
      { key: 'dec', name: 'December 2026', short: 'Dec' },
      { key: 'jan', name: 'January 2027', short: 'Jan' },
      { key: 'feb', name: 'February 2027', short: 'Feb' }
    ];

    // Form 10E previous years list (Empty by default)
    let tableAEntries = [];

    // Initialize salary table inputs
    function initSalaryTable() {
      const tbody = document.getElementById('salary-table-body');
      tbody.innerHTML = '';
      months.forEach((m, idx) => {
        const tr = document.createElement('tr');
        const isLast = idx === months.length - 1;
        const copyBtnHtml = isLast ? 
          `<span style="color:#94a3b8; font-size:0.75rem;">(Last)</span>` : 
          `<button type="button" class="btn btn-outline" style="padding:2px 8px; font-size:0.75rem; background:#eff6ff; color:#1d4ed8; border-color:#93c5fd; white-space:nowrap;" onclick="copyMonthDown(${idx})" title="Copy ${m.name} values down to remaining months">⬇️ Copy Down</button>`;

        tr.innerHTML = `
          <td data-label="Month" style="text-align:left; font-weight:600;">${m.name}</td>
          <td data-label="Basic Pay + DA"><input type="number" class="form-control m-basic" id="basic-${m.key}" value="0" oninput="calculateAll()"></td>
          <td data-label="Other Allowances"><input type="number" class="form-control m-allow" id="allow-${m.key}" value="0" oninput="calculateAll()"></td>
          <td data-label="Monthly Gross" style="font-weight:700; color:#1e3a8a;" id="m-tot-${m.key}">0</td>
          <td data-label="PF / NPS Deducted"><input type="number" class="form-control m-pf" id="pf-${m.key}" value="0" oninput="calculateAll()"></td>
          <td data-label="Tax Deducted (TDS)"><input type="number" class="form-control m-tds" id="tds-${m.key}" value="0" oninput="calculateAll()"></td>
          <td data-label="Action" style="text-align:center;">${copyBtnHtml}</td>
        `;
        tbody.appendChild(tr);
      });
    }

    // Number helpers
    function getNum(id) {
      const el = document.getElementById(id);
      if (!el) return 0;
      const v = parseFloat(el.value);
      return isNaN(v) ? 0 : v;
    }

    function setNum(id, val) {
      const el = document.getElementById(id);
      if (el) el.value = Math.round(val);
    }

    function setText(id, text) {
      const el = document.getElementById(id);
      if (el) el.textContent = text;
    }

    function formatINR(val) {
      return Math.round(val || 0).toLocaleString('en-IN');
    }

    // Tab Navigation
    function showTab(tab) {
      const tabs = ['calculator', 'new-regime', 'old-regime', 'form-10e', 'slabs'];
      tabs.forEach(t => {
        const btn = document.getElementById('tab-' + t);
        if (btn) btn.classList.remove('active');
        const view = document.getElementById(t === 'calculator' ? 'calculator-form-view' :
                             t === 'new-regime' ? 'new-regime-statement-view' :
                             t === 'old-regime' ? 'old-regime-statement-view' :
                             t === 'form-10e' ? 'form-10e-view' : 'tax-slabs-view');
        if (view) view.style.display = 'none';
      });

      const activeBtn = document.getElementById('tab-' + tab);
      if (activeBtn) activeBtn.classList.add('active');

      const activeView = document.getElementById(tab === 'calculator' ? 'calculator-form-view' :
                                tab === 'new-regime' ? 'new-regime-statement-view' :
                                tab === 'old-regime' ? 'old-regime-statement-view' :
                                tab === 'form-10e' ? 'form-10e-view' : 'tax-slabs-view');
      if (activeView) activeView.style.display = 'block';

      if (tab === 'form-10e') {
        renderTableA();
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // --- Slabs and Calculations for FY 2026-27 ---

    // New Regime Tax Computation for FY 2026-27 (AY 2027-28)
    function computeNewRegimeTax(taxableIncome) {
      let income = Math.max(0, taxableIncome);
      let tax = 0;

      // Slabs: 0-4L Nil, 4-8L 5%, 8-12L 10%, 12-16L 15%, 16-20L 20%, 20-24L 25%, >24L 30%
      if (income > 400000) tax += Math.min(income - 400000, 400000) * 0.05;
      if (income > 800000) tax += Math.min(income - 800000, 400000) * 0.10;
      if (income > 1200000) tax += Math.min(income - 1200000, 400000) * 0.15;
      if (income > 1600000) tax += Math.min(income - 1600000, 400000) * 0.20;
      if (income > 2000000) tax += Math.min(income - 2000000, 400000) * 0.25;
      if (income > 2400000) tax += (income - 2400000) * 0.30;

      // Section 87A Rebate
      let rebate = 0;
      if (income <= 1200000) {
        rebate = Math.min(tax, 60000);
      } else if (income > 1200000 && income <= 1275000) {
        // Marginal relief: Tax payable cannot exceed excess income over 12 Lakhs
        let excess = income - 1200000;
        if (tax > excess) {
          rebate = tax - excess;
        }
      }

      let taxAfterRebate = Math.max(0, tax - rebate);

      // Surcharge
      let surcharge = 0;
      if (income > 50000000) surcharge = taxAfterRebate * 0.25;
      else if (income > 20000000) surcharge = taxAfterRebate * 0.25;
      else if (income > 10000000) surcharge = taxAfterRebate * 0.15;
      else if (income > 5000000) surcharge = taxAfterRebate * 0.10;

      let cess = Math.round((taxAfterRebate + surcharge) * 0.04);
      let totalTax = Math.round(taxAfterRebate + surcharge + cess);

      return { tax: Math.round(tax), rebate: Math.round(rebate), taxAfterRebate: Math.round(taxAfterRebate), surcharge: Math.round(surcharge), cess, totalTax };
    }

    // Old Regime Tax Computation for FY 2026-27 (AY 2027-28)
    function computeOldRegimeTax(taxableIncome, age = 'Individual') {
      let income = Math.max(0, taxableIncome);
      let exemption = age === 'Super Senior Citizen' ? 500000 : (age === 'Senior Citizen' ? 300000 : 250000);
      let tax = 0;

      if (income > exemption) tax += Math.min(income - exemption, 500000 - exemption) * 0.05;
      if (income > 500000) tax += Math.min(income - 500000, 500000) * 0.20;
      if (income > 1000000) tax += (income - 1000000) * 0.30;

      let rebate = 0;
      if (income <= 500000) {
        rebate = Math.min(tax, 12500);
      }

      let taxAfterRebate = Math.max(0, tax - rebate);

      let surcharge = 0;
      if (income > 50000000) surcharge = taxAfterRebate * 0.37;
      else if (income > 20000000) surcharge = taxAfterRebate * 0.25;
      else if (income > 10000000) surcharge = taxAfterRebate * 0.15;
      else if (income > 5000000) surcharge = taxAfterRebate * 0.10;

      let cess = Math.round((taxAfterRebate + surcharge) * 0.04);
      let totalTax = Math.round(taxAfterRebate + surcharge + cess);

      return { tax: Math.round(tax), rebate: Math.round(rebate), taxAfterRebate: Math.round(taxAfterRebate), surcharge: Math.round(surcharge), cess, totalTax };
    }

    // --- Historical Tax Computation for Previous Financial Years (FY 2010-11 to 2025-26) ---
    function computeHistoricalTax(yearStr, income, age = 'Individual', regime = 'OLD') {
      income = Math.max(0, parseFloat(income || 0));
      if (income <= 0) return { tax: 0, rebate: 0, cess: 0, totalTax: 0 };

      const startYear = parseInt(yearStr.split('-')[0].trim());
      let tax = 0;
      let rebate = 0;
      let surcharge = 0;
      const cessRate = startYear >= 2018 ? 0.04 : 0.03;

      if (regime === 'NEW' && startYear >= 2020) {
        if (startYear >= 2020 && startYear <= 2022) {
          if (income > 250000) tax += Math.min(income - 250000, 250000) * 0.05;
          if (income > 500000) tax += Math.min(income - 500000, 250000) * 0.10;
          if (income > 750000) tax += Math.min(income - 750000, 250000) * 0.15;
          if (income > 1000000) tax += Math.min(income - 1000000, 250000) * 0.20;
          if (income > 1250000) tax += Math.min(income - 1250000, 250000) * 0.25;
          if (income > 1500000) tax += (income - 1500000) * 0.30;
          if (income <= 500000) rebate = Math.min(tax, 12500);
        } else if (startYear === 2023) {
          if (income > 300000) tax += Math.min(income - 300000, 300000) * 0.05;
          if (income > 600000) tax += Math.min(income - 600000, 300000) * 0.10;
          if (income > 900000) tax += Math.min(income - 900000, 300000) * 0.15;
          if (income > 1200000) tax += Math.min(income - 1200000, 300000) * 0.20;
          if (income > 1500000) tax += (income - 1500000) * 0.30;
          if (income <= 700000) rebate = tax;
          else if (income > 700000 && tax > (income - 700000)) tax = income - 700000;
        } else if (startYear >= 2024) {
          if (income > 300000) tax += Math.min(income - 300000, 400000) * 0.05;
          if (income > 700000) tax += Math.min(income - 700000, 300000) * 0.10;
          if (income > 1000000) tax += Math.min(income - 1000000, 200000) * 0.15;
          if (income > 1200000) tax += Math.min(income - 1200000, 300000) * 0.20;
          if (income > 1500000) tax += (income - 1500000) * 0.30;
          if (income <= 700000) rebate = tax;
          else if (income > 700000 && tax > (income - 700000)) tax = income - 700000;
        }
      } else {
        // OLD Regime
        let exemption = 250000;
        if (age === 'Senior Citizen') exemption = startYear >= 2014 ? 300000 : (startYear >= 2011 ? 250000 : 240000);
        else if (age === 'Super Senior Citizen') exemption = 500000;
        else {
          if (startYear === 2010) exemption = 160000;
          else if (startYear === 2011) exemption = 180000;
          else if (startYear <= 2013) exemption = 200000;
          else exemption = 250000;
        }

        if (startYear <= 2011) {
          if (income > exemption) tax += Math.min(income - exemption, 500000 - exemption) * 0.10;
          if (income > 500000) tax += Math.min(income - 500000, 300000) * 0.20;
          if (income > 800000) tax += (income - 800000) * 0.30;
        } else if (startYear <= 2016) {
          if (income > exemption) tax += Math.min(income - exemption, 500000 - exemption) * 0.10;
          if (income > 500000) tax += Math.min(income - 500000, 500000) * 0.20;
          if (income > 1000000) tax += (income - 1000000) * 0.30;
          if (startYear >= 2013 && startYear <= 2015 && income <= 500000) rebate = Math.min(tax, 2000);
          else if (startYear === 2016 && income <= 500000) rebate = Math.min(tax, 5000);
        } else {
          // 2017 to 2025
          if (income > exemption) tax += Math.min(income - exemption, 500000 - exemption) * 0.05;
          if (income > 500000) tax += Math.min(income - 500000, 500000) * 0.20;
          if (income > 1000000) tax += (income - 1000000) * 0.30;
          if (startYear <= 2018 && income <= 350000) rebate = Math.min(tax, 2500);
          else if (startYear >= 2019 && income <= 500000) rebate = Math.min(tax, 12500);
        }
      }

      let taxAfterRebate = Math.max(0, tax - rebate);

      // Surcharge
      if (income > 50000000) surcharge = taxAfterRebate * (regime === 'NEW' && startYear >= 2023 ? 0.25 : 0.37);
      else if (income > 20000000) surcharge = taxAfterRebate * 0.25;
      else if (income > 10000000) surcharge = taxAfterRebate * 0.15;
      else if (income > 5000000) surcharge = taxAfterRebate * 0.10;

      let cess = Math.round((taxAfterRebate + surcharge) * cessRate);
      let totalTax = Math.round(taxAfterRebate + surcharge + cess);

      return { tax: Math.round(tax), rebate: Math.round(rebate), taxAfterRebate: Math.round(taxAfterRebate), surcharge: Math.round(surcharge), cess, totalTax };
    }

    // Main Calculator and DOM sync
    function calculateAll() {
      // 1. Monthly Salaries
      let totBasic = 0, totAllow = 0, totGross = 0, totPf = 0, totTds = 0;
      months.forEach(m => {
        let b = getNum('basic-' + m.key);
        let a = getNum('allow-' + m.key);
        let pf = getNum('pf-' + m.key);
        let tds = getNum('tds-' + m.key);
        let mTot = b + a;

        totBasic += b;
        totAllow += a;
        totGross += mTot;
        totPf += pf;
        totTds += tds;

        setText('m-tot-' + m.key, formatINR(mTot));
        setText('m-' + m.key, formatINR(mTot));
      });

      setText('tot-basic', formatINR(totBasic));
      setText('tot-allow', formatINR(totAllow));
      setText('tot-gross', formatINR(totGross));
      setText('tot-pf', formatINR(totPf));
      setText('tot-tds', formatINR(totTds));

      // 2. Additional Income & Row 1 Items
      let surrender = getNum('row1b-surrender');
      let bonus = getNum('row1b-bonus');
      let arrears = getNum('row1b-arrears');
      let otherInc = getNum('row1b-other');
      let row1bTotal = surrender + bonus + arrears + otherInc;

      let row1cExcess = getNum('row1c-excess');
      let row1GrossSalary = Math.max(0, totGross + row1bTotal - row1cExcess);

      // Row 2 Deductions (New Regime)
      let row2aStdDed = 75000;
      let row2bConvey = getNum('row2b-conveyance');
      let row2cNps = getNum('row2c-nps');
      let row2eProfTax = getNum('row2e-proftax');
      let row2TotDedNew = row2aStdDed + row2bConvey + row2cNps + row2eProfTax;

      // Row 3 Remuneration
      let row3Remun = getNum('row3-remuneration');

      // Row 4 Total Income New Regime (Rounded to nearest 10)
      let rawIncomeNew = Math.max(0, row1GrossSalary - row2TotDedNew + row3Remun);
      let row4TotalIncomeNew = Math.round(rawIncomeNew / 10) * 10;

      // Row 5-10 New Regime Taxes
      let newTaxObj = computeNewRegimeTax(row4TotalIncomeNew);
      let row11Relief89 = getNum('row11-relief89');
      let row12BalanceTaxPayable = Math.max(0, newTaxObj.totalTax - row11Relief89);

      // Row 13 & 14
      let row13TdsPaid = totTds;
      let row14BalanceToPay = Math.max(0, row12BalanceTaxPayable - row13TdsPaid);

      // Anticipatory Monthly Deduction
      let pendingMonths = Math.max(1, getNum('pending-months') || 1);
      let monthlyAnticipatoryTds = Math.ceil(row14BalanceToPay / pendingMonths);

      // Mode
      let isAnticipatory = document.getElementById('stmt-mode').value === 'anticipatory';
      let modeText = isAnticipatory ? 'ANTICIPATORY STATEMENT' : 'FINAL STATEMENT';

      // Update Top Comparison Cards
      setText('top-new-tax', '₹' + formatINR(row12BalanceTaxPayable));
      setText('top-monthly-tds', '₹' + formatINR(monthlyAnticipatoryTds) + ' / mo');
      setText('top-pending-months-label', isAnticipatory ? `(${pendingMonths} pending months)` : '(Final Settlement)');

      // Update Form 10E Badge
      setText('f10e-cur-arrear-tag', '₹' + formatINR(arrears));

      // --- Populate New Regime Statement (Single Page A4) ---
      setText('eco-badge-mode', modeText);
      setText('eco-emp-name', document.getElementById('emp-name').value || '');
      setText('eco-emp-desig', document.getElementById('emp-designation').value || '');
      setText('eco-emp-pan', (document.getElementById('emp-pan').value || '').toUpperCase());
      setText('eco-emp-pen', document.getElementById('emp-pen').value || '');
      setText('eco-emp-office', document.getElementById('emp-office').value || '');

      setText('eco-row1a', formatINR(totGross));
      setText('eco-row1b', formatINR(row1bTotal));
      setText('eco-row1c', formatINR(row1cExcess));
      setText('eco-row1-tot', formatINR(row1GrossSalary));
      setText('eco-row1-main', formatINR(row1GrossSalary));

      setText('eco-row2a', formatINR(row2aStdDed));
      setText('eco-row2b', formatINR(row2bConvey));
      setText('eco-row2c', formatINR(row2cNps));
      setText('eco-row2e', formatINR(row2eProfTax));
      setText('eco-row2-sub', formatINR(row2TotDedNew));
      setText('eco-row2-main', formatINR(row2TotDedNew));

      setText('eco-row3-main', formatINR(row3Remun));
      setText('eco-row4-main', formatINR(row4TotalIncomeNew));
      setText('eco-row5-main', formatINR(newTaxObj.tax));
      setText('eco-row6-main', formatINR(newTaxObj.rebate));
      setText('eco-row7-main', formatINR(newTaxObj.taxAfterRebate));
      setText('eco-row8-main', formatINR(newTaxObj.surcharge));
      setText('eco-row9-main', formatINR(newTaxObj.cess));
      setText('eco-row10-main', formatINR(newTaxObj.totalTax));
      setText('eco-row11-main', formatINR(row11Relief89));
      setText('eco-row12-main', formatINR(row12BalanceTaxPayable));
      setText('eco-row13-main', formatINR(row13TdsPaid));
      setText('eco-row14-main', formatINR(row14BalanceToPay));

      if (isAnticipatory) {
        setText('eco-anticipatory-note', `(To be deducted @ ₹${formatINR(monthlyAnticipatoryTds)} / month for ${pendingMonths} pending months)`);
      } else {
        setText('eco-anticipatory-note', `(Final Assessment for FY 2026-27 / AY 2027-28)`);
      }

      const empName = (document.getElementById('emp-name').value || '').trim();
      const empPlace = (document.getElementById('emp-place').value || '').trim();
      setText('eco-sig-place', empPlace || '________________');
      setText('eco-sig-date', formatDate(document.getElementById('stmt-date').value));
      setText('eco-sig-name', empName);
      setText('eco-sig-pen', document.getElementById('emp-pen').value || '');
      setText('eco-sig-desig', document.getElementById('emp-designation').value || '');
      setText('eco-sig-office', document.getElementById('emp-office').value || '');

      // --- Populate Detailed Old Regime Statement ---
      let oldStdDed = 50000;
      let oldProfTax = row2eProfTax;
      let oldSalaryIncome = Math.max(0, row1GrossSalary - (oldStdDed + oldProfTax));
      let oldGrossTotIncome = oldSalaryIncome + row3Remun;

      // Sum detailed 80C items
      let gpf = getNum('ded-gpf');
      let sli = getNum('ded-sli');
      let gis = getNum('ded-gis');
      let lic = getNum('ded-lic');
      let tuition = getNum('ded-tuition');
      let hlp = getNum('ded-hl-principal');
      let ppf = getNum('ded-ppf');
      let other80c = getNum('ded-80c-other');
      let tot80cClaimed = gpf + sli + gis + lic + tuition + hlp + ppf + other80c;
      let ded80cEligible = Math.min(tot80cClaimed, 150000);

      setText('lbl-80c-claimed', '₹' + formatINR(tot80cClaimed));
      setText('lbl-80c-eligible', '₹' + formatINR(ded80cEligible));

      let ded80ccd = Math.min(getNum('ded-80ccd1b'), 50000);
      let ded80d = getNum('ded-80d');
      let ded24b = Math.min(getNum('ded-24b'), 200000);
      let ded80e = getNum('ded-80e');
      let ded80g = getNum('ded-80g');
      let ded80tta = Math.min(getNum('ded-80tta'), 10000);
      let totalOldDeductions = ded80cEligible + ded80ccd + ded80d + ded24b + ded80e + ded80g + ded80tta;

      let oldTaxableIncome = Math.max(0, oldGrossTotIncome - totalOldDeductions);
      oldTaxableIncome = Math.round(oldTaxableIncome / 10) * 10;
      let oldTaxObj = computeOldRegimeTax(oldTaxableIncome);
      let oldBalanceTaxPayable = Math.max(0, oldTaxObj.totalTax - row11Relief89);
      let oldBalanceToPay = Math.max(0, oldBalanceTaxPayable - row13TdsPaid);
      let oldMonthlyTds = Math.ceil(oldBalanceToPay / pendingMonths);

      setText('top-old-tax', '₹' + formatINR(oldBalanceTaxPayable));
      if (row12BalanceTaxPayable < oldBalanceTaxPayable) {
        let diff = oldBalanceTaxPayable - row12BalanceTaxPayable;
        setText('top-regime-recommendation', `🌟 New Regime saves ₹${formatINR(diff)}`);
      } else if (oldBalanceTaxPayable < row12BalanceTaxPayable) {
        let diff = row12BalanceTaxPayable - oldBalanceTaxPayable;
        setText('top-regime-recommendation', `⚖️ Old Regime saves ₹${formatINR(diff)}`);
      } else {
        setText('top-regime-recommendation', `Both Regimes Equal`);
      }

      setText('old-badge-mode', modeText);
      setText('old-emp-name', document.getElementById('emp-name').value);
      setText('old-emp-desig', document.getElementById('emp-designation').value);
      setText('old-emp-pan', (document.getElementById('emp-pan').value || '').toUpperCase());
      setText('old-emp-pen', document.getElementById('emp-pen').value);
      setText('old-emp-office', document.getElementById('emp-office').value);

      setText('old-row1', formatINR(row1GrossSalary));
      setText('old-row2-pt', formatINR(oldProfTax));
      setText('old-row2', formatINR(oldStdDed + oldProfTax));
      setText('old-row3', formatINR(oldSalaryIncome));
      setText('old-row4', formatINR(row3Remun));
      setText('old-row5', formatINR(oldGrossTotIncome));

      // Monthly breakdown in Old Regime Statement
      months.forEach(m => {
        let el = document.getElementById('old-m-' + m.key);
        if (el) el.textContent = formatINR(getNum('basic-' + m.key) + getNum('allow-' + m.key));
      });
      setText('old-row1a', formatINR(totGross));
      setText('old-row1b', formatINR(row1bTotal));
      setText('old-row1c', formatINR(row1cExcess));
      setText('old-row1-tot', formatINR(row1GrossSalary));

      setText('old-det-gpf', formatINR(gpf));
      setText('old-det-sli', formatINR(sli));
      setText('old-det-gis', formatINR(gis));
      setText('old-det-lic', formatINR(lic));
      setText('old-det-tuition', formatINR(tuition));
      setText('old-det-hlp', formatINR(hlp));
      setText('old-det-ppf', formatINR(ppf + other80c));
      setText('old-80c-claimed', formatINR(tot80cClaimed));
      setText('old-80c', formatINR(ded80cEligible));

      setText('old-80ccd', formatINR(ded80ccd));
      setText('old-80d', formatINR(ded80d));
      setText('old-24b', formatINR(ded24b));
      setText('old-80e', formatINR(ded80e));
      setText('old-80g', formatINR(ded80g));
      setText('old-80tta', formatINR(ded80tta));
      setText('old-row6', formatINR(totalOldDeductions));

      setText('old-sig-pen', document.getElementById('emp-pen').value || '');
      setText('old-sig-office', document.getElementById('emp-office').value || '');

      setText('old-row7', formatINR(oldTaxableIncome));
      setText('old-row8', formatINR(oldTaxObj.tax));
      setText('old-row9', formatINR(oldTaxObj.rebate));
      setText('old-row10', formatINR(oldTaxObj.taxAfterRebate));
      setText('old-row11', formatINR(oldTaxObj.cess));
      setText('old-row12', formatINR(oldTaxObj.totalTax));
      setText('old-row13', formatINR(row11Relief89));
      setText('old-row14', formatINR(row13TdsPaid));
      setText('old-row15', formatINR(oldBalanceToPay));

      if (isAnticipatory) {
        setText('old-anticipatory-note', `(To be deducted @ ₹${formatINR(oldMonthlyTds)} / month for ${pendingMonths} pending months)`);
      } else {
        setText('old-anticipatory-note', `(Final Assessment)`);
      }

      setText('old-sig-place', empPlace || '________________');
      setText('old-sig-date', formatDate(document.getElementById('stmt-date').value));
      setText('old-sig-name', empName);
      setText('old-sig-desig', document.getElementById('emp-designation').value || '');

      // --- Update Form 10E Static Employee particulars ---
      setText('f10e-disp-name', empName);
      setText('f10e-disp-pan', (document.getElementById('emp-pan').value || '').toUpperCase());
      setText('f10e-disp-desig', document.getElementById('emp-designation').value || '');
      setText('f10e-disp-pen', document.getElementById('emp-pen').value || '');
      setText('f10e-disp-office', document.getElementById('emp-office').value || '');
      setText('f10e-ver-name', empName);
      setText('f10e-ver-name2', empName);
      setText('f10e-ver-desig', document.getElementById('emp-designation').value || '');
      setText('f10e-ver-place', empPlace || '________________');
      setText('f10e-ver-date', formatDate(document.getElementById('stmt-date').value));

      // Auto-save user entered data so it persists across page refreshes
      if (window._autoSaveEnabled) {
        try {
          const draft = collectFormData();
          localStorage.setItem('income_tax_2026_27_draft', JSON.stringify(draft));
        } catch (e) {}
      }
    }

    // Date formatter dd/mm/yyyy
    function formatDate(dStr) {
      if (!dStr) return '';
      const parts = dStr.split('-');
      if (parts.length === 3) return `${parts[2]}/${parts[1]}/${parts[0]}`;
      return dStr;
    }

    // --- Form 10E Logic & Table A Rendering ---
    function onYearSelectionChange() {
      const yr = document.getElementById('f10e-sel-year').value;
      const startYear = parseInt(yr.split('-')[0].trim());
      const newWrap = document.getElementById('f10e-regime-new-wrap');
      if (startYear < 2020) {
        newWrap.style.display = 'none';
        document.getElementById('f10e-regime-old').checked = true;
      } else {
        newWrap.style.display = 'inline-block';
      }
    }

    function addPreviousYearEntry() {
      const year = document.getElementById('f10e-sel-year').value;
      const income = Math.max(0, getNum('f10e-input-income'));
      const arrear = Math.max(0, getNum('f10e-input-arrear'));
      const age = document.getElementById('f10e-input-age').value;
      const regime = document.querySelector('input[name="f10e-taxslab"]:checked').value;

      if (arrear <= 0) {
        alert('Please enter arrears received greater than 0.');
        return;
      }

      // Check if year already exists, replace or add
      const existing = tableAEntries.find(e => e.year === year);
      if (existing) {
        if (!confirm(`Financial Year ${year} already exists in Table A. Do you want to update it?`)) {
          return;
        }
        existing.income = income;
        existing.arrear = arrear;
        existing.age = age;
        existing.regime = regime;
      } else {
        tableAEntries.push({
          id: Date.now(),
          year,
          income,
          arrear,
          age,
          regime
        });
      }

      renderTableA();
    }

    function deleteTableAEntry(id) {
      if (confirm('Are you sure you want to remove this financial year from Form 10E?')) {
        tableAEntries = tableAEntries.filter(e => e.id !== id);
        renderTableA();
      }
    }

    function renderTableA() {
      const tbody = document.getElementById('table-a-body');
      tbody.innerHTML = '';

      let totArrears = 0;
      let totTaxWithout = 0;
      let totTaxWith = 0;
      let totDiff = 0;

      tableAEntries.forEach((entry, idx) => {
        let incomeWithArrear = entry.income + entry.arrear;
        let taxWithout = computeHistoricalTax(entry.year, entry.income, entry.age, entry.regime).totalTax;
        let taxWith = computeHistoricalTax(entry.year, incomeWithArrear, entry.age, entry.regime).totalTax;
        let diff = Math.max(0, taxWith - taxWithout);

        totArrears += entry.arrear;
        totTaxWithout += taxWithout;
        totTaxWith += taxWith;
        totDiff += diff;

        let tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="text-align:center;">${idx + 1}</td>
          <td style="font-weight:600;">${entry.year} <small style="color:#000;">(${entry.regime})</small></td>
          <td style="text-align:right;">${formatINR(entry.income)}</td>
          <td style="text-align:right; font-weight:600; color:#000;">${formatINR(entry.arrear)}</td>
          <td style="text-align:right;">${formatINR(incomeWithArrear)}</td>
          <td style="text-align:right;">${formatINR(taxWithout)}</td>
          <td style="text-align:right;">${formatINR(taxWith)}</td>
          <td style="text-align:right; font-weight:bold; color:#000;">${formatINR(diff)}</td>
          <td style="text-align:center;" class="no-print-10e">
            <button class="btn btn-danger" style="padding:2px 6px; font-size:0.7rem;" onclick="deleteTableAEntry(${entry.id})">✕</button>
          </td>
        `;
        tbody.appendChild(tr);
      });

      setText('tbla-tot-arrear', formatINR(totArrears));
      setText('tbla-tot-tax-wo', formatINR(totTaxWithout));
      setText('tbla-tot-tax-w', formatINR(totTaxWith));
      setText('tbla-tot-diff', formatINR(totDiff));

      // Compute Annexure I (Current Year FY 2026-27 vs Previous Years)
      // Current year total income including arrears:
      let curArrearsIn1b = getNum('row1b-arrears');
      // If current arrears input in 1b is 0 but Table A has arrears, auto-sync prompt
      let curTotalIncomeWithArrears = Math.round(parseFloat(document.getElementById('eco-row4-main').textContent.replace(/,/g, '')) || 0);

      // Current year tax with arrears:
      let curTaxWithArrears = computeNewRegimeTax(curTotalIncomeWithArrears).totalTax;

      // Current year income without arrears:
      let curIncomeWithoutArrears = Math.max(0, curTotalIncomeWithArrears - totArrears);
      curIncomeWithoutArrears = Math.round(curIncomeWithoutArrears / 10) * 10;
      let curTaxWithoutArrears = computeNewRegimeTax(curIncomeWithoutArrears).totalTax;

      // Difference in current year:
      let curTaxOnArrears = Math.max(0, curTaxWithArrears - curTaxWithoutArrears);

      // Section 89 Relief = Current Year Tax on Arrears (A) - Previous Years Tax on Arrears (B)
      let relief89 = Math.max(0, curTaxOnArrears - totDiff);

      // Update Annexure I table
      setText('f10e-step1-inc', formatINR(curTotalIncomeWithArrears));
      setText('f10e-step1-tax', formatINR(curTaxWithArrears));
      setText('f10e-step2-inc', formatINR(curIncomeWithoutArrears));
      setText('f10e-step2-tax', formatINR(curTaxWithoutArrears));
      setText('f10e-tax-cur-arrear', formatINR(curTaxOnArrears));

      setText('f10e-prev-with-tax', formatINR(totTaxWith));
      setText('f10e-prev-without-tax', formatINR(totTaxWithout));
      setText('f10e-tax-prev-arrear', formatINR(totDiff));

      setText('f10e-final-relief', '₹' + formatINR(relief89));
      window._calculatedRelief89 = relief89;
    }

    function apply10eToStatement() {
      if (window._calculatedRelief89 === undefined) {
        renderTableA();
      }
      let r = window._calculatedRelief89 || 0;
      setNum('row11-relief89', r);
      calculateAll();
      alert(`✓ Success! Relief of ₹${formatINR(r)} applied to Row 11 of Income Tax Statement.`);
      showTab('new-regime');
    }

    function loadSample10E() {
      tableAEntries = [
        { id: 1, year: '2024 - 25', income: 850000, arrear: 65000, age: 'Individual', regime: 'NEW' },
        { id: 2, year: '2023 - 24', income: 780000, arrear: 45000, age: 'Individual', regime: 'NEW' }
      ];
      setNum('row1b-arrears', 110000);
      calculateAll();
      renderTableA();
      alert('✓ Sample Arrears loaded into Table A (FY 2024-25 & FY 2023-24).');
    }

    function clear10EData() {
      if (confirm('Clear all Form 10E previous year entries?')) {
        tableAEntries = [];
        setNum('row11-relief89', 0);
        calculateAll();
        renderTableA();
      }
    }

    // --- Action Bar Functions ---

    // Load Prof. Rajesh K Sample (Model PDF)
    const loadOldSample = function() { loadSampleData(); };
    function loadSampleData() {
      document.getElementById('emp-name').value = 'Prof. Rajesh K';
      document.getElementById('emp-pan').value = 'ABCDE5678G';
      document.getElementById('emp-pen').value = '412850';
      document.getElementById('emp-designation').value = 'Professor';
      document.getElementById('emp-office').value = 'GOVT COLLEGE KOZHIKODE';
      document.getElementById('emp-place').value = 'Kozhikode';
      document.getElementById('stmt-mode').value = 'anticipatory';
      document.getElementById('stmt-date').value = '2026-11-23';
      document.getElementById('pending-months').value = '3';

      // Imaginary monthly salary slightly modified from typical college professor scale
      const monthlyValues = [
        { basic: 149200, allow: 0, pf: 14000, tds: 9500 }, // Mar
        { basic: 149200, allow: 0, pf: 14000, tds: 9500 }, // Apr
        { basic: 149200, allow: 0, pf: 14000, tds: 9500 }, // May
        { basic: 149200, allow: 0, pf: 14000, tds: 9500 }, // Jun
        { basic: 153700, allow: 0, pf: 14000, tds: 9500 }, // Jul (increment)
        { basic: 153700, allow: 0, pf: 14000, tds: 9500 }, // Aug
        { basic: 153700, allow: 0, pf: 14000, tds: 9500 }, // Sep
        { basic: 153700, allow: 0, pf: 14000, tds: 9500 }, // Oct
        { basic: 153700, allow: 0, pf: 14000, tds: 9500 }, // Nov
        { basic: 153700, allow: 0, pf: 14000, tds: 9500 }, // Dec
        { basic: 153700, allow: 0, pf: 14000, tds: 9500 }, // Jan
        { basic: 153700, allow: 0, pf: 14000, tds: 9500 }  // Feb
      ];

      months.forEach((m, idx) => {
        let v = monthlyValues[idx];
        setNum('basic-' + m.key, v.basic);
        setNum('allow-' + m.key, v.allow);
        setNum('pf-' + m.key, v.pf);
        setNum('tds-' + m.key, v.tds);
      });

      setNum('row1b-surrender', 0);
      setNum('row1b-bonus', 0);
      setNum('row1b-arrears', 0);
      setNum('row1b-other', 0);
      setNum('row1c-excess', 0);
      setNum('row3-remuneration', 12000);
      setNum('row2b-conveyance', 0);
      setNum('row2c-nps', 0);
      setNum('row2e-proftax', 2500);
      setNum('row11-relief89', 0);

      window._autoSaveEnabled = true;
      calculateAll();
      showToast('📄 Loaded sample teacher data (Prof. Rajesh K).');
    }

    // Clear All Data
    function clearAllData() {
      if (!confirm('Are you sure you want to clear all data? This will reset all salary and deduction fields.')) {
        return;
      }
      document.getElementById('emp-name').value = '';
      document.getElementById('emp-pan').value = '';
      document.getElementById('emp-pen').value = '';
      document.getElementById('emp-designation').value = '';
      document.getElementById('emp-office').value = '';
      document.getElementById('emp-place').value = '';

      months.forEach(m => {
        setNum('basic-' + m.key, 0);
        setNum('allow-' + m.key, 0);
        setNum('pf-' + m.key, 0);
        setNum('tds-' + m.key, 0);
      });

      setNum('row1b-surrender', 0);
      setNum('row1b-bonus', 0);
      setNum('row1b-arrears', 0);
      setNum('row1b-other', 0);
      setNum('row1c-excess', 0);
      setNum('row3-remuneration', 0);
      setNum('row2b-conveyance', 0);
      setNum('row2c-nps', 0);
      setNum('row2e-proftax', 0);
      setNum('row11-relief89', 0);

      setNum('ded-gpf', 0);
      setNum('ded-sli', 0);
      setNum('ded-gis', 0);
      setNum('ded-lic', 0);
      setNum('ded-tuition', 0);
      setNum('ded-hl-principal', 0);
      setNum('ded-ppf', 0);
      setNum('ded-80c-other', 0);
      setNum('ded-80ccd1b', 0);
      setNum('ded-80d', 0);
      setNum('ded-24b', 0);
      setNum('ded-80e', 0);
      setNum('ded-80g', 0);
      setNum('ded-80tta', 0);

      tableAEntries = [];
      renderTableA();

      // Clear saved draft from browser storage
      try {
        localStorage.removeItem('income_tax_2026_27_draft');
      } catch (e) {}

      calculateAll();
      showToast('🧹 All data cleared and storage reset.');
    }

    // Copy Any Month Salary down to all Subsequent Months
    function copyMonthDown(idx) {
      if (idx < 0 || idx >= months.length - 1) return;
      const src = months[idx];
      const b = getNum('basic-' + src.key);
      const a = getNum('allow-' + src.key);
      const pf = getNum('pf-' + src.key);
      const tds = getNum('tds-' + src.key);

      if (b === 0 && a === 0) {
        alert('Please enter a salary amount in ' + src.name + ' first.');
        return;
      }

      for (let i = idx + 1; i < months.length; i++) {
        const target = months[i];
        setNum('basic-' + target.key, b);
        setNum('allow-' + target.key, a);
        setNum('pf-' + target.key, pf);
        setNum('tds-' + target.key, tds);
      }

      calculateAll();
      alert('✓ Copied ' + src.name + ' Gross Salary & Deductions down to all remaining months (' + months[idx + 1].name + ' to February 2027)!');
    }

    // Copy March Salary down to All Months
    function copyMarchSalary() {
      copyMonthDown(0);
    }

    // Apply DA Hike Prompt
    function applyDAHikePrompt() {
      const pctStr = prompt('Enter DA Hike percentage (e.g. 4 for 4% increase):', '4');
      if (!pctStr) return;
      const pct = parseFloat(pctStr);
      if (isNaN(pct) || pct <= 0) {
        alert('Please enter a valid percentage.');
        return;
      }
      const fromMonth = prompt('Apply DA hike from which month? (mar, apr, may, jun, jul, aug, sep, oct, nov, dec, jan, feb):', 'jul');
      if (!fromMonth) return;

      const factor = 1 + (pct / 100);
      let started = false;
      months.forEach(m => {
        if (m.key.toLowerCase() === fromMonth.toLowerCase().trim()) started = true;
        if (started) {
          let curr = getNum('basic-' + m.key);
          setNum('basic-' + m.key, Math.round(curr * factor));
        }
      });
      calculateAll();
      alert(`✓ ${pct}% DA hike applied starting from ${fromMonth.toUpperCase()}.`);
    }

    // Printing Handlers
    function printNewRegimeStatement() {
      showTab('new-regime');
      document.body.className = 'printing-new-regime';
      window.setTimeout(() => {
        window.print();
        window.setTimeout(() => { document.body.className = ''; }, 1000);
      }, 200);
    }

    function printOldRegimeStatement() {
      showTab('old-regime');
      document.body.className = 'printing-old-regime';
      window.setTimeout(() => {
        window.print();
        window.setTimeout(() => { document.body.className = ''; }, 1000);
      }, 200);
    }

    function printForm10E() {
      showTab('form-10e');
      renderTableA();
      document.body.className = 'printing-10e';
      window.setTimeout(() => {
        window.print();
        window.setTimeout(() => { document.body.className = ''; }, 1000);
      }, 200);
    }


    // --- Direct A4 PDF Download & Toast Notifications ---
    function showToast(msg) {
      let toast = document.getElementById('app-toast');
      if (!toast) {
        toast = document.createElement('div');
        toast.id = 'app-toast';
        toast.style.cssText = `
          position: fixed;
          bottom: 24px;
          right: 24px;
          background: #0f172a;
          color: #ffffff;
          padding: 12px 20px;
          border-radius: 8px;
          font-size: 0.875rem;
          font-weight: 600;
          box-shadow: 0 10px 25px -5px rgba(0,0,0,0.4);
          z-index: 99999;
          transition: opacity 0.3s ease, transform 0.3s ease;
          max-width: 90vw;
          border: 1px solid #334155;
        `;
        document.body.appendChild(toast);
      }
      toast.textContent = msg;
      toast.style.opacity = '1';
      toast.style.transform = 'translateY(0)';
      clearTimeout(window._toastTimer);
      window._toastTimer = setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(10px)';
      }, 4000);
    }

    
    // --- Data Management: Save, Restore, Export, Import JSON ---
    function collectFormData() {
      const data = {
        app: 'IncomeTaxCalculator',
        version: '2026-27',
        exportedAt: new Date().toISOString(),
        employee: {
          name: document.getElementById('emp-name').value,
          pan: document.getElementById('emp-pan').value,
          pen: document.getElementById('emp-pen').value,
          designation: document.getElementById('emp-designation').value,
          office: document.getElementById('emp-office').value,
          place: document.getElementById('emp-place').value,
          stmtMode: document.getElementById('stmt-mode').value,
          stmtDate: document.getElementById('stmt-date').value,
          pendingMonths: getNum('pending-months')
        },
        salaryMonths: {},
        additionalIncome: {
          surrender: getNum('row1b-surrender'),
          bonus: getNum('row1b-bonus'),
          arrears: getNum('row1b-arrears'),
          other: getNum('row1b-other'),
          excess: getNum('row1c-excess'),
          remuneration: getNum('row3-remuneration')
        },
        deductions: {
          conveyance: getNum('row2b-conveyance'),
          npsEmployer: getNum('row2c-nps'),
          profTax: getNum('row2e-proftax'),
          relief89: getNum('row11-relief89'),
          gpf: getNum('ded-gpf'),
          sli: getNum('ded-sli'),
          gis: getNum('ded-gis'),
          lic: getNum('ded-lic'),
          tuition: getNum('ded-tuition'),
          hlp: getNum('ded-hl-principal'),
          ppf: getNum('ded-ppf'),
          other80c: getNum('ded-80c-other'),
          ded80ccd1b: getNum('ded-80ccd1b'),
          ded80d: getNum('ded-80d'),
          ded24b: getNum('ded-24b'),
          ded80e: getNum('ded-80e'),
          ded80g: getNum('ded-80g'),
          ded80tta: getNum('ded-80tta')
        },
        tableAEntries: tableAEntries
      };

      months.forEach(m => {
        data.salaryMonths[m.key] = {
          basic: getNum('basic-' + m.key),
          allow: getNum('allow-' + m.key),
          pf: getNum('pf-' + m.key),
          tds: getNum('tds-' + m.key)
        };
      });

      return data;
    }

    function restoreFormData(data) {
      if (!data) return;
      if (data.employee) {
        document.getElementById('emp-name').value = data.employee.name || '';
        document.getElementById('emp-pan').value = data.employee.pan || '';
        document.getElementById('emp-pen').value = data.employee.pen || '';
        document.getElementById('emp-designation').value = data.employee.designation || '';
        document.getElementById('emp-office').value = data.employee.office || '';
        document.getElementById('emp-place').value = data.employee.place || '';
        if (data.employee.stmtMode) document.getElementById('stmt-mode').value = data.employee.stmtMode;
        if (data.employee.stmtDate) document.getElementById('stmt-date').value = data.employee.stmtDate;
        if (data.employee.pendingMonths) setNum('pending-months', data.employee.pendingMonths);
      }

      if (data.salaryMonths) {
        months.forEach(m => {
          const sm = data.salaryMonths[m.key] || {};
          setNum('basic-' + m.key, sm.basic || 0);
          setNum('allow-' + m.key, sm.allow || 0);
          setNum('pf-' + m.key, sm.pf || 0);
          setNum('tds-' + m.key, sm.tds || 0);
        });
      }

      if (data.additionalIncome) {
        setNum('row1b-surrender', data.additionalIncome.surrender || 0);
        setNum('row1b-bonus', data.additionalIncome.bonus || 0);
        setNum('row1b-arrears', data.additionalIncome.arrears || 0);
        setNum('row1b-other', data.additionalIncome.other || 0);
        setNum('row1c-excess', data.additionalIncome.excess || 0);
        setNum('row3-remuneration', data.additionalIncome.remuneration || 0);
      }

      if (data.deductions) {
        setNum('row2b-conveyance', data.deductions.conveyance || 0);
        setNum('row2c-nps', data.deductions.npsEmployer || 0);
        setNum('row2e-proftax', data.deductions.profTax || 0);
        setNum('row11-relief89', data.deductions.relief89 || 0);
        setNum('ded-gpf', data.deductions.gpf || 0);
        setNum('ded-sli', data.deductions.sli || 0);
        setNum('ded-gis', data.deductions.gis || 0);
        setNum('ded-lic', data.deductions.lic || 0);
        setNum('ded-tuition', data.deductions.tuition || 0);
        setNum('ded-hl-principal', data.deductions.hlp || 0);
        setNum('ded-ppf', data.deductions.ppf || 0);
        setNum('ded-80c-other', data.deductions.other80c || 0);
        setNum('ded-80ccd1b', data.deductions.ded80ccd1b || 0);
        setNum('ded-80d', data.deductions.ded80d || 0);
        setNum('ded-24b', data.deductions.ded24b || 0);
        setNum('ded-80e', data.deductions.ded80e || 0);
        setNum('ded-80g', data.deductions.ded80g || 0);
        setNum('ded-80tta', data.deductions.ded80tta || 0);
      }

      if (Array.isArray(data.tableAEntries)) {
        tableAEntries = data.tableAEntries;
        renderTableA();
      }

      calculateAll();
    }

    function saveDraft() {
      const data = collectFormData();
      localStorage.setItem('income_tax_2026_27_draft', JSON.stringify(data));
      showToast('💾 Draft saved successfully to browser storage!');
    }

    function restoreDraft() {
      const raw = localStorage.getItem('income_tax_2026_27_draft');
      if (!raw) {
        alert('No saved draft found in this browser storage.');
        return;
      }
      try {
        const data = JSON.parse(raw);
        restoreFormData(data);
        showToast('📂 Saved draft restored successfully!');
      } catch (e) {
        alert('Failed to restore draft: ' + e.message);
      }
    }

    function exportJSON() {
      const data = collectFormData();
      const jsonStr = JSON.stringify(data, null, 2);
      const blob = new Blob([jsonStr], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      const name = (document.getElementById('emp-name').value || 'tax_statement').replace(/[^a-zA-Z0-9_-]/g, '_');
      a.href = url;
      a.download = `${name}_income_tax_2026_27.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      showToast('📥 Data exported as JSON file successfully!');
    }

    function triggerImportJSON() {
      const fileInput = document.getElementById('json-file-input');
      if (fileInput) {
        fileInput.value = '';
        fileInput.click();
      }
    }

    function handleFileImport(event) {
      const file = event.target.files && event.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(e) {
        try {
          const data = JSON.parse(e.target.result);
          restoreFormData(data);
          showToast('📤 Data imported from ' + file.name + ' successfully!');
        } catch (err) {
          alert('Invalid JSON file format: ' + err.message);
        }
      };
      reader.readAsText(file);
    }

    // High-Resolution Vector A4 PDF Generation using Isolated Visual Overlay
    function downloadPdfFromElement(elementId, filename) {
      const element = document.getElementById(elementId);
      if (!element) {
        alert('Statement element not found.');
        return;
      }

      showToast('⏳ Rendering neat A4 PDF... Please wait.');

      if (typeof html2pdf !== 'undefined') {
        const overlay = document.createElement('div');
        overlay.id = 'pdf-render-overlay';
        overlay.style.position = 'fixed';
        overlay.style.top = '0';
        overlay.style.left = '0';
        overlay.style.width = '100vw';
        overlay.style.height = '100vh';
        overlay.style.backgroundColor = '#ffffff';
        overlay.style.zIndex = '9999999';
        overlay.style.overflow = 'hidden';
        overlay.style.margin = '0';
        overlay.style.padding = '0';

        const banner = document.createElement('div');
        banner.style.textAlign = 'center';
        banner.style.padding = '10px';
        banner.style.fontSize = '13px';
        banner.style.fontWeight = 'bold';
        banner.style.color = '#000000';
        banner.style.background = '#f8fafc';
        banner.style.borderBottom = '1px solid #cbd5e1';
        banner.innerHTML = '⏳ Generating crisp vector A4 PDF... Please wait a moment.';
        overlay.appendChild(banner);

        const container = document.createElement('div');
        container.style.width = '670px';
        container.style.margin = '10px auto 0 auto';
        container.style.background = '#ffffff';
        container.style.boxSizing = 'border-box';

        const clone = element.cloneNode(true);
        clone.id = 'pdf-export-clone';
        clone.style.width = '100%';
        clone.style.maxWidth = '670px';
        clone.style.minWidth = '670px';
        clone.style.margin = '0';
        clone.style.padding = '0';
        clone.style.background = '#ffffff';
        clone.style.color = '#000000';
        clone.style.boxSizing = 'border-box';

        container.appendChild(clone);
        overlay.appendChild(container);
        document.body.appendChild(overlay);

        // 670px at 96 DPI is 177.27mm. Total A4 portrait width is 210mm.
        // Exact symmetrical margins to center the 670px blocks on A4 page: (210 - 177.27) / 2 = 16.36mm (~16.4mm).
        const opt = {
          margin: [6, 16.4, 6, 16.4],
          filename: filename,
          image: { type: 'jpeg', quality: 0.98 },
          html2canvas: {
            scale: 2,
            useCORS: true,
            letterRendering: true,
            scrollY: 0,
            scrollX: 0,
            logging: false
          },
          jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
        };

        html2pdf().set(opt).from(clone).save().then(() => {
          if (overlay.parentNode) document.body.removeChild(overlay);
          showToast('✓ Neat A4 PDF downloaded: ' + filename);
        }).catch(err => {
          console.warn('html2pdf fallback to window.print():', err);
          if (overlay.parentNode) document.body.removeChild(overlay);
          window.print();
        });
      } else {
        window.print();
      }
    }

    function downloadNewRegimePdf() {
      showTab('new-regime');
      setTimeout(() => {
        downloadPdfFromElement('ecostatt-single-page', 'Income_Tax_Statement_2026-27_New_Regime.pdf');
      }, 250);
    }

    function downloadOldRegimePdf() {
      showTab('old-regime');
      setTimeout(() => {
        downloadPdfFromElement('old-regime-single-page', 'Income_Tax_Statement_2026-27_Old_Regime.pdf');
      }, 250);
    }

    function downloadForm10EPdf() {
      showTab('form-10e');
      renderTableA();
      setTimeout(() => {
        downloadPdfFromElement('form-10e-single-page', 'Form_10E_Section_89_Relief_2026-27.pdf');
      }, 250);
    }

    // Initialization
    document.addEventListener('DOMContentLoaded', function() {
      initSalaryTable();
      onYearSelectionChange();

      // Check if user has saved draft in localStorage
      const saved = localStorage.getItem('income_tax_2026_27_draft');
      if (saved) {
        try {
          const parsed = JSON.parse(saved);
          restoreFormData(parsed);
          window._autoSaveEnabled = true;
          showToast('📂 Restored your saved data.');
          return;
        } catch (err) {
          console.warn('Could not restore draft:', err);
        }
      }

      // No saved data: start with clean blank form
      window._autoSaveEnabled = true;
      calculateAll();
    });
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("Generated index.html successfully! Size:", os.path.getsize('index.html'))
