from new import*
from new import animate
import new as n
import naiveworking as nw
import Mbayes as mb
import Bbayes
import LogisticReg
import hybridworking
import NuSVC_classifier
import samm as s
class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "SentAna App")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command=lambda: n.popupmessage('Not supported just yet!'))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        exchangeChoice = tk.Menu(menubar, tearoff=1)
        exchangeChoice.add_command(label="Naive-Bayes",
                                   command=lambda: self.show_frame(NaiveBayesGUI))
        exchangeChoice.add_command(label="MultinomialNaivebayes",
                                   command=lambda: self.show_frame(MultinomialNaivebayes))
        exchangeChoice.add_command(label="BinomialNaivebayes",
                                   command=lambda: self.show_frame(BinomialNaivebayes))
        exchangeChoice.add_command(label="LogisticRegression",
                                   command=lambda: self.show_frame(LogisticRegeration))
        exchangeChoice.add_command(label="NuSVC",
                                   command=lambda: self.show_frame(NuSVC))

        exchangeChoice.add_command(label="Bag-Of-Word",
                                   command=lambda: self.show_frame(BOW))
        exchangeChoice.add_command(label="Hybrid",
                                   command=lambda: self.show_frame(Hybrid))
        menubar.add_cascade(label="SentAna", menu=exchangeChoice)

        dataTF = tk.Menu(menubar, tearoff=1)
        dataTF.add_command(label="Tick",
                           command=lambda: n.popupmessage('tick'))
        dataTF.add_command(label="1 day",
                           command=lambda: n.popupmessage('1d'))
        dataTF.add_command(label="3 day",
                           command=lambda: n.popupmessage('3d'))
        dataTF.add_command(label="1 Week",
                           command=lambda: n.popupmessage('7d'))
        menubar.add_cascade(label="Data Time Frame", menu=dataTF)

        TIME_INTR = tk.Menu(menubar, tearoff=1)

        TIME_INTR.add_command(label="Tick",
                          command=lambda: n.popupmessage('tick'))
        TIME_INTR.add_command(label="1 minute",
                          command=lambda: n.popupmessage('1Min'))
        TIME_INTR.add_command(label="5 minute",
                          command=lambda: n.popupmessage('5Min'))
        TIME_INTR.add_command(label="15 minute",
                          command=lambda: n.popupmessage('15Min'))
        TIME_INTR.add_command(label="30 minute",
                          command=lambda: n.popupmessage('30Min'))
        TIME_INTR.add_command(label="1 Hour",
                          command=lambda: n.popupmessage('1H'))
        TIME_INTR.add_command(label="3 Hour",
                          command=lambda: n.popupmessage('3H'))
        menubar.add_cascade(label="Time Interval", menu=TIME_INTR)

        topIndi = tk.Menu(menubar, tearoff=1)
        topIndi.add_command(label="None",
                            command=lambda: n.popupmessage('none'))
        topIndi.add_separator()
        topIndi.add_command(label="MODI",
                            command=lambda: n.popupmessage('MODI'))
        topIndi.add_command(label="RAHUL",
                            command=lambda: n.popupmessage('RAHUL'))
        topIndi.add_command(label="Kejriwal",
                            command=lambda: n.popupmessage('Kejriwal'))

        menubar.add_cascade(label="Top Indicator", menu=topIndi)

        mainI = tk.Menu(menubar, tearoff=1)
        mainI.add_command(label="None",
                          command=lambda: n.popupmessage('none'))
        mainI.add_separator()
        mainI.add_command(label="BAR",
                          command=lambda: n.popupmessage('BAR'))
        mainI.add_command(label="Scatter Plot",
                          command=lambda: n.popupmessage('Scatter Plot'))
        mainI.add_command(label="Geographical Indentation",
                          command=lambda: n.popupmessage('Geographical Indentation'))
        menubar.add_cascade(label="Graph Indicator", menu=mainI)


        startStop = tk.Menu(menubar, tearoff=1)
        startStop.add_command(label="Resume",
                              command=lambda: n.popupmessage('start'))
        startStop.add_command(label="Pause",
                              command=lambda: n.popupmessage('stop'))
        menubar.add_cascade(label="Resume/Pause Client", menu=startStop)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tutorial", command=lambda :n.popupmessage("tutorial"))
        menubar.add_cascade(label="Help", menu=helpmenu)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}
        for F in (StartPage, Hybrid,NaiveBayesGUI,MultinomialNaivebayes,BinomialNaivebayes,LogisticRegeration,NuSVC,BOW):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

        tk.Tk.iconbitmap(self, default='logo.ico')

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class StartPage(tk.Frame):
    file_name = " "
    def load_file(self):
        self.file_name = filedialog.askopenfilename(filetypes=([('All files', '*.*'),
                                                                ('Text files', '*.txt'),
                                                                ('CSV files', '*.csv')]))
        print(type(self.file_name))
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""This prediction may be wrong.if you want to contineu press 'agree' else 'disagree'."""), font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Agree",
                             command=lambda: controller.show_frame(Hybrid))
        button1.pack()

        button2 = ttk.Button(self, text="Disagree",
                             command=quit)
        button2.pack()
        button3 = ttk.Button(self, text="upload file",
                             command=self.load_file)
        button3.pack()
        label1 = tk.Label(self, text= " ".join(self.file_name), font=LARGE_FONT)
        label1.pack(pady=10, padx=10)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class Hybrid(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hybrid Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(s.fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button2 = ttk.Button(self,text = "execute model",
                             command = lambda: n.popupmessage(hybridworking.Accuracy))
        button2.pack()
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

class NaiveBayesGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NaiveBayesGUI Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(n.f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button2 = ttk.Button(self, text="execute model",
                             command=lambda: n.popupmessage(nw.Accuracy))
        button2.pack()

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class MultinomialNaivebayes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MultinomialNaivebayes Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(n.f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button2 = ttk.Button(self, text="execute model",
                             command=lambda: n.popupmessage(mb.Accuracy))
        button2.pack()

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
class BinomialNaivebayes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BinomialNaivebayes Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(n.f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button2 = ttk.Button(self, text="execute model",
                             command=lambda: n.popupmessage(Bbayes.Accuracy))
        button2.pack()

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
class LogisticRegeration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="LogisticRegression Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(n.f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button2 = ttk.Button(self, text="execute model",
                             command=lambda: n.popupmessage(LogisticReg.Accuracy))
        button2.pack()

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class NuSVC(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NuSVC Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        canvas = FigureCanvasTkAgg(n.f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button2 = ttk.Button(self, text="execute model",
                             command=lambda: n.popupmessage(NuSVC_classifier.Accuracy))
        button2.pack()

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class BOW(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BOW Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(n.f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

app = SeaofBTCapp()
app.geometry("800x650")
ani = animation.FuncAnimation(n.f, animate, interval=1000)
app.mainloop()