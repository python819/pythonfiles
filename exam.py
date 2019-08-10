#module 1:--
#1
#for j in range(1,6):
#	print('*'*j)
#2
'''
a=input('enter the password')
if len(a)>=6 and len(a)<=12:
	if a.isalpha() is True:
		print('should contain atleast one special symboland one number')
	elif a.isalnum() is True:
		print('should contain atleast one special symbol')
	elif a.islower() is True :
		print('should contain atleast one uppercase')
	elif a.isupper() is True :
		print('should contain atleast one lowercase')
	else:
		print('strong password')
else:
	print('passowrd shoulb be min of 6 and max of 12 characters' )
'''
#3
a=[]
for j in range(0,5):
	a[j]=input('enter the elements')
print(a.sort())

