from docx import Document
import random

names = ['Alex', 'Grace', 'Charlie', 'Karen', 'Eric', 'Joanne', 'Delfina', 'Papa and Judy']
random.shuffle(names)

print(names)

alex_count = 0
grace_count = 0
charlie_count = 0
karen_count = 0
eric_count = 0
joanne_count = 0
delfina_count = 0
papajudy_count = 0

for name in names:
    names_copy = names[:]
    names_copy.remove(name)
    person1_choices = []
    while len(person1_choices) !=3:
        choice = random.choice(names_copy)
        if choice not in person1_choices:
            if choice == 'Alex':
                if alex_count <3:
                    person1_choices.append(choice)
                    alex_count+=1
            elif choice == 'Grace':
                if grace_count <3:
                    person1_choices.append(choice)
                    grace_count+=1
            elif choice == 'Charlie':
                if charlie_count <3:
                    person1_choices.append(choice)
                    charlie_count+=1
            elif choice == 'Karen':
                if karen_count <3:
                    person1_choices.append(choice)
                    karen_count+=1
            elif choice == 'Eric':
                if eric_count <3:
                    person1_choices.append(choice)
                    eric_count+=1
            elif choice == 'Joanne':
                if joanne_count <3:
                    person1_choices.append(choice)
                    joanne_count+=1
            elif choice == 'Delfina':
                if delfina_count <3:
                    person1_choices.append(choice)
                    delfina_count+=1
            else:
                if papajudy_count <3:
                    person1_choices.append(choice)
                    papajudy_count+=1
    print(name)
    print(person1_choices)

    document = Document()
    document.add_heading('Secret Santa', 0)
    document.add_paragraph('You are: ' + name)
    document.add_paragraph('Your assigned people to get presents for: ')
    document.add_paragraph(person1_choices[0], style='List Bullet')
    document.add_paragraph(person1_choices[1], style='List Bullet')
    document.add_paragraph(person1_choices[2], style='List Bullet')
    document.add_paragraph('Yay! Merry Xmas! :)')
    document.save(name +"_secret_santa.docx")

