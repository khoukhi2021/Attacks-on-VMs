
import tkinter as Tk
import tkinter.scrolledtext as tkst
import re


class InformationView(object):

    def __init__(self, GUI):
        self._GUI = GUI
        self._informationText = "Resources/Information/General.txt"
        self._scrolledText = tkst.ScrolledText(self._GUI.getContent(), wrap="word", font=("Segoe UI", "11"))

    def selectInformationText(self):
        if self._GUI.getAttack() == '':
            self._informationText = "Resources/Information/General.txt"
        else:
            self._informationText = "Resources/Information/" + self._GUI.getAttack() + ".txt"

    def createScrolledText(self):
        listLinesTitles = []
        lineNumber = 1
        self._GUI.destroyMainLabel()
        with open(self._informationText, 'r') as file:
            lines = file.readlines()
            for content_line in lines:
                pattern = '^[0-9]'
                if re.match(pattern, content_line):
                    self.addListTitles(listLinesTitles, lineNumber, content_line)
                self._scrolledText.insert(Tk.END, content_line)
                lineNumber += 1
        self.addTitleFont(listLinesTitles)
        self._scrolledText.config(state=Tk.DISABLED)
        self._scrolledText.grid(column=4, row=1, columnspan=5, rowspan=3, sticky='EWNS')

    def addListTitles(self, list_titles, number_line, content_line):
        list_titles.append(str(number_line) + "." + str(0))
        list_titles.append(str(number_line) + "." + str(len(content_line) - 1))

    def addTitleFont(self,list_titles):
        for index in range(0, len(list_titles) - 1, 2):
            self._scrolledText.tag_add("title", list_titles[index], list_titles[index + 1])
            self._scrolledText.tag_config("title", foreground="#C70039", font=("Georgia", "16", "bold"), underline=1)

    def displayScrolledText(self):
        self._GUI.changeMainLabelTitle("INFORMATION")
        self._scrolledText = tkst.ScrolledText(self._GUI.getContent(), wrap="word", font=("Segoe UI", "11"))
        self.selectInformationText()
        self.createScrolledText()
        self._GUI.updateMainLabel(self._scrolledText)
