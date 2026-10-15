def calculate_finances(
    monthly_income: float, tax_rate: float, currency: str = "USD"
) -> None:
    """
    Calculate annual and monthly net/gross income and taxes,
    then format and print the financial breakdown.
    """
    yearly_salary: float = monthly_income * 12
    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_net_income: float = yearly_salary - yearly_tax

    # formatting output inside a clean visual block
    print("==============================================")
    print(f"{'FINANCIAL SUMMARY':^35}")
    print("=" * 35)
    print(f"Monthly income:      {currency} {monthly_income:,.2f}")
    print(f"Tax rate:            {tax_rate:.1f}%")
    print(f"Monthly tax:         {currency} {monthly_tax:,.2f}")
    print(f"Monthly net income:  {currency} {monthly_net_income:,.2f}")
    print("-" * 35)
    print(f"Yearly salary:       {currency} {yearly_salary:,.2f}")
    print(f"Yearly tax paid:     {currency} {yearly_tax:,.2f}")
    print(f"Yearly net income:   {currency} {yearly_net_income:,.2f}")
    print("==============================================")


def main() -> None:
    """Main entry point of the financial calculator CLI."""
    print("============ Financial Calculator ============")
    # safe input handling with try-except loop
    while True:
        try:
            monthly_income: float = float(input("Enter your monthly income: "))
            tax_rate: float = float(input("Enter your tax rate (%): "))
            break
        except ValueError:
            print("Error: Please enter a valid number. Try again.\n")
    currency: str = (
        input("Enter currency symbol (e.g., USD, EUR, KR): ").strip().upper() or "USD"
    )

    calculate_finances(monthly_income, tax_rate, currency=currency)


if __name__ == "__main__":
    main()
