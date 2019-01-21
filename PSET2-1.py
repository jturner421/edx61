balance = 4213
# totalPaymnets = 0
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthly_int_rate = annualInterestRate / 12.0
interest = 0
# cumPay = 0
totalPaid = 0


def min_payment(balance, monthlyPaymentRate):
    return balance * monthlyPaymentRate


def unpaidBalance(balance, minPay):
    return balance - minPay


def interestPer(unpaid_bal, monthlyIntrate):
    return unpaid_bal * monthlyIntRate


count = 0
while count <= 11:
    # computer monthly min payment
    # remBalance = balance + interest
    minPay = round(min_payment(balance, monthlyPaymentRate), 2)
    # compute the unpaid balance
    unpaidBal = round(unpaidBalance(balance, minPay), 2)
    # calculate interest
    interest = round(interestPer(unpaidBal, monthlyIntRate), 2)
    totalPaid = totalPaid + minPay
    balance = unpaidBal + interest
    per = count + 1
    print('Month:  ' + str(per))
    print('Minimum monthly Payment:  ' + str(minPay))
    print('Remaining balance: ' + str(balance))
    count += 1

print('Total paid: ' + str(totalPaid))
print('Remaining balance: ' + str(balance))
