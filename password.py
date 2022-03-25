i = 0
while i <= 2:
	password = input('Please enter your password: ')

	if password == 'a123456':
		print('Login Successfully!')
		break

	if i == 2:
		print('You lose')
		break 

	else:
		print('Login Failed. You have ', 2-i, ' times left')
		i = i + 1


	


