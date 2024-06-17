"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Dominique Blair
Date:   May 9, 2024
"""

import currency

from_currency     = input('3-letter code for original currency: ')
to_currency       = input('3-letter code for the new currency: ')

from_amt = float(input('Amount of the original currency: '))
to_amt   = round(currency.exchange(from_currency, to_currency, from_amt),3)

result   =  'You can exchange ' +str(from_amt)+ ' '+from_currency+' for '+str(to_amt)+' '+to_currency+'.'

print(result)