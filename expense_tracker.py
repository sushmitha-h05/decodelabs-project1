def display_banner():
    print("=" * 50)
    print("   💰 DECODELABS EXPENSE TRACKER 💰")
    print("   Track every rupee. Miss nothing.")
    print("=" * 50)

def display_summary(expenses: list, total: float):
    print("\n📊 --- SESSION SUMMARY ---")
    for i, amount in enumerate(expenses, start=1):
        print(f"   Transaction {i:02d}  →  ₹{amount:.2f}")
    print("-" * 30)
    print(f"   Total Spent   →  ₹{total:.2f}")
    print(f"   Transactions  →  {len(expenses)}")
    print("=" * 50)

def run_tracker():
    display_banner()
    print("\nEnter expense amounts one by one.")
    print("Type  'quit'  to stop and see your total.\n")

 
    total = 0.0
    expenses = []

    while True:
        raw = input("Enter expense (or 'quit'): ").strip()


        if raw.lower() == "quit":
            break

        try:
            amount = float(raw)
            if amount < 0:
                print("⚠️  Negative expense? Enter a positive number.\n")
                continue
        except ValueError:
            print("❌  Invalid input. Enter a number like 100 or 49.99\n")
            continue

    
        total += amount
        expenses.append(amount)
        print(f"✅  Added ₹{amount:.2f}  |  Running Total: ₹{total:.2f}\n")


    if expenses:
        display_summary(expenses, total)
    else:
        print("\n⚠️  No expenses recorded. Nothing to show.")
        print("=" * 50)


if __name__ == "__main__":
    run_tracker()