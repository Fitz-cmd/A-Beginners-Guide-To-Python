#It is also possible to indicate alignment and width within the format string. 
# For example, 
# if you wish to indicate a width to be left for a placeholder whatever the actual value supplied, 
# you can do this using a colon (':') followed by the width to use. 
# For example to specify a gap of 25 characters which can be filled with a substitute value 
# you can use {:25} as shown below:
print('|{:25}|'.format('25 characters width'))
print('|{:<25}|'.format('left aligned')) # The default 
print('|{:>25}|'.format('right aligned')) 
print('|{:^25}|'.format('centered'))
# Can format numbers with comma as thousands separator 
print('{:,}'.format(1234567890)) 
print('{:,}'.format(1234567890.0))