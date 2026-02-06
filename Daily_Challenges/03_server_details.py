#create variable called server set equal to dictionary
server = {
    'type': 't2.micro',
    'ip': '192.168.1.1',
    'status': 'active',
    'owner': 'Zachary',
}

#print the value of the ip key in the server dictionary
# print(server['ip'])

choice = input('What would you like to know? (type/ip/status/owner):')
if choice in server: 
    print(f'The {choice} of the server is: {server[choice]}')
else:
    print('Sorry, that is not a valid choice.')
    
