from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import constants

class Unified_Tool(ttk.Frame):
    # =============================================================================
    # Main setup options
    def __init__(self, isapp=True, name='unified_tool'):
        ttk.Frame.__init__(self, name=name)
        self.master.title("Unified Tool")
        self.pack(expand=Y, fill=BOTH)
        self.isapp = isapp
        self._create_widgets()
        file_name = StringVar()

    def _create_widgets(self):
        self._create_panels()

    def _create_panels(self):
        panel = Frame(self, name='panel')
        panel.pack(side=TOP, fill=BOTH, expand=Y)
        # create the notebook
        nb = ttk.Notebook(panel, name='notebook_panel')
        nb.pack(fill=BOTH, expand=Y, padx=2, pady=3)
        self._create_ca_del_tab(nb)
        #self._create_traversal_tab(nb)
        #self._create_tot_tab(nb)
        #self._create_zcc_tab(nb)

    # =============================================================================
    # Delineation tab
    def load_file(self):
        self.file_name = filedialog.askopenfilename(filetypes=([('All files', '*.*'),
                                                                  ('Text files', '*.txt'),
                                                                  ('CSV files', '*.csv')]))
        return self.file_name

    # =============================================================================
    # Delineation tab
    def _create_ca_del_tab(self, nb):

        # variable to store the filename
        del_filename = StringVar()

        # frame to hold content
        frame = ttk.Frame(nb, name='ca_delineation')

        # widgets to be displayed on 'Description' tab
        msg = ["For delineating the catchment area of a point or collection of points. In "
               "the file selection box to the left, select the input file containing the points "
               "for catchment area delineation."]
        lbl_intro = ttk.Label(frame, wraplength='4i', justify=LEFT, anchor=N,
                        text=''.join(msg))

        # button for selecting the input file
        btn_del_select_file = ttk.Button(frame, text="Browse", command=self.load_file, width=10)
        # button for triggering the task
        btn_del = ttk.Button(frame, text='Delineate!', underline=0,
                              command=lambda v=del_filename: self._delineate(del_filename))

        # label that displays the input file name
        lbl_del = ttk.Label(frame, textvariable=del_filename, name='delineate')

        # position and set resize behaviour
        lbl_intro.grid(row=0, column=0, columnspan=2, sticky='new', pady=5)
        lbl_del.grid(row=1, column=1,  pady=(2,4))
        btn_del_select_file.grid(row=1, column=0, pady=(2,4))
        btn_del.grid(row=2, column=0, pady=(2,4))
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure((0,1), weight=1, uniform=1)

        # add to notebook (underline = index for short-cut character)
        nb.add(frame, text='CA Delineation', underline=0, padding=2)

    def _delineate(self, v):
        v.set('Delineating....')
        self.update()

app = Unified_Tool()
#app.geometry("1280x620")
#ani = animation.FuncAnimation(f, animate, interval=1000)
