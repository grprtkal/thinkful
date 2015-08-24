def fizzbuzz(a, b): 
	for i in xrange(a, b):
		if i % 3 == 0 and i % 5 == 0: 
			print("FizzBuzz")
		elif i % 3 == 0: 
			print("Fizz")
		elif i % 5 == 0: 
			print("Buzz")	
		else: 
			print(i)

fizzbuzz(1, 101)