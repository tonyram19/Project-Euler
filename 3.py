#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def checkPrime(number):

	divisorCounter = 0
	i = 2

	while i <= number:
		if number % i == 0:
			divisorCounter = divisorCounter + 1

		if divisorCounter > 1:
			return False

		i = i + 1
		
	return True
	
number = 600851475143
i = 2

while i <= number:
	if number % i == 0:
		if checkPrime(i) == True:
			print i
	i = i + 1				