import sys

def list1_minus_list2(list1, list2):
	new_list = [x for x in list1 if x not in list2]
	return new_list

def marketing():

	clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
	participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
	recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

	contact_list = clients + participants
	contact_list = list(set(contact_list))
	contact_set = set(contact_list)
	if sys.argv[1] == 'call_center':
		lst = list1_minus_list2(clients, recipients)
		lst.append('jessica@gmail.com')
		print('clients =', lst)
	if sys.argv[1] == 'potential_clients':
		print('participants =', list1_minus_list2(participants, clients))
	if sys.argv[1] == 'loyalty_program':
		print('recipients =', list1_minus_list2(clients, participants))

if __name__ == '__main__':
	if len (sys.argv) != 2 or (sys.argv[1] != 'call_center' and sys.argv[1] != 'potential_clients' and sys.argv[1] != 'loyalty_program'):
		raise Exception("Error argument")
	marketing()