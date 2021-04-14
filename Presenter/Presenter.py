from Model.Information.TextInformation import TextInformation
from Model.Model import Model
from Model.ResultAttack.ResultInterface import ResultInterface
from View.MainView import MainView


class Presenter:

    def __init__(self):
        self.view = MainView(self)
        self.model = Model()

    def launchView(self):
        self.view.start()

    def getInformationText(self):
        textEditor = TextInformation(self.view.getAttack(),self.view.getContent())
        scrolledText = textEditor.createScrolledText()
        self.view.displayScrolledText(scrolledText)

    def getResulAttack(self):
        attack = self.view.getAttack()
        file = self.view.getFile()
        content = self.view.getContent()
        interfaceResult = ResultInterface()
        if attack == 'VoIP Eavesdropping':
            self.view.displayAudioWidget(interfaceResult.create_results(attack,file, content))
        elif attack == 'ARP Poisoning' or attack == 'DHCP Poisoning':
            result = interfaceResult.create_results(attack,None,content)
            self.view.displayExcel(result)
        elif attack == 'Extract Images':
            interfaceResult.create_results(attack,file,content)
        else:
            pass
