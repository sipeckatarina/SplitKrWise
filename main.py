import startno_okno as sto
import class_window as cw


number_people = int(sto.Start_number().number_people)

names = []
for person in sto.Start_names(number_people).names:
    if len(person) > 1:
        names.append(person[0].upper() + person[1:])
    else:
        names.append(person)

people = []
for name in names:
    people.append(cw.Person(name))

cw.Main_window(people)

'''
MEPIjanke = []
MEPIjanke.append(cw.Person('Vodnik'))
MEPIjanke.append(cw.Person('Minatti'))
MEPIjanke.append(cw.Person('Tišler'))
MEPIjanke.append(cw.Person('Blaznik'))
MEPIjanke.append(cw.Person('Podlogar'))
MEPIjanke.append(cw.Person('Šipec'))
cw.Main_window(MEPIjanke)
'''