import math

def humanReadable(value):

	if value <10E6:
		suffix = 'n'
	elif value < 10E3:
		suffix = 'u'
	elif value < 1:
		suffix = 'm'
	elif value < 1000:
		suffix = ''
	elif value < 1E6:
		suffix = 'K'
	elif value < 1E9:
		suffix = 'M'
	elif value < 1E12:
		suffix = 'B'
	else:
		suffix = 'T'

	string = '{0:.2f}{1}'.format(value, suffix)
	return string

def toNumber(value):
	if isinstance(value, (list, tuple, set)):
		converted_number = [toNumber(i) for i in value]
	if isinstance(value, str):
		if '.' in value:
			converted_number = float(value)
		else:
			converted_number = int(value)
	elif isinstance(value, (int, float)):
		converted_number = value
	else:
		try:
			converted_number = float(value)
		except:
			converted_number = math.nan
	return converted_number