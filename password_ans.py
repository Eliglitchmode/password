password = "a123456"
i = 3 # times left
while True:
	pwd = input('Please enter your password: ')	
	if pwd == password:
		print('Successfully Signed In!')
		break # exit loop
	else:
		i = i - 1
		print('Wrong! You have ', i,' times left!')
		if i == 0:
			break


