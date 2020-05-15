import query_db as qdb
import login
import getpass as pas 

def cashAdd(username,password):
	account_number, balance, __, __ = qdb.query_db(qdb.customer_info_query,username,password)[0]
	amount = int(input("Enter the amount you want to deposit: "))
	final_amount = int(balance) + amount
	qdb.query_db(qdb.transfer_to_query,amount,account_number)
	#We have to check this
	#update the log
	print('The deposit of {} was successful for account number {} you now have a balance of {}'.format(amount,account_number,final_amount))
	return True

def cashRemove(username,password):
	account_number, balance, __, __ = qdb.query_db(qdb.customer_info_query,username,password)[0]
	amount = int(input("Enter the amount you would like to withdraw: "))
	if amount <= int(balance):
		final_amount = int(balance) - amount
		qdb.query_db(qdb.transfer_from_query,amount,account_number)
		print('Withdrawal successful please take your cash!, your current balance is {}'.format(final_amount))
		return True
	else:
		print('Insufficient Funds!')
		return False

def transfercash(account_number):
	try:
		receiver_name = input('Recipients full name: ')
		receiver_acc_num = int(input('Recipient\'s Account Number: '))
		amount_send = int(input('Amount you want to transfer: '))
		rcv_acc_num = qdb.query_db(qdb.check_account_query,receiver_acc_num)[0]
		if receiver_acc_num not in rcv_acc_num:
			print('Recipient does not exist')
	except:
		print('Something went wrong :)')
		return False	

	try:
		account_number, balance = qdb.query_db(qdb.customer_transfer_query,account_number, amount_send)[0]
		print('You have transferred {} to {}'.format(amount_send,receiver_name))
	except:
		print('Insufficient Funds to complete this operation')
		#print('This account belongs to {}'.format(receiver_name))
		#print(account_number)
	qdb.query_db(qdb.transfer_from_query,amount_send,account_number)
	qdb.query_db(qdb.transfer_to_query,amount_send,receiver_acc_num)


#else:
#print('There is no sufficient funds to complete this operation')
#if amount_send >= int(balance):
			#final_amount = int(balance) - amount_send
			
def accNew():
	new_name = input('Enter your Full Name: ')
	new_user = input('Enter a unique username: ')
	# condition to check if username exists in the database
	new_pass = pas.getpass(prompt='Enter password: ')
	gend = input('Enter your gender either F or M: ')
	mail_add = input('Enter your email address: ')
	d_of_b = input('Enter your date of birth in this format yyyy-mm-dd: ')

	qdb.query_db(qdb.insert_cusomer_data_query, new_name, new_user, new_pass, gend, mail_add, d_of_b)
	
	#Update the database with the value transferred to the beneficiary
	#Send a mail notifying the recipient of the successful transfer
		
	
