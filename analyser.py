import csv
import os
from datetime import datetime

# Personal Expense and Budget Analyzer
# Data files are stored in your home folder to avoid read-only
# working-directory errors.

DATA_FILE = os.path.join(os.path.expanduser("~"), "expense_data.csv")
BUDGET_FILE = os.path.join(os.path.expanduser("~"), "monthly_budgets.csv")


def get_date():
    return datetime.now().strftime("%Y-%m-%d")


def load_records(username):
    records = []

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username:
                    records.append(row)

    return records


def save_record(username, record_type, amount, category, date, note):
    file_exists = os.path.exists(DATA_FILE)

    with open(DATA_FILE, "a", newline="") as file:
        fields = ["username", "type", "amount", "category", "date", "note"]
        writer = csv.DictWriter(file, fieldnames=fields)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "username": username,
            "type": record_type,
            "amount": amount,
            "category": category,
            "date": date,
            "note": note
        })


def get_monthly_budget(username, month):
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username and row["month"] == month:
                    return float(row["budget"])

    return None


def set_monthly_budget(username, month, budget):
    budgets = []

    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not (row["username"] == username and row["month"] == month):
                    budgets.append(row)

    budgets.append({
        "username": username,
        "month": month,
        "budget": budget
    })

    with open(BUDGET_FILE, "w", newline="") as file:
        fields = ["username", "month", "budget"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(budgets)


def add_income(username):
    print("\n--- Add Income ---")
    try:
        amount = float(input("Enter income amount: Rs. "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    category = input("Income source (for example, Salary or Allowance): ").strip()
    date = input("Date (YYYY-MM-DD) or press Enter for today: ").strip()
    if date == "":
        date = get_date()

    note = input("Note (optional): ").strip()
    save_record(username, "income", amount, category, date, note)
    print("Income saved successfully.")


def add_expense(username):
    print("\n--- Add Expense ---")
    try:
        amount = float(input("Enter expense amount: Rs. "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    category = input(
        "Expense category (Food, Travel, Shopping, Bills, etc.): "
    ).strip()
    date = input("Date (YYYY-MM-DD) or press Enter for today: ").strip()
    if date == "":
        date = get_date()

    note = input("Note (optional): ").strip()
    save_record(username, "expense", amount, category, date, note)
    print("Expense saved successfully.")


def view_reports(username):
    records = load_records(username)
    month = input("Enter month (YYYY-MM), or press Enter for current month: ").strip()

    if month == "":
        month = datetime.now().strftime("%Y-%m")

    income = 0
    expenses = 0
    category_totals = {}

    print("\n--- Monthly Report:", month, "---")

    for row in records:
        if row["date"].startswith(month):
            amount = float(row["amount"])

            if row["type"] == "income":
                income += amount
            elif row["type"] == "expense":
                expenses += amount
                category = row["category"]
                category_totals[category] = category_totals.get(category, 0) + amount

    print("Total income:   Rs.", round(income, 2))
    print("Total expenses: Rs.", round(expenses, 2))
    print("Balance:        Rs.", round(income - expenses, 2))

    print("\nExpenses by category:")
    if category_totals:
        for category, total in category_totals.items():
            print(category, ": Rs.", round(total, 2))
    else:
        print("No expenses recorded for this month.")


def check_budget(username):
    month = input("Enter month (YYYY-MM), or press Enter for current month: ").strip()
    if month == "":
        month = datetime.now().strftime("%Y-%m")

    budget = get_monthly_budget(username, month)

    if budget is None:
        print("No budget has been set for", month)
        try:
            budget = float(input("Set monthly budget (Rs.): "))
            if budget <= 0:
                print("Budget must be greater than zero.")
                return
            set_monthly_budget(username, month, budget)
            print("Monthly budget saved.")
        except ValueError:
            print("Please enter a valid amount.")
            return

    records = load_records(username)
    total_expenses = 0

    for row in records:
        if row["type"] == "expense" and row["date"].startswith(month):
            total_expenses += float(row["amount"])

    remaining = budget - total_expenses

    print("\n--- Budget Check:", month, "---")
    print("Monthly budget: Rs.", round(budget, 2))
    print("Total expenses: Rs.", round(total_expenses, 2))

    if remaining >= 0:
        print("You are within your budget.")
        print("Remaining amount: Rs.", round(remaining, 2))
        print("Keep managing your spending well!")
    else:
        print("Alert: You are over your budget!")
        print("Extra spending: Rs.", round(abs(remaining), 2))
        print("Suggestion: Reduce non-essential expenses.")


def main():
    print("=" * 45)
    print("       PERSONAL EXPENSE AND BUDGET")
    print("                ANALYZER")
    print("=" * 45)
    print("Your data files will be saved in:", os.path.expanduser("~"))

    username = input("Enter your username to create/load your profile: ").strip()
    if username == "":
        print("Username cannot be empty.")
        return

    print("Welcome,", username + "!")

    while True:
        print("\n--------------- MAIN MENU ---------------")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Monthly / Category-wise Reports")
        print("4. Check Monthly Budget")
        print("5. Exit")
        print("-----------------------------------------")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_income(username)
        elif choice == "2":
            add_expense(username)
        elif choice == "3":
            view_reports(username)
        elif choice == "4":
            check_budget(username)
        elif choice == "5":
            print("Your data has been saved. Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
