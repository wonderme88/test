n=1,2,3,4,5,6

#p=11
p=int(input("Enter any no to check="))

if p>1:

	for i in range(2,p):	
	
		if p%i==0:
			print (p,' is Not a Prime')
			break
	else:
		print (p,'is a Prime Number')
			
else:
	print(p," is not a prime number")
