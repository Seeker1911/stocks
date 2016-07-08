stockDict = { 'GM': 'General Motors', 
			 'CAT':'Caterpillar', 'EK':"Eastman Kodak" }

purchases = [ ( 'GM', 100, '10-sep-2001', 48 ), 
			 ( 'CAT', 100, '1-apr-1999', 24 ), 
			 ( 'EK', 200, '1-jul-1998', 56 ) ]

'''
A set with ticker symbols, prices, dates and number of shares.
'''
# Compute the purchase price (shares * dollars) for each stock
for p in purchases:
	total_price = p[1] * p[3]
	company_ticker = p[0]
	company_name = stockDict[company_ticker]
	print('{0} for {1}'.format(total_price, company_ticker))

# [print('you bought {0} shares at ${1}'.format(p[1], p[3])) for p in purchases]

output = ['you bought {0} shares '.format(p[1])]
output.append('of {0} '.format(company_name))
output.append('at ${0}/share '.format(p[3]))
output.append('for a total price of ${0}'.format(total_price))
print(''.join(string for string in output))
