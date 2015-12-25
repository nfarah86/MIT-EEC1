def mult(a,b):
	if a==0:
		return 0
	else:
		return b + mult(a-1,b)

print (mult(3,4))



def bin(n):
	if n == 0:
		return '0'
	elif n == 1:
		return '1'
	else:
		return bin(int(n/2)) + bin(int(n%2)) 

print(bin(3))
print(bin(132))