import tkinter as tk
import startno_okno as sto

number_people = int(sto.Start_number().number_people)
people = sto.Start_names(number_people).names

print(people)