balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12

for m in range(12):
    min_monthly_payment = balance * monthlyPaymentRate
    unpaid_balance = balance - min_monthly_payment
    balance = unpaid_balance + monthlyInterestRate * unpaid_balance

print("Remaining balance:", round(balance, 2))
