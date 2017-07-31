# prompt for hours and rate to compute pay with overtime calculation
# catching exceptions with try and except
# updated with a function

def computepay(hours, rate):
    overtime = hours - 40
    if hours > 40:
        pay = (40 * rate) + (overtime * rate * 1.5)
        pay = '${:,.2f}'.format(pay) #converts the float value to a currency dollars
        return pay
    else:
        pay = hours * rate
        pay = '${:,.2f}'.format(pay)
        return pay

try:
    hours = raw_input('How many hours did you work? ')
    hours = float(hours)
    rate = raw_input('How much did you get payed each hour? ')
    rate = float(rate)
except:
    print 'Error, please enter numeric input.'

pay = computepay(hours, rate)

print 'Pay:', pay

Lesley is here.
