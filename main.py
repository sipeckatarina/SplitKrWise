import startno_okno as sto
import class_window as cw

EURO = 1
KUNE = 7.38
USD = 1.16

number_people = int(sto.Start_number().number_people)

if number_people == 1000:
    with open('memory.txt') as mem:
        people = []
        for per in mem:
            per = per.split(', ')
            per_name = per[0]
            per_balance = float(per[1][:-1])
            people.append(cw.Person(per_name, per_balance))
    cw.Main_window(people)
else:
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
