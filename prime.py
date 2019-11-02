n=1,2,3,4,5,6

#p=11
p=input("Enter a no to check=")
print(type(p))
for i in range(2,p):	
	
	if p%i==0:
		print ("Not Prime")
		break
	else:
		print ("Prime")
		break
