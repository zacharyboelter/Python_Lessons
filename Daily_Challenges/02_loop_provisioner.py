
# names = ["John", "Jane", "Doe", "Smith", "Alice", "Bob", "Charlie", "Zachary", "David", "Eve", "Frank"]

# for name in names:
#     if name == "Zachary":
#         print(f"Hey {name}! That's my name!")
#     else:
#         print(f'Hello {name}, come join the party!')


roles = ["web", "database", "cache", "load balancer", "worker", "scheduler"]

print("--- Automated Provisioning Sequence ---")

# Loop through each role and simulate provisioning

for role in roles:
    print(f'Provisioning a new {role} server...')
    print(f'SUCCESS: {role} is now live.\n')

print("--- All servers have been provisioned successfully! ---")