

number_prompt = "How many tickets would you like? "
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    tickets = input(number_prompt)
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your tickets is $10.")
    else:
        print("  Your tickets is $15.")