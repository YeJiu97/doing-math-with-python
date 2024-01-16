def is_factor(num):
	'''find all positive factors'''
	for i in range(1, b+1):
		if b % i == 0:
			return True
		else:
			return False


if __name__ == '__main__':
	
	b = input('Your number please')
	b = float(b)

	if b > 0 and b.is_integer():
		factors(int(b))
	else:
		print("Please enter a positive integer")