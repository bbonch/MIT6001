balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12
lower = balance / 12
upper = (balance * ((1 + monthlyInterestRate) ** 12)) / 12

min_amount = (upper + lower) / 2
while True:
    r_balance = balance
    for m in range(12):
        unpaid_balance = r_balance - min_amount
        r_balance = unpaid_balance + monthlyInterestRate * unpaid_balance

    if r_balance <= 0:
        upper = min_amount
    else:
        lower = min_amount
    if round(upper, 2) == round(lower, 2):
        break

    min_amount = (upper + lower) / 2

print("Lowest Payment:", round(min_amount, 2))
