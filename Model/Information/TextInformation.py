
import tkinter as Tk
import tkinter.scrolledtext as tkst
import re


class TextInformation(object):

    def __init__(self, typeAttack, currentContent):
        self._typeAttack = typeAttack
        self._scrolledText = tkst.ScrolledText(currentContent, wrap="word", font=("Segoe UI", "11"))

    def selectInformationText(self):
        if self._typeAttack == 'Extract Images':
            return "Model/Information/Resources/General.txt"
        if self._typeAttack == '':
            return "Model/Information/Resources/General.txt"
        else:
            return "Model/Information/Resources/" + self._typeAttack + ".txt"

    def createScrolledText(self):
        listLinesTitles = []
        lineNumber = 1
        typeAttack = self.selectInformationText()
        with open(typeAttack, 'r') as file:
            lines = file.readlines()
            for content_line in lines:
                pattern = '^[0-9]'
                if re.match(pattern, content_line):
                    self.addListTitles(listLinesTitles, lineNumber, content_line)
                self._scrolledText.insert(Tk.END, content_line)
                lineNumber += 1
        self.addTitleFont(listLinesTitles)
        return self._scrolledText

    def addListTitles(self, list_titles, number_line, content_line):
        list_titles.append(str(number_line) + "." + str(0))
        list_titles.append(str(number_line) + "." + str(len(content_line) - 1))

    def addTitleFont(self,list_titles):
        for index in range(0, len(list_titles) - 1, 2):
            self._scrolledText.tag_add("title", list_titles[index], list_titles[index + 1])
            self._scrolledText.tag_config("title", foreground="#C70039", font=("Georgia", "16", "bold"), underline=1)
