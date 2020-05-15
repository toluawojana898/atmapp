import query_db as qdb
import login
import getpass as pas 
from datetime import date
import logging

def accNew():
	check_account = qdb.query_db(qdb.account_query) #Check for account details
	check_user_name = qdb.query_db(qdb.username_query)
	new_account_number = [] #Account should automatically update from the SQL autoincrement
	new_name = input('Enter your Full Name: ')
	new_user = input('Enter a login username: ')
	opening_balance = int(input('How much would you like to open the account with: '))	
	account_type = input('Enter account type, "SAVINGS" or "CURRENT": ').upper()
	new_pass = pas.getpass(prompt='Enter your password: ')
	gender = input('Enter your gender either "F" or "M": ')
	mail_add = input('Enter your email address: ')
	d_of_b = input(input('Enter your date of birth in this format YYYY-MM-DD: '))
	d_of_b = date(d_of_b)

	# condition to check if username exists in the database
	while new_user in check_user_name:
		print('username already exists! Please enter a unique username')
		new_user = input('Enter a unique login username: ')


	qdb.query_db(qdb.insert_account_data_query, acc_id, acc_num, balance, account_type))
	qdb.query_db(qdb.insert_cusomer_data_query, new_name, new_user, new_pass, gender, mail_add, d_of_b)
