# 7-8 Deli Sandwiches

sandwich_orders = ['tuna', 'turkey', 'ham', 'veggie', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:
    print(sandwich)