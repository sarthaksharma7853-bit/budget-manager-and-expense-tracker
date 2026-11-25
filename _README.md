This project report is for a menu-driven Python mini project (Course: 2026CSAE100 — Computational Thinking and Programming) at Bennett University (School of Computer Science Engineering and Technology, Academic Year 2026–27). It provides a terminal-based tool for tracking personal income, expenses, and monthly budgets using only Python's standard library.

Team & Project Details
Team Members & Roles:

Nihal (S26CSEU1961, Batch/Section 56/28) – Team Leader

Ayush Kumar – Budget checking

Payash – Expense calculation and presentation

Sarthak Sharma – PPT preparation and data entry

Core Technologies: Python, csv, os, and datetime (no external packages required).

Profile System: Uses a username entered at startup to separate user records on a single machine (no passwords or online accounts).

Key Features & Workflow
The application runs a repeating 5-option text menu after loading or creating a user profile:

Add Income: Records a positive amount, income source, date (YYYY-MM-DD, defaulting to today if blank), and optional note.

Add Expense: Records a positive amount, expense category (such as Food, Travel, Shopping, or Bills), date, and optional note.

View Monthly / Category-wise Reports: Filters records by a selected YYYY-MM month (or current month) to calculate total income, total expenses, balance (income - expenses), and category-wise expense totals.

Check Monthly Budget: Retrieves or sets a monthly budget for the user and month, calculates remaining budget (budget - expenses), and displays an overspending alert with a suggestion to cut non-essential spending if exceeded.

Exit: Exits the loop (data is saved immediately upon each action).

Data Storage Design
Two CSV files are saved in the user's home directory (os.path.expanduser("~")) to avoid read-only working-directory issues:

expense_data.csv: Stores username, type (income or expense), amount, category, date, and note.

monthly_budgets.csv: Stores username, month (YYYY-MM), and budget.

Limitations & Future Scope
Current Limitations: Command-line interface only (no GUI), no password/authentication, no edit or delete options for existing records, limited date/month format validation, and budgets apply to total monthly spending rather than individual categories.

Future Scope: Add a GUI/dashboard, support editing and deleting entries, enforce strict date/month validation, add spending charts, and introduce category-level budgets and exportable summaries.
