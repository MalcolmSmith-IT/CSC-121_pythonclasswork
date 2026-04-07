# 7-5 Movie Tickets

total_cost = 0

num_tickets = int(input("How many tickets do you need? "))

for i in range(num_tickets):
    age = int(input(f"Enter the age of ticket holder #{i + 1}: "))

    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15

    total_cost += cost

print(f"\nThe total cost of the tickets is: ${total_cost}")