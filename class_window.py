import tkinter as tk
from people import Person


class Main():

    #people je spisek oseb Person(ime, stevilo)
    def __init__(self, people):

        self.people = people

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
        tk.Label(self.down, text='hudo').pack()




Main([Person('Katja', 10), Person('Andraž', 8)])