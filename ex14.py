#Exercise 14 - Prompting and Passing

from sys import argv

script, user_name, time = argv
prompt = '# '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me. (I won't hold it against you.)
You live in {lives}. Not sure where that is because I don't have a module for that... yet.
And you have a {computer} computer. Not a bad machine, it's nice in here.
You said it was {time} at the very beginning.
""")
