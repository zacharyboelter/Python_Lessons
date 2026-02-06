# Initialize an empty list to store the inventory of servers
inventory = []

print("--- AWS Resource Provider ---")

#Prompt the user to enter three different types of servers and add them to the inventory list
server1 = input("Enter first server type (e.g., ts2.micro): ")
inventory.append(server1)

server2 = input("Enter second server type: ")
inventory.append(server2)

server3 = input("Enter third server type: ")
inventory.append(server3)

# Display the inventory of servers
print("\nYour Current Cloud Inventory:")
print(inventory)

# Bonus: Check if you have a 'heavy' server in your inventory and print a message if you do
if "t2.large" in inventory:
    print("\nYou have a heavy server in your inventory!")

    