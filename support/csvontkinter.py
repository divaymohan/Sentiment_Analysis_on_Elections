import tkinter
import csv
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import constants
root = tkinter.Tk()

file_name = StringVar()
def load_file(self):
   self.file_name = filedialog.askopenfilename(filetypes=([('All files', '*.*'),
                                                           ('Text files', '*.txt'),
                                                           ('CSV files', '*.csv')]))
   print(self.file_name)



# open file
with open(str(file_name),newline="") as file:
   reader = csv.reader(file)

   # r and c tell us where to grid the labels
   r = 0
   for col in reader:
      c = 0
      for row in col:
         # i've added some styling
         label = tkinter.Label(root, width =20,height= 4,\
                               text = row, relief = tkinter.RIDGE)
         label.grid(row = r, column = c)
         c += 1
      r += 1

root.mainloop()

