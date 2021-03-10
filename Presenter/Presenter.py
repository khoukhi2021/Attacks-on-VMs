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
        content = self.view.getContent()
        interfaceResult = ResultInterface()
        if attack == 'VoIP Eavesdropping':
            self.view.displayAudioWidget(interfaceResult.create_results(attack, content))
        elif attack == 'ARP Poisoning' or attack == 'DHCP Poisoning':
            result = interfaceResult.create_results(attack,content)
            self.view.displayExcel(result[0], result[1], result[2])
        else:
            pass

    def display_results(self):
        # Gives the results to the graphic user interface with the right format
        pass

    def get_results(self):
        # Gets the results form the attack and transform them in the right format
        pass

    def init(self):
        # Should be used to set all the things we could need on the app launch
        pass

    def launch_attack(self, attack_type: str):
        # Launch the attack selected, is called by the graphic user interface when an attack launch is clicked
        # I know if, elseif clause isn't sexy but for now I have no other idea
        pass
