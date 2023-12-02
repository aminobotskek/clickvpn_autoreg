import clickvpn , temp_mail
# https://github.com/aminobotskek/clickvpn/blob/main/clickvpn.py
# https://github.com/aminobotskek/temp_mail/blob/main/temp_mail.py
def save_account(email,password):
	accounts= open("accounts.txt", "a+")
	accounts.write(f"{email}:{password}\n")
	accounts.close()
def main():
	try:
		client=clickvpn.Client()
		email=temp_mail.Client().new_email()['email']
		client.register(email=email,password=password)
		print(f"account {email} register")
		save_account(email=email,password=password)
	except Exception as e:
		print(e)
password=input("password»")
while True:
	main()