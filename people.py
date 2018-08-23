import tkinter as tk

#balance pomeni koliko denarja oseba dobi iz skupnega
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
        else:
            x = 'gets'
        return 'A person named {} who '.format(self.name) + x + ' {} euros.'.format(self.balance)

    def gives(self, amount, *args):
        money = amount / (len(args))
        self.balance += amount
        for person in args:
            person.balance -= money
