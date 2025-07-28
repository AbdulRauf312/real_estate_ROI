def calculate_roi(price_wan, rent_monthly, occupancy, interest_rate, loan_years):
    # Convert price from wan to RMB
    price_rmb = price_wan * 10000  # 1 wan = 10,000 RMB

    # Monthly values
    r_monthly = interest_rate / 12
    n_months = loan_years * 12
    rent_annual = rent_monthly * 12 * occupancy

    # Monthly mortgage payment (annuity formula)
    monthly_payment = (price_rmb * r_monthly * (1 + r_monthly)**n_months) / ((1 + r_monthly)**n_months - 1)

    # Initialize lists for plotting
    annual_cashflow = []
    cumulative_equity = []
    remaining_balance = []
    equity = 0
    balance = price_rmb  # Use price_rmb instead of price

    for year in range(1, loan_years + 1):
        interest_paid = 0
        principal_paid = 0
        for _ in range(12):
            interest = balance * r_monthly
            principal = monthly_payment - interest
            balance -= principal
            interest_paid += interest
            principal_paid += principal

        # Annual cashflow is rent income minus the annual mortgage payment
        yearly_cashflow = rent_annual - (monthly_payment * 12)
        equity += principal_paid

        # Append the results for plotting
        annual_cashflow.append(yearly_cashflow)
        cumulative_equity.append(equity)
        remaining_balance.append(balance)

    return annual_cashflow, cumulative_equity, remaining_balance, rent_annual, monthly_payment
