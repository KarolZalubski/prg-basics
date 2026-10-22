### 1-4
# Credit card payment 
#
account_balance = 500
total_payment = int(input("Podaj kwotę płatności: "))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')