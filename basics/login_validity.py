def login_validity(username,password):
	if username == 'admin' and password == 'admin@123':
		return True
	return False


def login():
	response = login_validity('admin','admin@123')
	if response :
		print("login successful")
	else:
		print("wrong creds")

login()
