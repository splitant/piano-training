# coding: utf-8
 
from Tkinter import * 
import json
import csv

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

csvfile = open('../letter_schema_chores.csv', 'r')
jsonfile = open('../letter_schema_chores.json', 'w')

fieldnames = ("Letter","Schema")
reader = csv.DictReader(csvfile, fieldnames)

for row in reader:
    print row
    json.dump(row, jsonfile)
    jsonfile.write('\n')

fenetre.mainloop()
