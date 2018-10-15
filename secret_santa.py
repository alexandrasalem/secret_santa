from docx import Document
import random

names = ['Alex', 'Grace', 'Charlie', 'Karen', 'Eric', 'Joanne', 'Delfina', 'Papa and Judy']
random.shuffle(names)

print(names)

for x in names:
	names_copy = names[:]
	names_copy.remove(x)
	person1_choices = []
	while len(person1_choices) !=3:
		choice = random.choice(names_copy)
		if choice not in person1_choices:
			person1_choices.append(choice)
	print(x)
	print(person1_choices)

