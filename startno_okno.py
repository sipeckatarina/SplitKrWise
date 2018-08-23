import tkinter as tk


class Start_number():

    def __init__(self):

        self.number_people = 0

        self.root = tk.Tk()
        self.root.title('SplitKrWise')
        #self.root.geometry("300x200")

        self.up = tk.Frame(self.root)
        self.up.grid(row=1)
        self.down = tk.Frame(self.root)
        self.down.grid(row=2)

        self.empty_row = tk.Label(self.up)
        self.empty_row.grid(row=1)

        self.number_label = tk.Label(self.up, text='Vpišite število oseb: ')
        self.number_label.grid(row=3, column=1)
        self.number_entry = tk.Entry(self.up)
        self.number_entry.grid(row=3, column=2)

        self.people_label = tk.Label(self.down, text='Privzeto število oseb je 4.', fg='grey')
        self.people_label.grid(row=1)

        self.empty_row2 = tk.Label(self.down)
        self.empty_row2.grid(row=2)

        self.ok = tk.Button(self.down, text='OK', command=self.ok)
        self.ok.grid(row=3)

        self.empty_row3 = tk.Label(self.down)
        self.empty_row3.grid(row=4)


        self.root.mainloop()

    def ok(self):
        self.number_people = self.number_entry.get()
        if self.number_people.isdigit():
            self.number_people = int(self.number_people)
            self.root.destroy()
        elif self.number_people == '':
            self.number_people = 4
            self.root.destroy()
        else:
            warning = tk.Label(self.down, text='Prosim, vpišite naravno število.')
            warning.grid(row=1)

#Startno_okno()


class Ent():

    def __init__(self, i, window):
        self.i = i
        self.ent = tk.Entry(window)

    def __repr__(self):
        return 'Ent #{}'.format(self.i)

    def show(self):
        self.ent.grid(row=self.i)


class Start_names():

    def __init__(self, number_people=4):

        self.number_people = number_people

        self.root = tk.Tk()
        self.root.title('SplitKrWise')

        self.up = tk.Frame(self.root)
        self.up.grid(row=1)
        self.mid = tk.Frame(self.root)
        self.mid.grid(row=2)
        self.down = tk.Frame(self.root)
        self.down.grid(row=3)

        self.left = tk.Frame(self.mid)
        self.left.grid(row=1, column=1)
        self.right = tk.Frame(self.mid)
        self.right.grid(row=1, column=2)

        self.ok = tk.Button(self.down, text='OK', command=self.ok)
        self.ok.pack()

        self.construct_tab()


        self.root.mainloop()

    def construct_tab(self):
        tab = []
        for i in range(self.number_people):
            tk.Label(self.left, text='Vpišite ime: ').grid(row=i)
            ent = Ent(i, self.right)
            ent.show()
            tab.append(ent)
        self.tab = tab

    def make_list(self):
        self.names = []
        for i in range(self.number_people):
            name = self.tab[i].ent.get()
            self.names.append(name)

    def ok(self):
        self.make_list()
        self.root.destroy()