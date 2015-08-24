# 0, 1, 1, 2, 3, 5, etc.
#F(0), F(1), F(2), F(3), F(4), F(5), etc.

def F(n): 
	if n < 2: 
		print("hello")
		return n
	else: 
		return F(n-2) + F(n-1)

print(F(4))


# Examples: 
# def F(3): 
# 	if n < 2: 
# 		return n
# 	else:
# 		return F(3-2) + F(3-1)
		# F(1) + F(2)
		# 1 + F(2-2) + F(2-1)
		# 1 + 0 + 1
		# 2 
#output of F(3) is 2.

# def F(4): 
# 	if n < 2: 
# 		return n
# 	else: 
# 		return F(4-2) + F(4-1)
		# F(2) + F(3)
		# F(2-2) + F(2-1) + F(3-2) + F(3-1)
		# F(0) + F(1) + F(1) + F(2)
		# 0 + 1 + 1 + F(2-2) + F(2-1)
		# 0 + 1 + 1 + 0 + 1
		# 3
#output of F(4) is 3.
