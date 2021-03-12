from random import choice

questions = ["Why is the sky blue?: ", "Why do people poop?: ", "Why dont you have any hair?: "]
question = choice(questions)
answer = input(question).strip()
while answer.lower() != "just because":
	answer = input("Why?: ").strip()
print("Oh... Okay")	