import tkinter.ttk as ttk
import tkinter as Tk
from View.ResultView import ResultView
from View.InformationView import InformationView


class MainView(object):

    def __init__(self):
        self._root = Tk.Tk()
        self._content = ttk.Frame(self._root)
        self.createRoot()
        self.createLabelWidgets()
        self.createButtonWidget()
        self.createComboBoxAttack()
        self.placeWidgets()
        self.makeResizableWidgets()
        self._informationView = InformationView(self)
        self._resultView = ResultView(self)
        self._root.mainloop()

    def createRoot(self):
        self._content.grid(column=0, row=0, columnspan=8, rowspan=3, sticky=('EWNS'))
        self._root.title('Platform of Attacks Simulation')
        self._root.tk.call('wm', 'iconphoto', self._root._w, Tk.PhotoImage(file='Resources/Pictures/Logo ensicaen.png'))

    def displayRoot(self):
        self._root.mainloop()

    def createLabelWidgets(self):
        self._AttackLabel = Tk.Label(self._content, bg='SystemButtonFace', text="Attack Choice", relief='sunken',
                                     justify='center')
        self.changeMainLabelTitle("NETWORK")

        networkImage = Tk.PhotoImage(file='Resources/Pictures/NetworkImage.png')
        self._mainLabel = Tk.Label(self._content, image=networkImage, justify='center')
        self._mainLabel.image = networkImage

    def changeMainLabelTitle(self, title):
        self._mainLabelTitle = Tk.Label(self._content, bg='#4ABBBF', text=title, font=("Segoe UI", "14", "bold"),
                                        relief='sunken', justify='center')
        self._mainLabelTitle.grid(column=4, row=0, columnspan=7, rowspan=1, sticky=('EWNS'))

    def createButtonWidget(self):
        informationButtonImage = Tk.PhotoImage(file='Resources/Pictures/InformationButton.png')
        self._informationButton = Tk.Button(self._content, image=informationButtonImage,
                                            command=lambda: self._informationView.displayScrolledText())
        self._informationButton.image = informationButtonImage
        self._startButton = Tk.Button(self._content, text="Start", bg='#4ABBBF',
                                      command=lambda: self._resultView.updateResultView())

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


if __name__ == '__main__':
    MainView()
