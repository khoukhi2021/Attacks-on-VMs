import tkinter.ttk as ttk
import tkinter as Tk


class MainView(object):

    def __init__(self, presenter):
        self._presenter = presenter
        self._root = Tk.Tk()
        self._content = ttk.Frame(self._root)
        self.createRoot()
        self.createLabelWidgets()
        self.createButtonWidget()
        self.createComboBoxAttack()
        self.updateFileComboBox([])
        self.placeWidgets()
        self.makeResizableWidgets()

    def start(self):
        self._root.mainloop()

    def createRoot(self):
        self._content.grid(column=0, row=0, columnspan=8, rowspan=3, sticky=('EWNS'))
        self._root.title('Platform of Attacks Simulation')
        self._root.tk.call('wm', 'iconphoto', self._root._w,
                           Tk.PhotoImage(file='View/Resources/Pictures/Logo ensicaen.png'))

    def displayRoot(self):
        self._root.mainloop()

    def createLabelWidgets(self):
        self._AttackLabel = Tk.Label(self._content, bg='SystemButtonFace', text="Attack Choice", relief='sunken',
                                     justify='center')
        self._fileLabel = Tk.Label(self._content, bg='SystemButtonFace', text="File Choice", relief='sunken',
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
        self._attackCombobox.grid(column=0, row=1, columnspan=4, rowspan=1, sticky=('EWNS'))
        self._fileLabel.grid(column=0, row=2, columnspan=4, rowspan=1, sticky=('EWNS'))
        self._fileComboxBox.grid(column=0, row=3, columnspan=4, rowspan=1, sticky=('EWNS'))
        self._mainLabel.grid(column=4, row=1, columnspan=7, rowspan=3, sticky=('EWNS'))
        self._informationButton.grid(column=0, row=4, columnspan=1, rowspan=1, sticky=('EWNS'))
        self._startButton.grid(column=2, row=4, columnspan=1, rowspan=1, sticky=('EWNS'))

    def createComboBoxAttack(self):
        attacksList = ['ARP Poisoning', 'DHCP Poisoning', 'VoIP Eavesdropping', 'Extract Images']
        self._attackCombobox = ttk.Combobox(self._content, state="readonly", values=attacksList)
        self._attackCombobox.bind("<<ComboboxSelected>>", lambda event, attack=self.getAttack(): self.callback(attack))

    def callback(self, attack):
        if self.getAttack() == 'VoIP Eavesdropping':
            self.updateFileComboBox(['call.wav', 'forensic.wav'])
            self._fileComboxBox.current(0)
        elif self.getAttack() == 'Extract Images':
            self.updateFileComboBox(['cards.pcap', 'GIF.pcap'])
            self._fileComboxBox.current(0)
        else:
            self.updateFileComboBox([])


    def updateFileComboBox(self, list):
        self._fileComboxBox = ttk.Combobox(self._content, state="readonly", values=list)
        self._fileComboxBox.grid(column=0, row=3, columnspan=4, rowspan=1, sticky=('EWNS'))

    def getAttack(self):
        return self._attackCombobox.get()

    def getFile(self):
        return self._fileComboxBox.get()

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
        self._mainLabel.grid_remove()
        self._mainLabel = new_widget

    def clearMainLabel(self):
        self._mainLabel.image.blank()

    def displayScrolledText(self, scrolledText):
        self.changeMainLabelTitle("INFORMATION")
        scrolledText.config(state=Tk.DISABLED)
        scrolledText.grid(column=4, row=1, columnspan=5, rowspan=3, sticky='EWNS')
        self.updateMainLabel(scrolledText)

    def displayExcel(self, treeview):
        self.changeMainLabelTitle("RESULTS")
        self.updateMainLabel(treeview)

    def displayAudioWidget(self, audio):
        self._mainLabel.grid_remove()
        self.changeMainLabelTitle("RESULTS")

        playButtonImage = Tk.PhotoImage(file='View/Resources/Pictures/play.png')
        playButton = Tk.Button(self._content, image=playButtonImage, justify='center',
                               command=lambda: audio.play())
        playButton.image = playButtonImage

        pauseButtonImage = Tk.PhotoImage(file='View/Resources/Pictures/pause.png')
        pauseButton = Tk.Button(self._content, image=pauseButtonImage, justify='center',
                                command=lambda: audio.managePause())
        pauseButton.image = pauseButtonImage

        stopButtonImage = Tk.PhotoImage(file='View/Resources/Pictures/stop.png')
        stopButton = Tk.Button(self._content, image=stopButtonImage, justify='center',
                               command=lambda: audio.close())
        stopButton.image = stopButtonImage

        playButton.grid(column=4, row=3, columnspan=1, rowspan=1, sticky=('EWNS'))
        pauseButton.grid(column=5, row=3, columnspan=1, rowspan=1, sticky=('EWNS'))
        stopButton.grid(column=6, row=3, columnspan=1, rowspan=1, sticky=('EWNS'))
