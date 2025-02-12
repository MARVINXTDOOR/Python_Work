# Initial guest list
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
