# Original guest list
guest_list = ["Bob Marley", "Denzel Washington", "Jackie Chan"]

# Sending invitation messages
for guest in guest_list:
    print(f"Dear {guest}, I would love to invite you to dinner. Please join me!")

# Informing that a bigger dinner table is available
print("\nGreat news! I found a bigger dinner table, so I’m inviting more guests!\n")

# Adding more guests
guest_list.insert(0, "Michael Jackson")  # Beginning of the list
guest_list.insert(2, "Bruce Lee")        # Middle of the list
guest_list.append("Oprah Winfrey")       # End of the list

# Sorting the list in alphabetical order
guest_list.sort()

# Sending new invitations
for guest in guest_list:
    print(f"Dear {guest}, I would love to invite you to dinner. Please join me!")

# Code for slicing the list
print("\nSlicing the guest list:\n")

# Slice for the first three items
print("The first three items in the list are:")
print(guest_list[:3])

# Slice for the three items from the middle of the list
print("\nThree items from the middle of the list are:")
middle_index = len(guest_list) // 2  # Find the middle index
print(guest_list[middle_index - 1:middle_index + 2])  # Adjust slice to get 3 items

# Slice for the last three items
print("\nThe last three items in the list are:")
print(guest_list[-3:])