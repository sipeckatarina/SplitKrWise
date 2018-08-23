import startno_okno as sto
import people as p
import class_window as cw

number_people = int(sto.Start_number().number_people)

names = []
for person in sto.Start_names(number_people).names:
    names.append(person[0].upper() + person[1:])

person = []
for name in names:
    person.append(p.Person(name))