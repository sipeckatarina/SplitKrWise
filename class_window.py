import tkinter as tk

EURO = 1
KUNE = 7.38
USD = 1.16

class Person():

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return 'Person({},{})'.format(self.name, self.balance)

    def __str__(self):
        x = ''
        if self.balance < 0:
            x = 'owes'
            bal = 0 - self.balance
        else:
            x = 'gets'
            bal = self.balance
        return 'A person named {} who '.format(self.name) + x + ' {} euros.'.format(bal)

    def gives(self, amount, *args):
        money = amount / (len(args[0]))
        money = float("{0:.2f}".format(money))
        self.balance += amount
        for person in args:
            for p in person:
                p.balance = p.balance -   money

#__________________________________________________________________________________________________________

class Main_window():

    #people je spisek oseb Person(ime, stevilo)
    def __init__(self, people):

        self.people = people
        self.number_people = len(people)

        self.root = tk.Tk()
        self.root.title('SplitKrWise')

        self.up = tk.Frame(self.root)
        self.mid = tk.Frame(self.root)
        self.down = tk.Frame(self.root)
        self.up.grid(row=1, column=1)
        self.mid.grid(row=2, column=1)
        self.down.grid(row=3, column=1)

        self.left = tk.Frame(self.mid)
        self.right = tk.Frame(self.mid)
        self.left.grid(row=1, column=1)
        self.right.grid(row=1, column=2)

        self.label = tk.Label(self.up, text='Trenutno stanje: ', fg='blue')
        self.label.pack()

        self.er3 = tk.Label(self.up)
        self.er3.pack()

        self.write()

        self.er2 = tk.Label(self.down)
        self.er2.pack()

        self.change_button = tk.Button(self.down, text='SPREMENI', command=self.change)
        self.change_button.pack()

        self.er4 = tk.Label(self.down)
        self.er4.pack()

        self.root.mainloop()

    def write(self):
        for i in range(len(self.people)):
            name = tk.Label(self.left, text=self.people[i].name)
            num = tk.Label(self.right, text=str(self.people[i].balance))
            name.grid(row=i)
            num.grid(row=i)

    def change(self):
        self.root.destroy()
        Change_window(self.people)

#__________________________________________________________________________________________________________

class Buttonn():

    def __init__(self, x, y, window, person, l):
        self.x = x
        self.y = y
        self.window = window
        self.person = person
        self.l = l
        self.button = tk.Button(self.window, text=person.name, command=self.press)

    def __repr__(self):
        return 'Button({}, {}, {}, {})'.format(self.x, self.y, self.window, self.person)

    def __str__(self):
        return 'Button of a person {} on ({}, {}) in {}.'.format(self.person, self.x, self.y, self.window)

    def write(self):
        self.button.grid(row=self.x, column=self.y)

    def press(self):
        if self.button.config('relief')[-1] == 'raised':
            self.button.config(relief='sunken', bg='grey83')
            self.l.append(self.person)
        else:
            self.button.config(relief='raised', bg='grey93')
            self.l.remove(self.person)


class Change_window():

    def __init__(self, people):

        self.people = people
        self.number_people = people
        self.amount = 0

        self.root = tk.Tk()
        self.root.title('SplitKrWise')
        self.l = []

        #razdeljeno okno na 5 delov
        self.up = tk.Frame(self.root)
        self.upmid = tk.Frame(self.root)
        self.mid = tk.Frame(self.root)
        self.downmid = tk.Frame(self.root)
        self.down = tk.Frame(self.root)
        self.downdown = tk.Frame(self.root)
        self.up.grid(row=1, column=1)
        self.upmid.grid(row=2, column=1)
        self.mid.grid(row=3, column=1)
        self.downmid.grid(row=4, column=1)
        self.down.grid(row=5, column=1)
        self.downdown.grid(row=6, column=1)

        #napis zgoraj
        tk.Label(self.up, text='Kdo je plačal?').pack()
        self.write_pays()
        tk.Label(self.mid, text='Za koga je plačal?').pack()
        self.write_owes()

        self.amount_label = tk.Label(self.down, text='Znesek: ')
        self.amount_entry = tk.Entry(self.down)
        self.amount_label.grid(row=1, column=1)
        self.amount_entry.grid(row=1, column=2)

        tk.Button(self.downdown, text='OK', command=self.close).pack()


        self.root.mainloop()

    def write_pays(self):
        self.tab_buttons_up = []
        for i in range(len(self.people)):
            per = Buttonn(i, 1, self.upmid, self.people[i], self.l)
            b = per.button
            b.grid(row=1, column=i+1)
            self.tab_buttons_up.append(b)

    def write_owes(self):
        self.tab_buttons_down = []
        for i in range(len(self.people)):
            per = Buttonn(i, 1, self.downmid, self.people[i], self.l)
            b = per.button
            b.grid(row=1, column=i+1)
            self.tab_buttons_down.append(b)

    def close(self):
        self.amount = self.amount_entry.get()
        if self.amount.isdigit():
            p = self.l
            p[0].gives(int(self.amount), p[1:])
            self.root.destroy()
            self.memory_update()
            Main_window(self.people)
        else:
            tk.Label(self.downdown, text='Vpišite naravno število.').pack()

    def memory_update(self):
        with open('memory.txt', 'w') as mem:
            for person in self.people:
                print('{}, {}'.format(person.name, person.balance), file=mem)
