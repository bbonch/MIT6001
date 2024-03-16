balance = 4773
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12

min_amount = 10
while True:
    r_balance = balance
    for m in range(12):
        unpaid_balance = r_balance - min_amount
        r_balance = unpaid_balance + monthlyInterestRate * unpaid_balance

    if r_balance <= 0:
        break

    min_amount += 10

print("Lowest Payment:", min_amount)
