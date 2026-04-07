# 3-8. My Updated Guest List - Sorted

guests = ["Nikola Tesla", "Ada Lovelace", "Alan Turing"]

print("Good news! I found a bigger dinner table, so more guests are invited.\n")

# Add new guests
guests.insert(0, "Grace Hopper")            # beginning
guests.insert(2, "Katherine Johnson")       # middle
guests.append("Linus Torvalds")              # end

# Sort alphabetically
guests.sort()

# Print sorted invitations
for guest in guests:
    print(f"{guest}, you are invited to dinner!")

# --- SLICES SECTION ---

print("\nThe first three items in the list are:")
print(guests[:3])

print("\nThree items from the middle of the list are:")
middle_index = len(guests) // 2
print(guests[middle_index - 1:middle_index + 2])

print("\nThe last three items in the list are:")
print(guests[-3:])