import tkinter.ttk as ttk
import tkinter as Tk
from Model.ResultAttack.ResultCreator import ResultCreator
from Model.Information.TextInformation import TextInformation


class MainView(object):

    def __init__(self,presenter):
        self._presenter = presenter
        self._root = Tk.Tk()
        self._content = ttk.Frame(self._root)
        self.createRoot()
        self.createLabelWidgets()
        self.createButtonWidget()
        self.createComboBoxAttack()
        self.placeWidgets()
        self.makeResizableWidgets()
        #self._informationView = TextInformation(self)
        #self._resultView = ResultCreator(self)

    def start(self):
        self._root.mainloop()

    def createRoot(self):
        self._content.grid(column=0, row=0, columnspan=8, rowspan=3, sticky=('EWNS'))
        self._root.title('Platform of Attacks Simulation')
        self._root.tk.call('wm', 'iconphoto', self._root._w, Tk.PhotoImage(file='View/Resources/Pictures/Logo ensicaen.png'))

    def displayRoot(self):
        self._root.mainloop()

    def createLabelWidgets(self):
        self._AttackLabel = Tk.Label(self._content, bg='SystemButtonFace', text="Attack Choice", relief='sunken',
                                     justify='center')
        self.changeMainLabelTitle("NETWORK")

        networkImage = Tk.PhotoImage(file='View/Resources/Pictures/NetworkImage.png')
        self._mainLabel = Tk.Label(self._content, image=networkImage, justify='center')
        self._mainLabel.image = networkImage

    def changeMainLabelTitle(self, title):
        self._mainLabelTitle = Tk.Label(self._content, bg='#4ABBBF', text=title, font=("Segoe UI", "14", "bold"),
                                        relief='sunken', justify='center')
        self._mainLabelTitle.grid(column=4, row=0, columnspan=7, rowspan=1, sticky=('EWNS'))

    def createButtonWidget(self):
        informationButtonImage = Tk.PhotoImage(file='View/Resources/Pictures/InformationButton.png')
        self._informationButton = Tk.Button(self._content, image=informationButtonImage,
                                            command=lambda: self._presenter.getInformationText())
        self._informationButton.image = informationButtonImage
        self._startButton = Tk.Button(self._content, text="Start", bg='#4ABBBF',
                                      command=lambda: self._presenter.getResulAttack())

    def placeWidgets(self):
        self._mainLabelTitle.grid(column=4, row=0, columnspan=7, rowspan=1, sticky=('EWNS'))
        self._AttackLabel.grid(column=0, row=0, columnspan=4, rowspan=1, sticky=('EWNS'))
        self._attackCombobox.grid(column=0, row=1, columnspan=2, rowspan=1, sticky=('EWNS'))
        self._mainLabel.grid(column=4, row=1, columnspan=7, rowspan=3, sticky=('EWNS'))
        self._informationButton.grid(column=0, row=3, columnspan=1, rowspan=1, sticky=('EWNS'))
        self._startButton.grid(column=2, row=3, columnspan=1, rowspan=1, sticky=('EWNS'))

    def createComboBoxAttack(self):
        attacksList = ['ARP Poisoning', 'DHCP Poisoning', 'VoIP Eavesdropping']
        self._attackCombobox = ttk.Combobox(self._content, state="readonly", values=attacksList)

    def getAttack(self):
        return self._attackCombobox.get()

    def getContent(self):
        return self._content

    def makeResizableWidgets(self):
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)
        for i in range(4):
            self._content.rowconfigure(i, weight=1)
        for j in range(9):
            self._content.columnconfigure(j, weight=1)

    def updateMainLabel(self, new_widget):
        self._mainLabel = new_widget

    def clearMainLabel(self):
        self._mainLabel.image.blank()
        self._NetworkImage.image = None

    def destroyMainLabel(self):
        self._mainLabel.destroy()

    def displayScrolledText(self,scrolledText):
        self.changeMainLabelTitle("INFORMATION")
        scrolledText.config(state=Tk.DISABLED)
        scrolledText.grid(column=4, row=1, columnspan=5, rowspan=3, sticky='EWNS')
        self.updateMainLabel(scrolledText)

    def displayExcel(self,treeview,max_row,max_column):
        self.changeMainLabelTitle("RESULTS")
        self.treeview_scrollbar = ttk.Scrollbar(self._GUI._content, orient="vertical",
                                                command=self._GUI._mainLabel.yview)
        treeview.configure(yscrollcommand=self.treeview_scrollbar.set)
        self.treeview_scrollbar.grid(row=1, column=9, sticky=('EWNS'))
        treeview.grid(column=4, row=1, columnspan=max_column, rowspan=max_row, sticky=('EWNS'))
        self.updateMainLabel(treeview)

    def displayAudioWidget(self,audio):
        self.changeMainLabelTitle("RESULTS")
        self.destroyMainLabel()

        playButtonImage = Tk.PhotoImage(file='View/Resources/Pictures/play.png')
        playButton = Tk.Button(self._content, image=playButtonImage, justify='center',
                                          command=lambda: audio.play(block=False))
        playButton.image = playButtonImage

        pauseButtonImage = Tk.PhotoImage(file='View/Resources/Pictures/pause.png')
        pauseButton = Tk.Button(self._content, image=pauseButtonImage, justify='center',
                                           command=lambda: self.managePause())
        pauseButton.image = pauseButtonImage

        stopButtonImage = Tk.PhotoImage(file='View/Resources/Pictures/stop.png')
        stopButton = Tk.Button(self._content, image=stopButtonImage, justify='center',
                                          command=lambda: audio.close())
        stopButton.image = stopButtonImage

        playButton.grid(column=4, row=3, columnspan=1, rowspan=1, sticky=('EWNS'))
        pauseButton.grid(column=5, row=3, columnspan=1, rowspan=1, sticky=('EWNS'))
        stopButton.grid(column=6, row=3, columnspan=1, rowspan=1, sticky=('EWNS'))
