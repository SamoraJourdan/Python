messages = ['hello', 'boop', 'soup']
sent_messages = []
def print_messages(messages):
	for message in messages:
		print(message)
print_messages(messages)

def send_messages(messages, sent_messages):
	while messages:
		message = messages.pop()
		print(message)
		sent_messages.append(message)

		 
#print_messages(messages)
#send_messages(messages, sent_messages)
#print(messages)
#print(sent_messages)
send_messages(messages [:], sent_messages)
print(messages)
print(sent_messages)