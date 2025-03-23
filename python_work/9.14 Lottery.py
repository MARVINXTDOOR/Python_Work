# Step 1: import the random module
import random

# Step 2: Create a list with 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Step 3: Randomly select 4 numbers or letters
winning_ticket = random.sample(lottery_pool, 4)

# Step 4: Print the winning ticket message
print("Any ticket matching these 4 numbers or letters wins a prize!")
print(f"Winning ticket: {winning_ticket}")