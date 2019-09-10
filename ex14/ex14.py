from sys import argv

script , user_name = argv
prompt = '> '

print(f"Hi the {user_name}, I am the {script} script.")
print("I'd like to ask you few questions")
print(f"do you like me {user_name}?")
likes = input(prompt)

print(f"Whre do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computers = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have {computers} computer . Nice.
""")
